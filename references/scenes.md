# 场景库：房间长什么样、每个物件挂哪个模块

整个网站首页是一个“等距视角的小房间”（两面墙 + 地板 + 一个 Q 版小人），房间放在一个底座上（见下方「底座」）。房间里的每一件可点的物件叫一个**槽位（slot）**，一个槽位挂一个模块：鼠标悬停物件会抬起来、上方的气泡变成主色并展开英文；点击后镜头飞到物件前，再弹出这个模块的二级页面。

模板内置 5 个场景（`SITE.scene`），在浏览器地址后面加 `?scene=kitchen` 就能直接预览别的场景。

| scene | 名字 | 气质 | 默认白天/夜晚 |
|---|---|---|---|
| `studio` | 工作台 / 书房 | 米色木地板、淡紫墙、窗户、串灯 | 白天 |
| `kitchen` | 厨房 | 薄荷格子地砖、鼠尾草绿橱柜、白瓷砖、吊灯 | 白天 |
| `bar` | 酒吧 | 深紫墙、深色木地板、霓虹灯牌（显示 brand）、串灯 | 夜晚 |
| `cabinet` | 陈列柜 / 橱柜 | 一整面 3×3 的木质陈列柜，每格放一件小物 | 白天 |
| `cafe` | 咖啡馆 | 奶油色墙 + 绿色墙裙、窗边座位、黑板菜单、红色邮筒 | 白天 |

## 底座（`SITE.base`）

房间下面放什么，和房间是分开选的，任何房间都能配任何底座。地址后加 `?base=cloud` 可以直接预览。

| base | 名字 | 感觉 |
|---|---|---|
| `island` | 🏝️ 圆形小岛（默认） | 温暖、经典 |
| `grass` | 🌱 草地方块 | 像一块漂浮的泥土，边上有小草和小花 |
| `cloud` | ☁️ 云朵 | 梦幻，旁边飘着几朵小云 |
| `water` | 🌊 水上小岛 | 周围一圈水，有水波和荷叶 |
| `rock` | 🪨 悬浮岩石 | 带水晶，旁边有漂浮的小石头，适合科技 / 游戏感 |
| `pedestal` | 🎂 白色展台 | 像手办展示台，简洁，中间一圈是主色 |
| `none` | ⬜ 无底座 | 只有一圈柔和的影子，最干净 |

## 槽位 → 推荐模块（隐喻）

自动分配规则：先看模块的 `object` 有没有指定槽位；没有就找“推荐模块里包含这个类型”的第一个空槽位；还没有就随便找一个空槽位；槽位用完的模块只出现在顶部导航里。

### studio 工作台
| 槽位 key | 物件 | 推荐模块 | 隐喻 |
|---|---|---|---|
| `cork` | 墙上的软木板（拍立得 + 便利贴） | about | 关于我的一切都钉在这里 |
| `books` | 桌上一排书 | journey / articles | 翻翻我的经历 |
| `laptop` | 笔记本电脑 | works / products | 我做的东西 |
| `notebook` | 桌上的本子和笔 | articles | 写下来的东西 |
| `phone` | 手机 + 马克杯 | contact / chat | 联系我 |
| `piano` | 立式钢琴 + 琴凳 | hobbies | 下班以后 |
| `map` | 左墙的足迹地图板 | travel | 去过的地方 |
| `cabinet` | 角落展示柜 | products / works | 摆出来的成果 |

### kitchen 厨房
| 槽位 | 物件 | 推荐模块 | 隐喻 |
|---|---|---|---|
| `fridge` | 贴满冰箱贴和照片的冰箱 | about | 冰箱上贴着“我” |
| `chalkboard` | 左墙 Recipe 黑板 | journey | 我的成长“菜谱” |
| `pot` | 灶台上咕嘟冒气的锅 | works | 正在炖的作品 |
| `oven` | 发光的烤箱 | products | 刚出炉的产品 |
| `cookbooks` | 左墙食谱书架 | articles | 我写的“食谱” |
| `spices` | 调料架 | hobbies | 生活的调味料 |
| `table` | 餐桌（果盘 + 明信片） | travel | 各地的味道 |
| `phone` | 墙上的红色电话 | contact / chat | 打个电话给我 |

### bar 酒吧
| 槽位 | 物件 | 推荐模块 | 隐喻 |
|---|---|---|---|
| `neon` | 霓虹灯牌（写着 brand） | about | 招牌就是我 |
| `menu` | 黑板酒单 | journey | 我的“酒单” |
| `bottles` | 酒架上的一排酒 | works | 珍藏的作品 |
| `cocktails` | 吧台上的特调 | products | 本店特调 |
| `table` | 小圆桌（书 + 蜡烛） | articles | 坐下来读一篇 |
| `jukebox` | 点唱机 | hobbies | 点一首我爱的 |
| `poster` | 旅行海报 | travel | 下一站 |
| `phone` | 吧台上的转盘电话 | contact / chat | 订位请致电 |

### cabinet 陈列柜（3 × 3 格）
| 位置 | 槽位 | 物件 | 推荐模块 |
|---|---|---|---|
| 上左 | `frame` | 相框 | about |
| 上中 | `globe` | 地球仪（会转） | travel |
| 上右 | `letters` | 信封和蜡封 | contact |
| 中左 | `books` | 一排书 | journey |
| 中中 | `camera` | 胶片相机 | works |
| 中右 | `notebook` | 笔记本 | articles |
| 下左 | `record` | 唱片机（会转） | hobbies |
| 下中 | `gifts` | 礼物盒 | products |
| 下右 | `plant` | 盆栽 | custom（空位，给新增模块用） |

### cafe 咖啡馆
| 槽位 | 物件 | 推荐模块 | 隐喻 |
|---|---|---|---|
| `sign` | 门口的 A 字黑板（写着 hello I'm 昵称） | about | 打个招呼 |
| `menu` | 墙上的 MENU 黑板 | journey | 我的菜单 |
| `espresso` | 咖啡机（冒热气） | works | 现做的作品 |
| `pastry` | 蛋糕玻璃柜 | products | 招牌甜点 |
| `bookcase` | 书架 | articles | 店里的书 |
| `record` | 唱片机 | hobbies | 店里在放的歌 |
| `window` | 窗边座位 + 明信片 | travel | 窗外的远方 |
| `postbox` | 红色邮筒 | contact / chat | 给我写信 |

## 根据描述搭房间（推荐，所有 AI 都能做）

用户用自己的话描述一个地方（“深夜的拉面小店”“海边冲浪小屋”“露营地”“堆满植物的卧室”……），你按下面 4 步把它变成 `"scene": "custom"` + `room`，**只写 JSON，不改代码**：

1. **定大框架**（`room.colors`）
   - 室内还是户外：室内两面墙（默认）；半开放（海边小屋、门店）只留后墙 `"walls": "back"`；户外（露营、花园、天台）不要墙 `"walls": false`。
   - 地面：木地板（默认）、格子砖 `"floorStyle": "tiles"`、纯色 `"floorStyle": "plain"`（草地、沙滩、水泥地都用它，配合 `floor` `floor2` 颜色）。
   - 白天 / 夜晚：有灯、霓虹、篝火、“深夜”等字眼就 `"night": true`；夜晚可以加串灯 `"lights": true`。
   - 窗户：左墙默认有一扇，不要就 `"window": false`；`windowZ` 可以挪位置。地毯：`rug` `rug2` 改颜色，不要地毯就 `"rug": false`。
   - 底座：能推断就直接定（海边 → `water`，户外草地 → `grass`，梦幻 / 卧室 → `cloud`，店铺 / 展示 → `pedestal`，科技 / 游戏 → `rock`），写在顶层 `base`。
2. **挑 6–9 件“能点”的东西**，每件对应一个板块，挑最能代表这个地方、又和板块有好懂关系的：招牌 / 门口小黑板 → 关于我；菜单 / 书架 / 速写本 → 经历；吧台上的锅、画架、冲浪板、电脑 → 作品；冰箱、礼物盒、货架 → 产品；书、桌上的本子 → 文章；唱片机、钢琴、篝火、调料架 → 爱好；地球仪、旅行海报、窗外 → 去过的地方；电话、邮筒、信封、长椅 → 联系。
3. **再加 3–6 件装饰**（没有 `key`）：凳子、植物、吊灯、地毯、树……让场景“像那个地方”。
4. **摆位置**：可点的东西分散在三块区域——后墙（`wall: "back"` 的挂件，或贴后墙放的家具 z≈-4.6 到 -5.3）、左墙（`wall: "left"`）、地面（x、z 在 -5 到 5）。小人站在 (1.8, 0, 1.3)，周围 1.5 内别放东西；可点的东西之间隔开 1.5 以上，气泡才不会挤。没有墙时，挂件（画框、黑板、霓虹字）会自动变成立在地上的立牌。

物件库里没有的东西，用最像的代替并在方案里说一声（招财猫 → 金色的小礼物盒；书法挂轴 → `frame` 的 `text`；吧台 → `counter`）。

### 四个例子（都实际搭过）

**深夜拉面店**（`"base": "pedestal"`）：
```json
{ "name": "深夜拉面店", "colors": {"wall": "#4A2F2A", "wall2": "#7A3B2E", "trim": "#C9A06A", "floor": "#3A3330", "floor2": "#2E2826", "floorStyle": "tiles", "rug": "#E2434F", "rug2": "#3A3330", "window": false, "lights": true, "night": true},
  "props": [
    {"key": "sign", "kind": "neon", "for": ["about"], "wall": "back", "x": 2.6, "y": 6.0, "text": "拉面", "color": "#FF5FA2", "w": 2.6, "h": 1.1},
    {"key": "menu", "kind": "board", "for": ["journey"], "wall": "left", "z": -2.5, "y": 4.8, "w": 2.2, "h": 2.6, "style": "chalk", "text": "MENU"},
    {"key": "counter", "kind": "counter", "for": ["works"], "x": -1.4, "z": -4.6, "w": 6.0, "color": "#8C5A3C", "color2": "#E9D9B8", "items": ["pot", "mug", "mug"]},
    {"kind": "stool", "x": -3.4, "z": -2.9, "color": "#E2434F"},
    {"kind": "stool", "x": -1.4, "z": -2.9, "color": "#E2434F"},
    {"kind": "stool", "x": 0.6, "z": -2.9, "color": "#E2434F"},
    {"key": "jars", "kind": "wallshelf", "for": ["hobbies"], "wall": "back", "x": -1.6, "y": 4.4, "w": 3.6, "items": ["jar", "plant", "jar", "books"]},
    {"key": "fridge", "kind": "fridge", "for": ["products"], "x": 4.6, "z": -4.8},
    {"kind": "pendant", "x": -2.6, "z": -4.4},
    {"kind": "pendant", "x": 0.0, "z": -4.4},
    {"key": "table", "kind": "table", "for": ["articles"], "x": -3.0, "z": 2.2, "items": ["mug", "letter"]},
    {"key": "poster", "kind": "frame", "for": ["travel"], "wall": "left", "z": 2.4, "y": 4.6, "art": "landscape", "w": 1.8, "h": 2.2},
    {"key": "phone", "kind": "wallphone", "for": ["contact"], "wall": "left", "z": -5.0, "y": 3.4},
    {"kind": "plant", "x": 5.2, "z": 0.6}
  ] }
```

**海边冲浪小屋**（`"base": "water"`，只留后墙）：
```json
{ "name": "海边冲浪小屋", "colors": {"walls": "back", "wall": "#E8F4F8", "wall2": "#7EC8E3", "floor": "#F1E1C2", "floor2": "#E6D2AE", "floorStyle": "plain", "rug": "#F5A623", "rug2": "#FFFDF9", "lights": true},
  "props": [
    {"key": "board1", "kind": "surfboard", "for": ["works"], "x": -3.6, "z": -5.2, "color": "#E2434F"},
    {"kind": "surfboard", "x": -2.6, "z": -5.3, "color": "#7EC8E3"},
    {"key": "window", "kind": "window", "for": ["about"], "wall": "back", "x": 1.4, "y": 4.8, "w": 3.0, "h": 2.2},
    {"key": "shelf", "kind": "wallshelf", "for": ["hobbies"], "wall": "back", "x": -2.8, "y": 5.6, "w": 3.0, "items": ["plant", "camera", "jar"]},
    {"key": "umbrella", "kind": "umbrella", "for": ["travel"], "x": -3.4, "z": 2.2, "color": "#F5A623"},
    {"key": "bench", "kind": "bench", "for": ["contact"], "x": 4.2, "z": -4.6, "color": "#7EC8E3"},
    {"key": "board", "kind": "board", "for": ["journey"], "wall": "back", "x": 4.6, "y": 5.2, "w": 1.8, "h": 1.6, "style": "cork", "text": "LOG"},
    {"key": "crate", "kind": "crate", "for": ["products"], "x": 0.4, "z": -4.6, "items": ["fruit"]},
    {"key": "table", "kind": "table", "for": ["articles"], "x": 4.4, "z": 2.0, "items": ["candle", "books"]},
    {"kind": "plant", "x": 5.3, "z": -1.6, "size": 1.6}
  ] }
```

**露营地**（`"base": "grass"`，没有墙，夜晚有篝火）：
```json
{ "name": "露营地", "colors": {"walls": false, "floor": "#A9D18E", "floor2": "#97C276", "floorStyle": "plain", "rug": "#F5A623", "rug2": "#FFFDF9", "night": true},
  "props": [
    {"key": "tent", "kind": "tent", "for": ["about"], "x": -2.6, "z": -3.6, "color": "#F5A623"},
    {"key": "fire", "kind": "campfire", "for": ["hobbies"], "x": 0.2, "z": -0.6},
    {"key": "tree1", "kind": "tree", "for": ["journey"], "x": 3.8, "z": -4.4, "size": 1.1},
    {"kind": "tree", "x": -5, "z": 0.8},
    {"kind": "tree", "x": 5.0, "z": 3.6, "size": 0.8},
    {"key": "bench", "kind": "bench", "for": ["contact"], "x": -2.4, "z": 1.6, "rot": 0.6},
    {"key": "sign", "kind": "board", "for": ["works"], "wall": "back", "x": 0.8, "y": 3.4, "w": 2.4, "h": 1.6, "style": "paper", "text": "WORKS"},
    {"key": "flowers", "kind": "flowerbed", "for": ["travel"], "x": 4.4, "z": 0.0, "rot": -1.57},
    {"key": "crate", "kind": "crate", "for": ["products"], "x": -4.6, "z": -1.6, "items": ["camera"]},
    {"key": "lamp", "kind": "lamp", "for": ["articles"], "x": -4.8, "z": -4.8}
  ] }
```

**卧室**（`"base": "cloud"`）：
```json
{ "name": "卧室", "colors": {"wall": "#F7EEF2", "wall2": "#E9D6E4", "floor": "#E8D6BF", "floor2": "#DCC6AA", "rug": "#AFC3E6", "rug2": "#FFFDF9", "windowZ": 2.6},
  "props": [
    {"key": "bed", "kind": "bed", "for": ["about"], "x": -3.6, "z": -3.6, "color": "#F9C6CC"},
    {"key": "desk", "kind": "desk", "for": ["works"], "wall": "back", "x": 2.6, "w": 3.6, "items": ["laptop", "mug"]},
    {"kind": "chair", "x": 2.6, "z": -3.4, "rot": 3.14},
    {"key": "shelf", "kind": "bookshelf", "for": ["journey"], "wall": "left", "z": 0.4, "w": 2.4, "h": 3.6},
    {"key": "frame", "kind": "frame", "for": ["travel"], "wall": "back", "x": -0.4, "y": 5.2, "art": "landscape", "w": 2.0, "h": 1.5},
    {"key": "tv", "kind": "tv", "for": ["hobbies"], "x": 4.6, "z": -0.6, "rot": -1.57},
    {"key": "aquarium", "kind": "aquarium", "for": ["products"], "x": 4.4, "z": 3.6, "rot": -1.57},
    {"key": "clock", "kind": "clock", "for": ["contact"], "wall": "back", "x": 5.0, "y": 5.6},
    {"key": "lamp", "kind": "lamp", "for": ["articles"], "x": -5.3, "z": -1.6},
    {"kind": "plant", "x": 0.2, "z": -5.3}
  ] }
```
板块要挂在指定的东西上，在板块里写 `"object": "这个key"`（例如 `{"id":"about", …, "object":"tent"}`）；不写的话按 `for` 自动匹配。

### 在现成房间上加减

描述和现成房间很接近时（“有钢琴的书房”“带吧台的咖啡馆”），保留 `"scene": "studio"` 等，用 `room.hide` 去掉不要的东西（按 key，见上面各房间的表），用 `room.props` 加新的，用 `room.colors` 改颜色。

### 物件种类 `kind`

| 贴墙的（`wall`: "back" + `x`，或 `wall`: "left" + `z`；`y` 是高度 2–7） | 说明 |
|---|---|
| `frame` 画框 | `w` `h`；`art`: portrait 自画像 / landscape 风景 / abstract 抽象 / text 文字（配 `text`） |
| `board` 板子 | `style`: chalk 黑板 / cork 软木板 / paper 白板；`text` 标题 |
| `neon` 霓虹字 | `text`（默认网站名）、`color` |
| `window` 窗户 | `w` `h`；`color` `color2` 是天空颜色 |
| `wallshelf` 墙上搁板 | `w`、`items` |
| `wallphone` 墙上电话 · `clock` 挂钟 | |

| 放地上的（`x` `z` `rot`；写 `wall` 会自动靠墙） | |
|---|---|
| 家具 | `desk` 长桌（`w` `items`）· `table` 小圆桌（`items`）· `counter` 柜台 / 吧台（`w` `items`）· `bookshelf` 书架（`w` `h`）· `bed` 床 · `sofa` 单人沙发 · `chair` 椅子 · `stool` 高脚凳 · `bench` 长椅 · `crate` 木箱（`items`）· `rug` 地毯（`w`） |
| 电器 / 娱乐 | `tv` 电视柜 · `fridge` 冰箱 · `stove` 灶台 · `fireplace` 壁炉（会亮）· `arcade` 街机 · `aquarium` 鱼缸 · `record` 唱片机 · `piano` 钢琴 · `guitar` 吉他 · `speaker` 音箱 · `mic` 麦克风 |
| 小物 | `easel` 画架 · `cart` 颜料推车 · `globe` 地球仪 · `camera` 相机 · `gift` 礼物盒 · `stack` 一摞本子 · `postbox` 邮筒 · `plant` 盆栽（`size`）· `lamp` 落地灯 · `pendant` 吊灯（从天花板垂下） |
| 户外 | `tree` 树（`size`）· `tent` 帐篷 · `campfire` 篝火（会亮）· `umbrella` 遮阳伞（带躺椅）· `surfboard` 冲浪板 · `flowerbed` 花坛（`w`） |

桌面 / 搁板上的小东西 `items`：`mug` 杯子 · `laptop` 电脑 · `books` 书 · `sketchbooks` 速写本 · `jar` 笔筒 · `plant` 小盆栽 · `letter` 信 · `candle` 蜡烛 · `fruit` 水果 · `pot` 锅 · `cake` 蛋糕 · `camera` 相机 · `globe` 地球仪 · `record` 唱片机。
所有物件都可以加 `color` `color2`（主色 / 副色）和 `size`（整体缩放）。

**进阶（能改代码时）**：想要列表里没有的物件，可以在模板的 `SCENES` 对象里复制一个场景，改名（如 `atelier`），只改两处：
   - `P`：配色（`floor` `floor2` `wall` `wall2` `trim` `island` `island2` `rug` `rug2`）、`floorTiles`（格子地砖）、`window`（左墙窗户，`false` 关掉）、`lights`（串灯）、`night`（默认夜晚）
   - `build(K, S, slot)`：用积木搭物件，每个可点物件调用 `slot("key", 物件, ["推荐模块类型"])`
3. 积木工具 `K`：`K.box / K.rbox(圆角盒) / K.cyl / K.sph / K.cone / K.tor / K.plane / K.board(墙上的板子，用 canvas 画内容) / K.books / K.plant / K.bottle / K.mug / K.stool / K.chair / K.table / K.lamp / K.neon(霓虹字)`，位置用 `K.at(物件, x, y, z)`，组合用 `K.grp(...)`。
4. 坐标约定：房间地板是 x、z ∈ [-6, 6]，后墙在 z = -6，左墙在 x = -6，墙高 8；小人站在 (1.8, 0, 1.3)，不要在它周围 1.5 以内放家具；挂墙上的东西贴着墙面放（后墙 z≈-5.92，左墙 x≈-5.92，左墙上的板子 `K.board(..., "x")`）。
5. 物件尽量 6–9 个、分散在后墙、左墙和地面三块区域，避免气泡挤在一起；每个可点物件要“一眼能认出来”，且和模块有个好玩的隐喻。
6. 改完用 `?scene=新名字` 预览，确认：物件不穿模、气泡不重叠、小人不被挡住。

**两种做法都要遵守的摆放规则**：房间地板 x、z ∈ [-6, 6]，后墙 z = -6，左墙 x = -6，墙高 8；小人站在 (1.8, 0, 1.3)，周围 1.5 以内别放东西（也可以用 `room.avatarAt: [x, 0, z]` 换位置）；可点物件 6–9 个，分散在后墙、左墙和地面，彼此隔开 1.5 以上，气泡才不会挤在一起；窗户默认在左墙 z = -1.6，左墙上的东西要避开它。

## 小人（avatar）
不需要真人照片，全部由配置生成：`skin` 肤色、`hair` 发色、`top` 上衣、`bottom` 下装、`style`（`skirt` 裙子 / `pants` 裤子）、`accessory`（`flower` 花环 / `cap` 帽子 / `glasses` 眼镜 / `bow` 蝴蝶结 / `none`）、`lines`（点小人时随机说的话，第一句是开场白）。小人会眨眼、轻轻晃，镜头飞向某个物件时会转身看过去。
