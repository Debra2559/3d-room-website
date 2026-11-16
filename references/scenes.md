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

## 用户想要的场景不在列表里？（画室、录音棚、图书馆、宿舍、车库……）

**推荐做法：只写 JSON，不改代码**（所有 AI 都能做，包括只能聊天的）。设 `"scene": "custom"`，再写一个 `room` 对象：

```json
"scene": "custom",
"room": {
  "name": "画室", "loading": "正在挤颜料、支画架…",
  "colors": { "floor":"#EADFCF","floor2":"#DDD0BC","wall":"#F6F3EE","wall2":"#DCE6F5","rug":"#3D6FE0","rug2":"#FFFDF9","windowZ":-2.2 },
  "props": [
    { "key":"portrait","kind":"frame","for":["about"],"wall":"back","x":-2.6,"y":5.4,"w":2.2,"h":2.7,"art":"portrait" },
    { "key":"easel","kind":"easel","for":["works"],"x":-2.0,"z":-2.2,"rot":0.55 },
    { "key":"sketchbooks","kind":"desk","for":["journey"],"x":2.6,"z":-4.95,"w":4.4,"items":["sketchbooks","jar"] },
    { "key":"bookshelf","kind":"bookshelf","for":["custom"],"wall":"left","z":2.6 },
    { "key":"paints","kind":"cart","for":["hobbies"],"x":4.6,"z":-2.0 },
    { "key":"letters","kind":"table","for":["contact"],"x":-2.4,"z":2.6,"w":1.4,"items":["letter","mug"] },
    { "kind":"chair","x":-3.6,"z":2.6,"rot":1.57,"color":"#FFD84D" },
    { "kind":"plant","x":5.2,"z":1.6 }
  ]
}
```
- **有 `key` 的物件可以点**，模块用 `"object": "key"` 指定挂在它上面（或者按 `for` 自动匹配）；没有 `key` 的只是装饰。
- `room.base` 也可以写底座（和顶层 `base` 一样）。`colors` 可用：`floor` `floor2` `wall` `wall2`（墙裙）`trim` `rug` `rug2` `floorTiles`（true = 格子地砖）`window`（false = 不要窗）`windowZ` `windowY` `lights`（串灯）`night`（默认夜晚）。
- 也可以在内置场景上加减：`"scene": "kitchen"` + `room.hide: ["spices"]`（按槽位 key 去掉物件）+ `room.props: [...]`（加新物件，比如给新增的“书单”模块加一个书架）。

**物件种类 `kind`**（括号里是常用参数）：

| 贴墙的（用 `wall`:"back"/"left" + `x` 或 `z` + `y` 高度） | 放地上的（用 `x` `z` `rot`；写 `wall` 会自动靠墙） |
|---|---|
| `frame` 画框（`w` `h` `art`: portrait 自画像 / landscape 风景 / abstract 抽象 / text 文字，`text`） | `easel` 画架 · `desk` 长桌（`w` `items`）· `table` 小圆桌（`w` `items`）· `counter` 柜台（`w` `items`） |
| `board` 板子（`style`: chalk 黑板 / cork 软木 / paper 白板，`text` 标题） | `bookshelf` 书架（`w` `h`）· `crate` 木箱（`items`）· `cart` 颜料推车 · `record` 唱片机柜 |
| `neon` 霓虹字（`text`，默认品牌名）· `wallshelf` 墙上搁板（`items`） | `piano` 钢琴 · `guitar` 吉他 · `speaker` 音箱 · `mic` 麦克风 · `globe` 地球仪 · `camera` 相机 · `gift` 礼物盒 |
| `wallphone` 墙上电话 · `clock` 挂钟 | `sofa` 单人沙发 · `chair` 椅子 · `stool` 高脚凳 · `postbox` 邮筒 · `plant` 盆栽 · `lamp` 落地灯（夜晚会亮）· `stack` 一摞本子 |

桌面 / 搁板上的小东西 `items`：`mug` `laptop` `books` `sketchbooks` `jar`（笔筒）`plant` `letter` `candle` `fruit` `pot`（锅）`cake` `camera` `globe` `record`。
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
