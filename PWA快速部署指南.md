# 📱 佛历万年历 PWA 快速部署指南

## 第一步：生成应用图标

1. **打开图标生成器**
   - 双击打开 `图标生成器.html`

2. **选择样式**
   - 选择您喜欢的图标样式（默认/日历/莲花/简约）
   - 选择背景颜色和文字颜色
   - 预览效果满意后下载

3. **下载图标**
   - 点击"下载 192x192"按钮，保存为 `icon-192.png`
   - 点击"下载 512x512"按钮，保存为 `icon-512.png`

4. **放置图标**
   - 将两个图标文件放到与HTML文件相同的目录

---

## 第二步：验证文件完整性

确保您的目录包含以下文件：

```
佛历工具/
├── 离线佛历万年历工具.html  ✅
├── lunar.js                   ✅
├── manifest.json              ✅
├── service-worker.js          ✅
├── icon-192.png              ⬜ 需要生成
├── icon-512.png              ⬜ 需要生成
├── 图标生成器.html            ✅ 工具
└── PWA快速部署指南.md         ✅ 本文件
```

---

## 第三步：本地测试

### 方法A：直接在手机浏览器测试（推荐）

1. **将所有文件发送到手机**
   - 通过微信、QQ、数据线等方式
   - 放到手机的Download文件夹

2. **安卓手机**
   - 用Chrome浏览器打开HTML文件
   - 点击浏览器菜单（右上角三个点）
   - 选择"添加到主屏幕"或"安装应用"
   - 确认安装

3. **iPhone**
   - 用Safari浏览器打开HTML文件
   - 点击底部分享按钮
   - 向下滚动，找到"添加到主屏幕"
   - 点击右上角"添加"

### 方法B：使用本地服务器（需要Node.js）

1. **安装http-server**
   ```bash
   npm install -g http-server
   ```

2. **启动服务器**
   ```bash
   cd "D:\devcode\01_devcode\佛历工具"
   http-server -p 8080
   ```

3. **手机访问**
   - 确保手机和电脑在同一WiFi
   - 手机浏览器访问：`http://电脑IP:8080/离线佛历万年历工具.html`
   - 安装到主屏幕

### 方法C：使用VS Code Live Server

1. **安装VS Code扩展**
   - 安装 "Live Server" 扩展

2. **启动**
   - 右键HTML文件 → "Open with Live Server"

3. **手机访问**
   - 查看电脑IP地址（cmd输入ipconfig）
   - 手机访问：`http://电脑IP:5500/离线佛历万年历工具.html`

---

## 第四步：在线部署（推荐，永久使用）

### 方案1：GitHub Pages（免费，推荐）

1. **创建GitHub账号**
   - 访问 https://github.com/
   - 注册并登录

2. **创建新仓库**
   - 点击右上角 "+" → "New repository"
   - 仓库名：`buddhist-calendar`
   - 选择"Public"
   - 点击"Create repository"

3. **上传文件**
   - 点击"uploading an existing file"
   - 拖拽以下文件：
     - 离线佛历万年历工具.html
     - lunar.js
     - manifest.json
     - service-worker.js
     - icon-192.png
     - icon-512.png
   - 填写提交说明，点击"Commit changes"

4. **启用GitHub Pages**
   - 进入仓库Settings
   - 左侧菜单找到"Pages"
   - Source选择"Deploy from a branch"
   - Branch选择"main"/"root"
   - 点击"Save"

5. **获取访问地址**
   - 几分钟后访问：`https://你的用户名.github.io/buddhist-calendar/`

### 方案2：Netlify（拖拽部署，最简单）

1. **访问 Netlify**
   - 打开 https://www.netlify.com/
   - 用GitHub或邮箱注册

2. **拖拽部署**
   - 将整个文件夹拖拽到Netlify页面
   - 等待部署完成
   - 获得访问地址

### 方案3：Vercel（从GitHub导入）

1. **访问 Vercel**
   - 打开 https://vercel.com/
   - 用GitHub账号登录

2. **导入项目**
   - 点击"New Project"
   - 选择刚才的GitHub仓库
   - 点击"Deploy"

---

## 第五步：在手机上安装

### 安卓手机

1. 用Chrome浏览器打开你的网站
2. 等待几秒，浏览器会提示"添加到主屏幕"
3. 点击"添加"或"安装"
4. 应用图标出现在桌面

**如果没有提示：**
1. 点击浏览器右上角菜单（三个点）
2. 选择"添加到主屏幕"
3. 确认添加

### iPhone

1. 用Safari浏览器打开你的网站
2. 点击底部分享按钮（方框带向上箭头）
3. 向下滑动，找到"添加到主屏幕"
4. 点击右上角"添加"

---

## 验证PWA安装成功

✅ 应用图标出现在手机桌面
✅ 点击图标打开，像原生应用
✅ 可以全屏显示，没有浏览器地址栏
✅ 断网后仍可正常使用
✅ 可以在设置中查看应用信息

---

## 常见问题

**Q: 为什么手机浏览器没有"添加到主屏幕"选项？**
A: 需要确保：
   - 使用HTTPS协议（GitHub Pages自动支持）
   - 或使用localhost（本地测试）
   - 图标文件存在且路径正确

**Q: 断网后无法使用？**
A: 检查Service Worker是否注册成功：
   - 打开开发者工具（F12）
   - Console中应该显示"Service Worker 注册成功"

**Q: 图标不显示？**
A: 确认：
   - 图标文件名正确（icon-192.png, icon-512.png）
   - 图标文件与HTML在同一目录
   - 图标文件格式是PNG

**Q: iPhone安装后打开是网页而不是应用？**
A: 确保使用Safari浏览器，不要用Chrome

---

## 分享给他人

部署到GitHub Pages后，直接分享网址给他人，他们：
1. 用手机浏览器打开网址
2. 添加到主屏幕
3. 永久使用，无需更新

---

## 技术支持

遇到问题？检查：
1. 浏览器控制台是否有错误（F12）
2. 所有文件是否齐全
3. Service Worker是否注册成功
4. 图标文件是否存在

祝使用愉快！🙏
