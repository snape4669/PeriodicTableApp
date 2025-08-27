#!/bin/bash

# 元素周期表查询工具启动脚本
# Launch script for Periodic Table Query Tool

echo "元素周期表查询工具启动器"
echo "========================================"
echo

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "错误: 未找到Python，请先安装Python 3.7或更高版本"
        echo "macOS用户可以使用: brew install python3"
        echo "Linux用户可以使用: sudo apt-get install python3 (Ubuntu/Debian)"
        echo "                    sudo yum install python3 (CentOS/RHEL)"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

# 检查Python版本
PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}' | cut -d. -f1,2)
REQUIRED_VERSION="3.7"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "错误: 需要Python 3.7或更高版本"
    echo "当前版本: $PYTHON_VERSION"
    exit 1
fi

echo "✓ Python版本检查通过: $PYTHON_VERSION"
echo

# 检查必需文件
if [ ! -f "periodic_table_app.py" ]; then
    echo "错误: 缺少文件 periodic_table_app.py"
    exit 1
fi

if [ ! -f "PeriodicTableJSON.json" ]; then
    echo "错误: 缺少文件 PeriodicTableJSON.json"
    exit 1
fi

echo "✓ 必需文件检查通过"
echo

# 检查tkinter是否可用
if ! $PYTHON_CMD -c "import tkinter" 2>/dev/null; then
    echo "错误: tkinter模块不可用"
    echo "请安装Python的tkinter支持"
    echo "macOS用户: brew install python-tk"
    echo "Linux用户: sudo apt-get install python3-tk (Ubuntu/Debian)"
    echo "            sudo yum install tkinter (CentOS/RHEL)"
    exit 1
fi

echo "✓ tkinter模块检查通过"
echo

echo "正在启动元素周期表查询工具..."
echo "========================================"
echo

# 运行应用程序
$PYTHON_CMD periodic_table_app.py

if [ $? -eq 0 ]; then
    echo
    echo "✓ 应用程序已正常退出"
else
    echo
    echo "❌ 应用程序运行出错，请检查错误信息"
    exit 1
fi
