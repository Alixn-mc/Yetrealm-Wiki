# 先看这个：Yetrealm Wiki 上线操作

这个目录已经是一个完整的 **MkDocs Material + GitHub Pages** 官方 Wiki 项目。

你的目标仓库：

```text
https://github.com/Alixn-mc/Yetrealm-Wiki
```

预计上线地址：

```text
https://alixn-mc.github.io/Yetrealm-Wiki/
```

---

## 最稳妥发布方式：GitHub Desktop

GitHub 网页上传不适合这个项目，因为 `docs/assets/` 里包含大量贴图文件，网页上传一次会卡在 100 个文件左右。请用 GitHub Desktop 或 Git 命令。

### 1. 安装 GitHub Desktop

安装并登录 GitHub Desktop。

### 2. Clone 仓库

在 GitHub Desktop 里选择：

```text
File → Clone repository → Alixn-mc/Yetrealm-Wiki
```

例如克隆到：

```text
D:\GitHub\Yetrealm-Wiki
```

### 3. 把本目录内容复制进去

把这个压缩包解压后的所有内容复制到刚刚 clone 出来的仓库根目录。

仓库根目录最后应该长这样：

```text
Yetrealm-Wiki/
├── .github/
├── docs/
├── tools/
├── mkdocs.yml
├── requirements.txt
├── README.md
└── 00_READ_ME_FIRST.md
```

注意：`mkdocs.yml` 必须在仓库最外层，不能套一层 `yetrealm_wiki/` 或 `Yetrealm-Wiki-ready/`。

### 4. Commit + Push

GitHub Desktop 左下角填写：

```text
Initial official Yetrealm Wiki
```

然后点：

```text
Commit to main
```

再点：

```text
Push origin
```

### 5. 开 GitHub Pages

打开仓库网页：

```text
Settings → Pages → Build and deployment → Source
```

选择：

```text
GitHub Actions
```

### 6. 等 Actions 运行

打开仓库的：

```text
Actions
```

等待 `Deploy Yetrealm Wiki` 变成绿色。

成功后网站地址是：

```text
https://alixn-mc.github.io/Yetrealm-Wiki/
```

---

## 本地检查

Windows 双击：

```text
tools/check_build.bat
```

macOS / Linux：

```bash
bash tools/check_build.sh
```

本项目已在生成环境执行过：

```bash
mkdocs build --strict
```

结果：通过。
