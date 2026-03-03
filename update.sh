#!/bin/bash

# Alph.ai API Skills 更新脚本
# 从 GitHub 拉取最新版本并自动安装

set -e

# 颜色定义
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}================================${NC}"
echo -e "${BLUE}  Alph.ai API Skills 更新器${NC}"
echo -e "${BLUE}================================${NC}"
echo

# 获取脚本所在目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# 检查是否是 git 仓库
if [ ! -d ".git" ]; then
    echo -e "${RED}错误: 当前目录不是 git 仓库${NC}"
    echo -e "${YELLOW}如果你是通过 zip 下载的，请重新 clone:${NC}"
    echo "  git clone https://github.com/Alph-ai-official/Skills.git Alph.ai_api_skills"
    echo "  cd Alph.ai_api_skills && ./install.sh"
    exit 1
fi

# 获取当前版本
CURRENT_VERSION=$(git describe --tags --abbrev=0 2>/dev/null || echo "未知")
echo -e "${YELLOW}当前版本:${NC} $CURRENT_VERSION"

# 拉取最新代码
echo -e "${BLUE}正在检查更新...${NC}"
git fetch origin main --tags 2>/dev/null

# 检查是否有更新
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse origin/main)

if [ "$LOCAL" = "$REMOTE" ]; then
    echo -e "${GREEN}已是最新版本，无需更新！${NC}"
    exit 0
fi

# 获取最新版本号
LATEST_VERSION=$(git describe --tags --abbrev=0 origin/main 2>/dev/null || echo "最新")
echo -e "${GREEN}发现新版本:${NC} $LATEST_VERSION"
echo

# 显示更新内容
echo -e "${BLUE}更新内容:${NC}"
git log --oneline $LOCAL..$REMOTE
echo

# 确认更新
read -p "确认更新? (y/n): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}已取消更新${NC}"
    exit 0
fi

# 拉取更新
echo -e "${BLUE}正在更新...${NC}"
git pull origin main
echo

# 自动安装
echo -e "${BLUE}正在安装到本地...${NC}"
echo

# 检测已安装的位置
INSTALLED=false
for DIR in "$HOME/.claude/skills" "$HOME/.cursor/skills" "$HOME/.windsurf/skills"; do
    if [ -d "$DIR/alphai" ]; then
        echo -e "${GREEN}检测到安装目录:${NC} $DIR"
        for skill in alphai alphai-trading alphai-market alphai-user alphai-twitter alphai-smart alphai-common; do
            if [ -d "$SCRIPT_DIR/$skill" ]; then
                cp -r "$SCRIPT_DIR/$skill" "$DIR/"
                echo -e "  ${GREEN}✓${NC} 更新 $skill"
            fi
        done
        INSTALLED=true
        echo
    fi
done

if [ "$INSTALLED" = false ]; then
    echo -e "${YELLOW}未检测到已安装的 skills，请先运行 ./install.sh 进行首次安装${NC}"
    exit 0
fi

# 显示最新版本
NEW_VERSION=$(git describe --tags --abbrev=0 2>/dev/null || echo "最新")
echo -e "${GREEN}================================${NC}"
echo -e "${GREEN}  更新完成！${NC}"
echo -e "${GREEN}  $CURRENT_VERSION → $NEW_VERSION${NC}"
echo -e "${GREEN}================================${NC}"
echo
echo -e "${YELLOW}提示:${NC} 如果你的 AI Agent 正在运行，建议重启以加载更新"
echo
