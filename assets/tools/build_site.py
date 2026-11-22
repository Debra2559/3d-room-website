#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3D 小房间个人网站 · 一键生成成品（给 AI 用，用户不需要碰）

只用 Python 自带的库（有 Pillow 或 macOS 的 sips 时会顺便压缩照片）。

用法：
  python3 build_site.py site.json --out my-site            生成成品网站文件夹
  python3 build_site.py site.json --out my-site --open     生成后用浏览器打开
  python3 build_site.py site.json --check                  只检查内容，不生成
  python3 build_site.py site.json --out my-site --with-ai  连同“真 AI 分身”后端（api/、knowledge/、vercel.json）一起放进去

照片怎么放：在 site.json 里，把照片位置（关于我 photo、作品 src / poster、图集 imgs、城市 photo、自定义 img）
直接写成用户照片在这台电脑上的路径（绝对路径，或相对 site.json 的路径）。脚本会把照片复制进 my-site/media/、
压缩，并在成品里改成 media/ 开头的路径。site.json 本身不会被改。

结束时会打印一份报告：放好了哪些照片、哪些位置还空着、哪些文件找不到、内容里有没有写错的地方。
退出码：0 = 成功；1 = 内容有错误（没有生成）；2 = 用法错误。
"""
import argparse, json, os, re, shutil, subprocess, sys, webbrowser

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_TEMPLATE = os.path.normpath(os.path.join(HERE, "..", "template"))

SCENES = {"studio", "kitchen", "bar", "cabinet", "cafe", "custom"}
BASES = {"island", "grass", "cloud", "water", "rock", "pedestal", "none"}
TYPES = {"about", "journey", "works", "products", "articles", "hobbies", "travel", "contact", "chat", "custom"}
STYLES = {
    "about": {"profile", "letter"}, "journey": {"book", "timeline", "cards"}, "works": {"bento"},
    "products": {"carousel", "grid"}, "articles": {"list"}, "hobbies": {"bento"},
    "travel": {"map", "album"}, "contact": {"letter", "cards"},
}
IMG_EXT = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".heic", ".heif", ".bmp", ".tif", ".tiff"}
VID_EXT = {".mp4", ".mov", ".m4v", ".webm"}
PHOTO_KEYS = {"photo", "src", "poster", "img"}
MAX_SIDE = 1600

errors, warns = [], []


def load_json(path):
    raw = open(path, encoding="utf-8-sig").read().strip()
    raw = re.sub(r"^```(?:json|js|javascript)?\s*", "", raw, flags=re.I)
    raw = re.sub(r"```\s*$", "", raw).strip()
    raw = re.sub(r"^window\.SITE\s*=\s*", "", raw).rstrip().rstrip(";")
    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        line = raw.splitlines()[e.lineno - 1] if e.lineno - 1 < len(raw.splitlines()) else ""
        print(f"❌ site.json 不是合法的 JSON：第 {e.lineno} 行第 {e.colno} 列，{e.msg}\n   这一行是：{line.strip()[:120]}")
        sys.exit(1)


def prop_kinds(template_html):
    m = re.search(r"const PROP_KINDS\s*=\s*\{([\s\S]*?)\n\};", template_html)
    if not m:
        return None
    return set(re.findall(r"^\s{2}([a-z]+)\s*:", m.group(1), flags=re.M))


def label_of(site, path):
    """把 JSON 路径翻译成用户看得懂的位置，例如「作品集 · 第 2 件《手绘地图》· 封面」"""
    m = re.match(r"modules\[(\d+)\](.*)", path)
    if not m:
        return path
    mod = site["modules"][int(m.group(1))]
    rest = m.group(2)
    name = mod.get("label") or mod.get("type")
    parts = [name]
    it = re.search(r"\.(items|cities|blocks)\[(\d+)\]", rest)
    if it:
        arr = (mod.get("data") or {}).get(it.group(1)) or []
        i = int(it.group(2))
        obj = arr[i] if i < len(arr) else {}
        title = obj.get("t") or obj.get("title") or obj.get("name") or obj.get("h") or ""
        unit = {"items": "件", "cities": "座城市", "blocks": "段"}[it.group(1)]
        title = title.strip("《》")
        parts.append(f"第 {i + 1} {unit}" + (f"《{title}》" if title else ""))
    key = re.findall(r"\.([a-z]+)(?:\[\d+\])*$", rest)
    key = key[0] if key else ""
    parts.append({"photo": "照片", "src": "图片 / 视频", "poster": "视频封面", "img": "配图", "imgs": "图集"}.get(key, key))
    return " · ".join(p for p in parts if p)


def walk(o, path=""):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from walk(v, f"{path}.{k}" if path else k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from walk(v, f"{path}[{i}]")
    else:
        yield path, o


def set_path(o, path, value):
    toks = re.findall(r"[^.\[\]]+|\[\d+\]", path)
    for t in toks[:-1]:
        o = o[int(t[1:-1])] if t.startswith("[") else o[t]
    t = toks[-1]
    if t.startswith("["):
        o[int(t[1:-1])] = value
    else:
        o[t] = value


def validate(site, kinds):
    if not isinstance(site, dict) or not isinstance(site.get("modules"), list):
        errors.append("最外层要有 modules 数组（网站的板块列表）")
        return
    if site.get("scene", "studio") not in SCENES:
        errors.append(f"scene 写成了 {site.get('scene')!r}，只能是 {', '.join(sorted(SCENES))}（自己搭的房间用 custom）")
    if site.get("scene") == "custom" and not isinstance(site.get("room"), dict):
        errors.append("scene 是 custom，但没有写 room（房间里摆什么）")
    base = site.get("base") or (site.get("room") or {}).get("base")
    if base and base not in BASES:
        errors.append(f"base 写成了 {base!r}，只能是 {', '.join(sorted(BASES))}")
    ids = set()
    for i, m in enumerate(site["modules"]):
        t = m.get("type")
        if t not in TYPES:
            errors.append(f"第 {i + 1} 个板块的 type 是 {t!r}，只能是 {', '.join(sorted(TYPES))}")
            continue
        mid = m.get("id") or t
        if mid in ids:
            errors.append(f"板块 id {mid!r} 重复了（每个板块的 id 要不一样）")
        ids.add(mid)
        st = m.get("style")
        if st and t in STYLES and st not in STYLES[t]:
            warns.append(f"「{m.get('label', t)}」的样子 {st!r} 不存在，会用默认样子（可选：{', '.join(sorted(STYLES[t]))}）")
    room = site.get("room") or {}
    slot_keys = set()
    if kinds:
        for j, p in enumerate(room.get("props") or []):
            k = p.get("kind")
            if k not in kinds:
                errors.append(f"房间里第 {j + 1} 件东西的 kind 是 {k!r}，没有这种物件（可用的见 references/scenes.md）")
            if p.get("key"):
                slot_keys.add(p["key"])
    for m in site["modules"]:
        obj = m.get("object")
        if site.get("scene") == "custom" and obj and slot_keys and obj not in slot_keys and m.get("type") != "chat":
            warns.append(f"「{m.get('label', m.get('type'))}」挂在 {obj!r} 上，但房间里没有 key 是 {obj!r} 的东西，它只会出现在导航里")
    if site.get("demo"):
        warns.append("内容里有 demo 字段，成品里已自动删掉（否则网页会显示“示例内容 / 编辑中”按钮）")


def find_local(ref, base_dir):
    if not isinstance(ref, str) or not ref or ref.startswith(("http://", "https://", "data:", "//")):
        return None
    p = os.path.expanduser(ref)
    cands = [p] if os.path.isabs(p) else [os.path.join(base_dir, p), os.path.join(os.getcwd(), p)]
    for c in cands:
        if os.path.isfile(c):
            return os.path.abspath(c)
    return None


def slug(s, used):
    base = re.sub(r"[^a-zA-Z0-9-]+", "-", s).strip("-").lower()[:40] or "photo"
    name, n = base, 2
    while name in used:
        name, n = f"{base}-{n}", n + 1
    used.add(name)
    return name


def media_name(site, path, local):
    """按位置起文件名，例如 about、works-2、travel-dali；文件名本来就是英文时直接用。"""
    own = os.path.splitext(os.path.basename(local))[0]
    if re.fullmatch(r"[A-Za-z0-9_-]{2,40}", own):
        return own
    m = re.match(r"modules\[(\d+)\](?:.*?\.(?:items|cities|blocks)\[(\d+)\])?", path)
    if not m:
        return "photo"
    mod = site["modules"][int(m.group(1))]
    return (mod.get("id") or mod.get("type") or "photo") + (f"-{int(m.group(2)) + 1}" if m.group(2) else "")


def compress(src, dst_noext):
    """返回写出的文件路径。优先 Pillow，其次 macOS sips，否则原样复制。"""
    ext = os.path.splitext(src)[1].lower()
    try:
        from PIL import Image, ImageOps  # type: ignore
        im = ImageOps.exif_transpose(Image.open(src))
        im.thumbnail((MAX_SIDE, MAX_SIDE))
        if im.mode in ("RGBA", "LA", "P"):
            im = im.convert("RGBA")
            out = dst_noext + ".webp"
            im.save(out, "WEBP", quality=82)
        else:
            out = dst_noext + ".jpg"
            im.convert("RGB").save(out, "JPEG", quality=84, optimize=True, progressive=True)
        return out
    except Exception:
        pass
    if shutil.which("sips") and ext in IMG_EXT:
        out = dst_noext + ".jpg"
        r = subprocess.run(["sips", "-s", "format", "jpeg", "-Z", str(MAX_SIDE), src, "--out", out], capture_output=True)
        if r.returncode == 0 and os.path.isfile(out):
            return out
    if ext in {".heic", ".heif", ".tif", ".tiff", ".bmp"}:
        warns.append(f"{os.path.basename(src)} 是 {ext} 格式，浏览器可能显示不了，又没有工具能转换：请换成 jpg / png")
    out = dst_noext + (ext if ext != ".jpeg" else ".jpg")
    shutil.copyfile(src, out)
    return out


def main():
    ap = argparse.ArgumentParser(description="把 site.json 生成成品网站文件夹")
    ap.add_argument("site")
    ap.add_argument("--out", help="成品文件夹，例如 my-site")
    ap.add_argument("--template", default=DEFAULT_TEMPLATE, help="模板文件夹（默认是 assets/template）")
    ap.add_argument("--check", action="store_true", help="只检查，不生成")
    ap.add_argument("--open", action="store_true", help="生成后用浏览器打开")
    ap.add_argument("--with-ai", action="store_true", help="带上真 AI 分身的后端文件（用 Vercel 上线时需要）")
    a = ap.parse_args()
    if not a.check and not a.out:
        ap.error("要么加 --out 文件夹，要么加 --check")

    tpl_html_path = os.path.join(a.template, "index.html")
    if not os.path.isfile(tpl_html_path):
        print(f"❌ 找不到模板：{tpl_html_path}\n   请确认 3d-room-website 文件夹完整（assets/template/index.html）。")
        sys.exit(2)
    tpl = open(tpl_html_path, encoding="utf-8").read()
    site = load_json(a.site)
    validate(site, prop_kinds(tpl))
    site.pop("demo", None)
    base_dir = os.path.dirname(os.path.abspath(a.site))

    # ---- 照片 / 视频 ----
    placed, empty, missing, used = [], [], [], set()
    media_jobs = []  # (json路径, 本地文件)
    for path, v in list(walk(site)):
        key = re.findall(r"([a-z]+)(?:\[\d+\])*$", path)
        key = key[0] if key else ""
        in_imgs = ".imgs[" in path
        if not (key in PHOTO_KEYS or in_imgs):
            continue
        if in_imgs and not re.search(r"\.imgs\[\d+\]\[[01]\]$", path):
            continue  # 图集里只有第 0、1 项是图片
        if v in ("", None):
            if key in {"photo", "src", "poster"}:
                empty.append(path)
            continue
        if not isinstance(v, str):
            continue
        local = find_local(v, base_dir)
        if local:
            media_jobs.append((path, local))
        elif v.startswith("media/"):
            local = find_local(os.path.join(a.template, v), base_dir)
            if local:
                media_jobs.append((path, local))
            else:
                missing.append((path, v))
        elif not v.startswith(("http://", "https://", "data:")) and os.path.splitext(v)[1].lower() in IMG_EXT | VID_EXT:
            missing.append((path, v))

    # chat 头像这类不是“照片位置”的空字段不提示
    empty = [p for p in empty if re.match(r"modules\[\d+\]\.data\.(photo|items\[\d+\]\.(src|poster))$", p)]
    for path in list(empty):
        mi = int(re.match(r"modules\[(\d+)\]", path).group(1))
        mod = site["modules"][mi]
        if path.endswith(".src"):
            it = mod["data"]["items"][int(re.search(r"items\[(\d+)\]", path).group(1))]
            if it.get("kind") not in ("image", "video"):
                empty.remove(path)
        if path.endswith(".photo") and mod.get("type") != "about":
            empty.remove(path)
        if path.endswith(".photo") and mod.get("style") == "letter":
            empty.remove(path)

    if errors:
        print("❌ 内容里有需要先改的地方（网站没有生成）：")
        for e in errors:
            print("   - " + e)
        for w in warns:
            print("   ⚠️ " + w)
        sys.exit(1)

    if a.check:
        print("✅ 内容检查通过")
        for w in warns:
            print("   ⚠️ " + w)
        if empty:
            print("📷 还空着的照片位置：")
            for p in empty:
                print("   - " + label_of(site, p))
        for p, v in missing:
            print(f"   ⚠️ 找不到文件 {v}（{label_of(site, p)}）")
        sys.exit(0)

    out = os.path.abspath(a.out)
    os.makedirs(os.path.join(out, "media"), exist_ok=True)
    shutil.copytree(os.path.join(a.template, "vendor"), os.path.join(out, "vendor"), dirs_exist_ok=True)
    if a.with_ai:
        for name in ("api", "knowledge"):
            src = os.path.join(a.template, name)
            if os.path.isdir(src):
                shutil.copytree(src, os.path.join(out, name), dirs_exist_ok=True)
        if os.path.isfile(os.path.join(a.template, "vercel.json")):
            shutil.copyfile(os.path.join(a.template, "vercel.json"), os.path.join(out, "vercel.json"))

    done = {}
    big_videos = []
    for path, local in media_jobs:
        if local in done:
            set_path(site, path, done[local])
            continue
        ext = os.path.splitext(local)[1].lower()
        name = slug(media_name(site, path, local), used)
        dst = os.path.join(out, "media", name)
        if os.path.commonpath([local, out]) == out:
            rel = os.path.relpath(local, out).replace(os.sep, "/")
        elif ext in VID_EXT:
            shutil.copyfile(local, dst + ext)
            rel = f"media/{name}{ext}"
            if os.path.getsize(local) > 8 * 1024 * 1024:
                big_videos.append(f"{os.path.basename(local)}（{os.path.getsize(local) // 1024 // 1024}MB）")
            if ext != ".mp4":
                warns.append(f"视频 {os.path.basename(local)} 不是 mp4，部分浏览器放不了；有 ffmpeg 的话转成 H.264 mp4 更稳")
        else:
            rel = "media/" + os.path.basename(compress(local, dst))
        done[local] = rel
        set_path(site, path, rel)
        placed.append((path, os.path.basename(local)))

    # ---- 写入成品 index.html ----
    js = json.dumps(site, ensure_ascii=False, indent=2).replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    html, n = re.subn(r'(<script id="site-content">)[\s\S]*?(</script>)', lambda m: f'<script id="site-content">\nwindow.SITE = {js};\n</script>', tpl, count=1)
    if n != 1:
        print("❌ 模板里找不到 <script id=\"site-content\">，模板可能被改坏了")
        sys.exit(2)
    title = " · ".join(x for x in [site.get("name"), site.get("brand")] if x) or "我的小房间"
    html = re.sub(r"<title>[\s\S]*?</title>", lambda m: f"<title>{title.replace('<', '')}</title>", html, count=1)
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(html)

    # ---- 报告 ----
    print(f"✅ 网站已生成：{os.path.join(out, 'index.html')}")
    print(f"   板块 {len(site['modules'])} 个；房间 {site.get('scene', 'studio')}；底座 {site.get('base') or (site.get('room') or {}).get('base') or 'island'}")
    if placed:
        print(f"📷 放好了 {len(placed)} 张照片 / 视频：")
        for p, f in placed:
            print(f"   - {label_of(site, p)} ← {f}")
    if empty:
        print("🔲 还空着的照片位置（访客那边不会显示空格子，只是少了图）：")
        for p in empty:
            print("   - " + label_of(site, p))
    for p, v in missing:
        print(f"   ⚠️ 找不到文件 {v}（{label_of(site, p)}），这个位置在网页上会是破图，请找到照片后重新生成")
    for v in big_videos:
        print(f"   ⚠️ 视频比较大：{v}，访客加载会慢，建议压到 8MB 以内")
    for w in warns:
        print("   ⚠️ " + w)
    if a.open:
        webbrowser.open("file://" + os.path.join(out, "index.html"))


if __name__ == "__main__":
    main()
