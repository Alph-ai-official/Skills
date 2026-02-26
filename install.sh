#!/bin/bash

# Alph.ai API Skills 安装脚本
# 用于快速安装 Skills 到 Claude Code

set -e

# 颜色定义
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}================================${NC}"
echo -e "${BLUE}  Alph.ai API Skills 安装器${NC}"
echo -e "${BLUE}================================${NC}"
echo

# 获取脚本所在目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TARGET_DIR="$HOME/.claude/skills"

echo -e "${YELLOW}源目录:${NC} $SCRIPT_DIR"
echo -e "${YELLOW}目标目录:${NC} $TARGET_DIR"
echo

# 检查目标目录是否存在
if [ ! -d "$TARGET_DIR" ]; then
    echo -e "${YELLOW}目标目录不存在，正在创建...${NC}"
    mkdir -p "$TARGET_DIR"
fi

# 列出要安装的 skills
echo -e "${BLUE}将安装以下 Skills:${NC}"
echo "  • alphai (主导航 + 认证指南)"
echo "  • alphai-trading (交易模块 - 54 API)"
echo "  • alphai-market (行情模块 - 41 API)"
echo "  • alphai-user (用户模块 - 67 API)"
echo "  • alphai-twitter (社媒推特X - 7 API)"
echo "  • alphai-smart (智能功能 - 31 API)"
echo "  • alphai-common (公共模块 - 8 API)"
echo

# 询问用户确认
read -p "确认安装? (y/n): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}已取消安装${NC}"
    exit 0
fi

# 复制 skills
echo
echo -e "${BLUE}开始安装...${NC}"

for skill in alphai alphai-trading alphai-market alphai-user alphai-twitter alphai-smart alphai-common; do
    if [ -d "$SCRIPT_DIR/$skill" ]; then
        echo -e "${GREEN}✓${NC} 安装 $skill"
        cp -r "$SCRIPT_DIR/$skill" "$TARGET_DIR/"
    else
        echo -e "${YELLOW}⚠${NC} 跳过 $skill (目录不存在)"
    fi
done

echo
echo -e "${GREEN}================================${NC}"
echo -e "${GREEN}  安装完成！${NC}"
echo -e "${GREEN}================================${NC}"
echo
echo -e "${BLUE}使用方法:${NC}"
echo "  1. 直接调用: /alphai-trading 查询下单接口"
echo "  2. 主导航: /alphai 我想做交易"
echo "  3. 自动选择: 直接提问，Claude 会自动选择模块"
echo
echo -e "${BLUE}验证安装:${NC}"
echo "  ls ~/.claude/skills/ | grep alphai"
echo
echo -e "${YELLOW}提示:${NC} 如果 Claude Code 正在运行，建议重启以加载新 skills"
echo
