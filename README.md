# 沙特项目产品展示网站 - 小白部署指南

## 📁 你拿到的文件

```
saudi-products-site/
├── index.html          ← 首页（产品列表）
├── condenser.html      ← 同步调相机详情页
├── aidc.html           ← 智算中心详情页
├── gis.html            ← 380kV GIS详情页
├── transformer.html    ← 三绕组变压器详情页
├── generate_qrcode.py  ← 二维码生成脚本
├── qrcode.png          ← 二维码图片（需要重新生成）
└── images/             ← 放图片的文件夹（你需要准备4张图）
```

---

## 🚀 方法一：免费部署到 GitHub Pages（推荐，扫码就能访问）

### 第1步：注册 GitHub 账号（5分钟）

1. 打开 https://github.com
2. 点右上角 **Sign up**
3. 填邮箱、密码、用户名（**记好你的用户名，比如 xiaoming123**）
4. 邮箱收到验证码后填进去，完成注册

### 第2步：创建仓库（2分钟）

1. 登录后，点右上角 **+** → **New repository**
2. Repository name 填：`saudi-products`
3. 选 **Public**（公开）
4. **不要勾选** "Add a README file"
5. 点绿色按钮 **Create repository**

### 第3步：上传文件（3分钟）

创建完仓库后会跳到一个页面，按下面操作：

1. 点页面中间的 **uploading an existing file**（蓝色链接）
2. 把 `saudi-products-site` 文件夹里的 **5个HTML文件** 全选拖进去
3. 在下方 "Commit message" 随便写点什么，比如 "上传网站"
4. 点绿色按钮 **Commit changes**

### 第4步：上传图片（1分钟）

1. 回到仓库首页，点 **Add file** → **Upload files**
2. 把准备好的4张图片拖进去：
   - `condenser.jpg`（同步调相机）
   - `aidc.jpg`（智算中心）
   - `gis.jpg`（GIS设备）
   - `transformer.jpg`（变压器）
3. 确保图片是放在 `images/` 文件夹里：
   - 在拖文件之前，先在页面上的路径框里输入 `images/`
   - 或者上传后在每个文件名前加上 `images/`
4. 点 **Commit changes**

### 第5步：开启 GitHub Pages（2分钟）

1. 在仓库首页，点顶部 **Settings** 标签
2. 左边菜单点 **Pages**（在 "Code and automation" 下面）
3. "Branch" 下拉选 **main**，旁边选 **/ (root)**，点 **Save**
4. 等1-2分钟，页面刷新后会显示：
   > Your site is live at `https://你的用户名.github.io/saudi-products/`

### 第6步：生成二维码

拿到网址后，打开命令行（Win+R 输入 `cmd`），输入：

```bash
cd E:\saudi-products-site
python generate_qrcode.py "https://你的用户名.github.io/saudi-products/"
```

二维码会生成在 `qrcode.png`，发给别人扫码即可！

---

## 🏠 方法二：本地直接打开（最简单，但只有你自己能看）

1. 打开 `E:\saudi-products-site` 文件夹
2. 双击 `index.html`
3. 浏览器里就能看到网站了

---

## 🖼 图片准备

你需要准备 4 张 JPG 图片，放到 `images/` 文件夹里：

| 文件名 | 对应产品 |
|--------|----------|
| `condenser.jpg` | 同步调相机 |
| `aidc.jpg` | 智算中心 |
| `gis.jpg` | 380kV GIS |
| `transformer.jpg` | 三绕组变压器 |

如果没有图片，网站会自动显示占位图标，不影响功能。

---

## 🔄 修改网址后重新生成二维码

```bash
cd E:\saudi-products-site
python generate_qrcode.py "新的网址"
```

---

## ❓ 常见问题

**Q: 二维码扫不出来？**
A: 确保网址是 `https://` 开头的，而且网站已经部署成功（浏览器能打开）。

**Q: 网页显示乱码？**
A: 右键网页 → 编码 → 选 UTF-8。

**Q: 语言切换不生效？**
A: 右上角下拉框选择语言即可，选择会自动记住。支持中文/English/العربية。

**Q: 咨询表单提交后去哪了？**
A: 目前只是前端演示，提交后会弹窗提示成功。如果需要真正接收咨询，需要对接后端服务。
