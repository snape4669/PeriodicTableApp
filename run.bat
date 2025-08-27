@echo off
chcp 65001 >nul
title 元素周期表查询工具启动器

echo 元素周期表查询工具启动器
echo ========================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到Python，请先安装Python 3.7或更高版本
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM 检查必需文件
if not exist "periodic_table_app.py" (
    echo 错误: 缺少文件 periodic_table_app.py
    pause
    exit /b 1
)

if not exist "PeriodicTableJSON.json" (
    echo 错误: 缺少文件 PeriodicTableJSON.json
    pause
    exit /b 1
)

echo 正在启动元素周期表查询工具...
echo.

REM 运行应用程序
python periodic_table_app.py

if errorlevel 1 (
    echo.
    echo 应用程序运行出错，请检查错误信息
    pause
) else (
    echo.
    echo 应用程序已正常退出
)

pause
