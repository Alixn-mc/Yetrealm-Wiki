# 用 Git 命令发布 Yetrealm Wiki

适合已经安装 Git 的用户。

## 首次发布

```bash
git clone https://github.com/Alixn-mc/Yetrealm-Wiki.git
cd Yetrealm-Wiki
```

把本包里的全部文件复制到 `Yetrealm-Wiki` 目录中，然后执行：

```bash
git add .
git commit -m "Initial official Yetrealm Wiki"
git push origin main
```

然后去 GitHub 网页：

```text
Settings → Pages → Build and deployment → Source → GitHub Actions
```

## 后续更新

```bash
git add .
git commit -m "Update wiki"
git push origin main
```

每次 push 后，GitHub Actions 都会自动重新构建网站。
