# 上线与 AI 分身

## 网站文件夹长这样
```
my-site/
├── index.html          ← 成品（内容已经写在里面）
├── vendor/three.min.js ← 3D 引擎（离线也能用；删掉会自动从国内/国外 CDN 下载）
├── media/              ← 你的照片、视频（JSON 里写 media/文件名）
├── api/chat.js         ← 可选：AI 分身的后端（Vercel 函数）
├── knowledge/*.md      ← 可选：AI 分身的知识库
└── vercel.json         ← 可选：配合 api/chat.js
```
双击 `index.html` 就能在本机打开预览（AI 分身是演示模式）。

## 上线方式（任选一个，都免费起步）

| 方式 | 适合 | 步骤 |
|---|---|---|
| **Vercel** | 想要真 AI 分身 | 安装 Node.js → 在文件夹里运行 `npx vercel --prod`，按提示登录。⚠️ `*.vercel.app` 在中国大陆访问不稳定，建议绑定自己的域名 |
| **Netlify Drop** | 最省事 | 打开 app.netlify.com/drop，把整个文件夹拖进去 |
| **GitHub Pages** | 有 GitHub 账号 | 新建仓库 → 上传全部文件 → Settings → Pages → 选 main 分支 |
| **国内静态托管** | 访客主要在国内 | 腾讯云 / 阿里云 / 七牛等的静态网站托管或对象存储（绑定已备案域名） |

上线后检查：首页 3D 能加载、每个气泡能点开、手机上打开一次、视频能播、分享到微信 / 社交平台时标题正常。

可选优化：
- 分享卡片图：截一张首页图存成 `og.jpg`（1200×630），在 `<head>` 里加 `<meta property="og:image" content="https://你的域名/og.jpg">`。
- 想更快：图片转 webp、视频压到 3–5MB；`vendor/three.min.js` 保留在本地（国内访客不用等 CDN）。

## AI 分身：从演示模式升级成真 AI

演示模式（默认）：按 `chat.data.qa` 里的关键词回答，不需要服务器，任何托管方式都能用。

真 AI（需要能跑函数的托管，模板附带的是 Vercel 版本）：
1. 把 `api/chat.js`、`vercel.json`、`knowledge/` 放进网站文件夹。
2. 在 `index.html` 的内容里把 chat 模块的 `data.endpoint` 改成 `"/api/chat"`。
3. 写知识库 `knowledge/*.md`：
   - 文件名以 `0` 开头的（`00-profile.md`、`01-experience.md`）每次对话都完整交给模型：放最核心的信息，尽量短。
   - 其他文件（文章、问答、项目细节）会被切段，按问题检索最相关的几段。
   - ⚠️ 这个文件夹会随网站公开，只写愿意公开的内容（见 privacy.md）。
4. Vercel 项目 → Settings → Environment Variables：
   - `LLM_API_KEY`（必填）：任何 OpenAI 兼容接口的密钥（DeepSeek、Kimi/Moonshot、通义千问、智谱、豆包方舟等都支持）
   - `LLM_BASE_URL`（可选，默认 `https://api.deepseek.com`）、`LLM_MODEL`（可选，默认 `deepseek-chat`）
   - `OWNER_NAME`（可选）：AI 分身怎么称呼你（用昵称）
   - `ALLOWED_ORIGINS`（可选）：额外允许调用的网址
5. 重新部署（`npx vercel --prod`）。打开网站 → 和我聊聊，状态显示“在线 · AI 实时回答”就成功了；接口不可用时会自动退回演示模式。

后端自带的保护：只允许本站调用、每人每分钟 12 条、最多 12 轮、每条 800 字、回答最多 420 token、拒绝角色扮演 / 写代码等与介绍主人无关的请求、资料里没有的不编造。密钥只在服务器上，不会出现在网页里。
