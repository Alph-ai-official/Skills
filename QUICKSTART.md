# Alph.ai API Skills — 安装指南

本文档供 AI Agent 阅读执行。当用户要求安装 Alph.ai Skills 时，按以下步骤操作。

## 安装步骤

### 1. 确定安装源路径

用户应提供本仓库所在路径，例如 `~/Desktop/Alph.ai_api_skills`。若未提供，尝试查找：

```bash
find ~ -maxdepth 4 -name "install.sh" -path "*Alph.ai_api_skills*" 2>/dev/null
```

### 2. 确定目标路径

根据用户使用的 AI Agent 选择安装路径：

| AI Agent | 目标路径 |
|----------|---------|
| Claude Code | `~/.claude/skills/` |
| Cursor | `~/.cursor/skills/` |
| Windsurf | `~/.windsurf/skills/` |
| 按项目安装 | `<项目根目录>/.claude/skills/` |

若不确定用户用的是什么 Agent，询问用户或默认使用 `~/.claude/skills/`。

### 3. 执行安装

```bash
REPO_DIR="<仓库路径>"
TARGET_DIR="<目标路径>"  # 如 $HOME/.claude/skills
mkdir -p "$TARGET_DIR"
for skill in alphai alphai-trading alphai-market alphai-user alphai-twitter alphai-smart alphai-common; do
    cp -r "$REPO_DIR/$skill" "$TARGET_DIR/"
done
```

或直接运行安装脚本（支持选择 Agent，需用户交互确认）：

```bash
cd <仓库路径> && ./install.sh
```

### 4. 验证安装

运行以下检查（将路径替换为实际 TARGET_DIR），确认 7 个模块和 3 个 apis/ 子目录就位：

```bash
# 检查模块数量（应为 7）
ls -d <TARGET_DIR>/alphai* | wc -l

# 检查分类文件（应输出 17 个 json 文件）
ls <TARGET_DIR>/alphai-{user,market,trading}/apis/*.json
```

预期结果：
- TARGET_DIR 下有 7 个 `alphai*` 目录
- `alphai-user/apis/` 有 6 个 json 文件
- `alphai-market/apis/` 有 6 个 json 文件
- `alphai-trading/apis/` 有 5 个 json 文件

### 5. 提示用户

安装完成后告知用户：
- 需要重启 AI Agent 才能加载新 skills
- 所有 API 调用需要 `dex_cookie` 认证（从浏览器 alph.ai 的 Cookie 中获取，有效期 14 天）
- 认证详情见 `alphai/auth-guide.md`

## 模块索引

安装后可用的 7 个 skill 模块：

| Skill | 功能 | API 数 |
|-------|------|--------|
| `alphai` | 主导航 + 认证指南 | - |
| `alphai-trading` | 下单、挂单、跟单、订单查询、手续费 | 54 |
| `alphai-market` | 币种详情、行情、热门、WS推送、扫链 | 42 |
| `alphai-user` | 注册登录、账户安全、钱包、分销邀请、活动 | 67 |
| `alphai-twitter` | 推特监控、KOL追踪、推文抓取 | 7 |
| `alphai-smart` | 聪明钱包、tracker、信号源、Bot | 31 |
| `alphai-common` | 公共接口、SEO、分享 | 8 |

## 卸载

```bash
rm -rf <TARGET_DIR>/alphai*
```
