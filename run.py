#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
元素周期表查询工具启动脚本
Launch script for Periodic Table Query Tool
"""

import os
import sys
import subprocess
import platform

def check_python_version():
    """检查Python版本"""
    if sys.version_info < (3, 7):
        print("错误: 需要Python 3.7或更高版本")
        print(f"当前版本: {sys.version}")
        return False
    return True

def check_required_files():
    """检查必需文件"""
    required_files = ["periodic_table_app.py", "PeriodicTableJSON.json"]
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("错误: 缺少以下必需文件:")
        for file in missing_files:
            print(f"  - {file}")
        return False
    
    return True

def check_tkinter():
    """检查tkinter是否可用"""
    try:
        import tkinter
        return True
    except ImportError:
        print("错误: tkinter模块不可用")
        print("请安装Python的tkinter支持")
        return False

def run_app():
    """运行应用程序"""
    try:
        # 导入并运行主应用程序
        from periodic_table_app import main
        main()
    except Exception as e:
        print(f"启动应用程序时出错: {e}")
        print("请检查错误信息并修复问题")
        return False
    
    return True

def main():
    """主函数"""
    print("元素周期表查询工具启动器")
    print("=" * 40)
    
    # 检查Python版本
    if not check_python_version():
        sys.exit(1)
    
    # 检查必需文件
    if not check_required_files():
        sys.exit(1)
    
    # 检查tkinter
    if not check_tkinter():
        sys.exit(1)
    
    print("✓ 所有检查通过，正在启动应用程序...")
    print("=" * 40)
    
    # 运行应用程序
    if run_app():
        print("应用程序已正常退出")
    else:
        print("应用程序运行出错")
        sys.exit(1)

if __name__ == "__main__":
    main()
