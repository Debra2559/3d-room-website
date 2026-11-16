# 模块库：每个模块能怎么呈现、要用户补充什么、数据怎么写

网站内容全部写在一个 `SITE` 对象里（JSON）。`SITE.modules` 是一个数组，**顺序 = 顶部导航顺序**。每个模块的通用字段：

| 字段 | 说明 |
|---|---|
| `id` | 唯一英文 id，导航和跳转用（如 `about`、`recipes`） |
| `type` | 模块类型，见下表（决定用哪个渲染器） |
| `label` / `en` | 中文名 / 英文小字（气泡和导航上显示） |
| `style` | 呈现形式（每种类型有 1–3 种） |
| `title` / `subtitle` / `lede` | 二级页面的大标题 / 英文副标题 / 一段引言 |
| `object` | 挂在场景里哪个物件上（槽位 key，见 scenes.md）；不写就自动分配；写 `false` 表示只在导航里出现 |
| `nav` | 写 `false` 不进顶部导航 |
| `data` | 这个模块的内容 |

> 自定义模块（用户想新增的“菜谱”“读书清单”“摄影”“播客”等）：用 `type: "custom"`，或者复用一个结构相近的类型（例如“菜谱”用 `articles`，“摄影”用 `works` 的 gallery），再改 `label`。

---

## 1. about · 关于我
- **呈现形式**：`profile`（默认：抠图照片 + 四周 4 张贴纸 + 小档案表 + 工具箱 + 手写标签） · `letter`（一封横线信纸自我介绍）
- **要用户补充**：昵称；一段 2–4 句的自我介绍；4 个“身份/个性贴纸”（大字 + 小字，例：`["PM","产品经理"]`）；小档案 3–5 行（方向 / 在做 / MBTI / 常驻城市等）；工具箱关键词；可选：透明背景抠图照片（没有就显示首字母圆章）
```json
{ "id":"about","type":"about","label":"关于","en":"about","style":"profile","title":"你好，我是小满","subtitle":"A curious maker.",
  "data":{ "photo":"media/me.webp","bio":"……","stickers":[["PM","产品经理"],["Maker","动手做东西"],["12","座城市走过"],["INFP","生活里的我"]],
    "profile":[["方向","AI 产品"],["在做","……"]],"toolbox":["Figma","Python"],"badges":["产品设计","常驻某一线城市"] } }
```
`letter` 额外可用：`data.greet`（开头称呼）、`data.more`（更多段落数组）。

## 2. journey · 经历
- **呈现形式**：`book`（默认：翻页书，左侧目录、左页公司+年份+小插画、右页要点+手写便签） · `timeline`（竖向时间线） · `cards`（拼贴卡片）
- **要用户补充**：每段经历的 机构名（可脱敏成“某AI公司”）、时间、角色/项目名、2–3 条“做了什么”、一行关键词；可选：项目复盘卡片（指向某篇文章）
- 插画 `pic` 可选：`chat` `web` `slides` `voice` `data` `code` `design` `school` `hardware` `team`（全是原创矢量，不含任何公司标志）
```json
{ "id":"journey","type":"journey","style":"book","data":{
  "items":[{ "org":"某AI\n创业公司","yr":"2024","title":"AI 生成网站 · 0-1","pic":"web","desc":"一句话概括","pts":["做了什么 1","做了什么 2"],"note":"关键词 · 关键词 · 关键词" }],
  "cases":[{ "t":"复盘标题","org":"某公司","tags":["评测"],"bg":"#AFC3E6","pic":"chat","article":0 }] } }
```
`org` 里的 `\n` 是书页大字的换行。`cases[].article` 是文章模块里的序号（从 0 开始）。

## 3. works · 作品集
- **呈现形式**：`bento`（默认：拼贴卡片，视频封面上有“▶ 播放 0:31”胶囊，图片点开看大图）
- 每件作品的 `kind`：`video` / `image` / `gallery`（多张图拼一排）/ `text`（只有文字）；`shape`：`feature`（整行主打，文字左媒体右）/ `wide`（整行）/ 不写（半行）；`vertical: true` 竖版视频装进“手机框”
- **要用户补充**：作品名、一句话描述、类型、2–3 个标签；视频（mp4/H.264，建议 ≤ 5MB）+ 封面图 + 时长；图片（webp/jpg，长边 ≤ 2000px，另备一张小图）；可选：链接
```json
{ "kind":"video","shape":"feature","vertical":true,"src":"media/demo.mp4","poster":"media/demo.jpg","dur":"0:31","type":"硬件 · AI","bg":"#E9DDF5","t":"作品名","d":"一句话","tags":["标签"],"note":"↗ 手写小字" }
{ "kind":"gallery","type":"设计物料","bg":"#FCE4EC","t":"……","d":"……","imgs":[["media/a-s.webp","media/a.webp","图注",0.63]] }
```
`imgs` 每项：[小图, 大图, 图注, 宽高比]。`dark: true` 用深色卡片。

## 4. products · 产品 / 项目
- **呈现形式**：`carousel`（默认：叠放大卡 + 右侧详情 + 底部缩略条，← → 键切换，有链接显示 LIVE、没有显示 WIP） · `grid`（卡片网格）
- **要用户补充**：产品名、类型、1–2 句描述、上线链接（没有就算“打磨中”）；可选卡片配色和图标 `ic`：`spark key compass plane chart flask pen film gem code heart camera book chat globe mail star cup music home`
```json
{ "t":"产品名","type":"效率工具","desc":"……","url":"https://…","bg":"#E2434F","fg":"#FFFDF9","ic":"cup" }
```

## 5. articles · 文章 / 笔记
- **呈现形式**：`list`（编号列表 + 阅读器）
- **要用户补充**：标题、摘要、日期、阅读时长、标签、正文（每段一项；支持 `## 小标题`、`**加粗**`、`1.` / `-` 列表）
```json
{ "title":"……","summary":"……","date":"2025-10","readTime":"5 分钟","tags":["产品"],"content":["第一段","## 小标题","- 列表 1\n- 列表 2"] }
```

## 6. hobbies · 爱好
- **呈现形式**：`bento`（彩色拼贴卡，每张卡一个可以玩的小互动）
- 每张卡的 `widget`：
  - `piano` 可弹的小钢琴（鼠标或键盘 A–K），自带巴赫《C 大调前奏曲》（公有领域）自动演奏
  - `gacha` 抽一张创作灵感（风格 × 氛围 × 主体），配一张随抽随画的小画；可自定义 `styles` `moods` `subjects`
  - `typewriter` 打字机轮流打出几行字（`lines`，或 `go` 到文章模块时自动用文章标题）
  - `radar` 好奇心雷达（`points: [[标题, 一句话], …]`）
  - `stamps` 城市邮戳（自动读足迹模块，或 `words`）
  - `hike` 小人沿山路登顶插旗
  - `none` 只有文字
- 其他字段：`t` 名称、`en` 英文小字、`d` 描述、`c` 卡片底色、`i` 图标、`wide: true` 整行、`dark: true` 深色、`go` 跳到某个模块
- **要用户补充**：有哪些爱好、每个一句话；每个爱好想要哪种小互动（不知道就按上面推荐：音乐→piano，画画/AI 创作→gacha，写作→typewriter，旅行→stamps，户外→hike，好奇/探索→radar）

## 7. travel · 足迹
- **呈现形式**：`map`（默认：深色足迹地图 + 明信片 + 旅途相册 + 城市索引邮戳） · `album`（相册 + 明信片）
- 地图按城市经纬度自动缩放，**不依赖任何国家边界数据**，全世界都能用；从 `home` 城市向其他城市画虚线航线
- **要用户补充**：去过的城市（AI 自己补经纬度，保留 2 位小数）；大本营城市（可不写或写到城市级）；可选：照片（长边 1200px）、一句话、一段回忆 `{title,date,story}`
```json
{ "home":"北京","cities":[{ "name":"大理","lat":25.59,"lng":100.23,"photo":"media/dali.jpg","note":"一句话","memory":{"title":"回忆标题","date":"某年 · 春","story":"……"} }] }
```

## 8. contact · 联系
- **呈现形式**：`letter`（默认：自动打字的信纸 + 邮箱条“复制邮箱” + 社交卡片） · `cards`（只有邮箱 + 社交卡片）
- **要用户补充**：一段问候语；对外邮箱（建议单独开一个，不用含真名拼音的）；社交账号（平台、账号名、一句话、链接；链接还没给就 `u` 留空，只显示账号名；还没开通的加 `"soon": true` 显示“即将开通”）
```json
{ "greeting":"你好！\n……","email":"hello@example.com","social":[{ "t":"GitHub","h":"@id","d":"一句话","u":"https://…","bg":"#2B3563","fg":"#fff","icon":"GH" }] }
```

## 9. chat · AI 分身（和我聊聊）
- **呈现形式**：右下角“和我聊聊”按钮 + 聊天窗口。默认**演示模式**：按 `qa` 关键词问答，不需要任何服务器；配置 `endpoint` 后接真大模型（见 deploy.md）
- **要用户补充**：开场白；4 个推荐问题；6–12 组常见问答（关键词 → 回答 → 可选跳转模块）；兜底回答
```json
{ "id":"chat","type":"chat","label":"和我聊聊","object":false,"data":{ "endpoint":"","hello":"……","suggestions":["你是谁？"],
  "qa":[{ "k":["你是谁","介绍"],"a":"……","go":"about" }],"fallback":"这个问题网站上还没写，欢迎发邮件问我本人～" } }
```

## 10. custom · 自定义模块
- 用来装任何新模块：读书清单、菜谱、摄影、播客、课程、志愿者经历……
```json
{ "id":"books","type":"custom","label":"书单","en":"reading","title":"最近在读","data":{ "blocks":[
  { "h":"小标题","p":["一段文字"],"cards":[{ "t":"书名","d":"一句话","c":"#EEF8C9","i":"book","url":"" }],"img":"media/x.webp" } ] } }
```

---

## 全站字段

```json
{
  "name":"小满", "brand":"XM·STUDIO", "brandTag":"studio", "scene":"kitchen", "base":"cloud",
  "room":{ … 可选，自定义场景 / 在内置场景上加减物件，见 scenes.md … },
  "theme":{ "accent":"#E2434F","ink":"#1C2342","lime":"#D6F04F","sky":"#CBD7EA","paper":"#FFFDF9" },
  "hero":{ "hi":"hi，我是小满，欢迎来我的厨房 ↘","title":"把想法，<mark>做成</mark>真的东西。","sub":"一两句介绍","primary":{"text":"看看我的作品 →","go":"works"},"secondary":{"text":"先认识我","go":"about"} },
  "avatar":{ "skin":"#F6DDD2","hair":"#2A2238","top":"#F9C6CC","bottom":"#2B3563","style":"pants|skirt","accessory":"glasses|flower|cap|bow|none","lines":["欢迎光临～","点点桌上的东西试试！"] },
  "modules":[ … ]
}
```
- `brandTag`：logo 后面的手写小字，默认 `studio`（画室可以写 `atelier`，写空字符串就不显示）。
- `scene`：`studio` `kitchen` `bar` `cabinet` `cafe`，或 `custom`（配合 `room` 自己搭）。写了不存在的场景名会退回工作台并提示。
- `base`：房间下面的底座，`island`（默认）`grass` `cloud` `water` `rock` `pedestal` `none`，见 scenes.md。
- **照片**：没有照片时，单张图（作品 `src`、视频 `poster`、关于我 `photo`）留空即可；图集写占位文件名（如 `media/作品1-1.jpg`）。在模板预览、导入预览或成品网页地址加 `?edit` 时，这些位置会变成“📷 点这里放照片”的格子，点一下选电脑里的照片，自动压缩后存进内容，「下载成品网页」时一起带上（浏览器能存的总量约 5MB，照片很多时请改用 `media/` 文件夹）。普通访客打开时，缺的图片显示“图片待补充”，不会出现破图。
- `hero.title` 里只允许 `<mark>…</mark>`（荧光笔高亮）和 `<br>`，其他标签会被当成文字。
- 颜色建议：`accent` 一个鲜明的主色，`ink` 深色文字，`lime` 荧光高亮色；整体保持“米白纸张 + 一个主色 + 一个荧光色”。
