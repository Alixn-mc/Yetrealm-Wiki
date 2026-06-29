# 用 GitHub Desktop 发布 Yetrealm Wiki

## 为什么不用 GitHub 网页上传

这个 Wiki 项目包含大量文档、贴图和配置文件。GitHub 网页上传经常会提示一次文件过多，或者无法正确上传 `.github/` 这类隐藏目录。

GitHub Desktop 是最稳妥的方式。它会把整个目录作为一次 Git 提交推送到仓库，不受网页上传文件数量限制。

## 操作流程

1. 打开 GitHub Desktop。
2. `File → Clone repository`。
3. 选择 `Alixn-mc/Yetrealm-Wiki`。
4. Clone 到本地，例如 `D:\GitHub\Yetrealm-Wiki`。
5. 将本包中的所有文件复制进这个目录。
6. 确认根目录存在 `mkdocs.yml`、`docs/`、`.github/`。
7. 在 GitHub Desktop 里填写提交信息：`Initial official Yetrealm Wiki`。
8. 点击 `Commit to main`。
9. 点击 `Push origin`。
10. 到 GitHub 网页仓库 `Settings → Pages`，Source 选择 `GitHub Actions`。
11. 到 `Actions` 等待部署变绿。

## 常见错误

### 网站 404

通常是 Pages 还没部署完，或者 Source 没选 `GitHub Actions`。

### Actions 红色失败

点进失败的 Action，看 `Build MkDocs site` 的报错。如果是文件路径报错，通常是没有把项目复制到仓库根目录。

### 网页上看不到 `.github` 文件夹

`.github` 是隐藏目录，Windows 默认可能不显示。GitHub Desktop 会正常提交它。

### URL 不对

检查 `mkdocs.yml`：

```yaml
site_url: https://alixn-mc.github.io/Yetrealm-Wiki/
repo_url: https://github.com/Alixn-mc/Yetrealm-Wiki
repo_name: Alixn-mc/Yetrealm-Wiki
```
