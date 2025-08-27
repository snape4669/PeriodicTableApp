#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
元素周期表查询工具构建脚本
Build script for Periodic Table Query Tool
"""

import os
import sys
import subprocess
import platform
import shutil

def run_command(command, description):
    """运行命令并处理错误"""
    print(f"正在{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description}完成")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description}失败: {e}")
        print(f"错误输出: {e.stderr}")
        return False

def check_dependencies():
    """检查依赖是否安装"""
    print("检查依赖...")
    
    try:
        import PyInstaller
        print("✓ PyInstaller 已安装")
    except ImportError:
        print("✗ PyInstaller 未安装，正在安装...")
        if not run_command("pip install pyinstaller", "安装PyInstaller"):
            return False
    
    return True

def build_executable():
    """构建可执行文件"""
    system = platform.system()
    
    if system == "Windows":
        return build_windows()
    elif system == "Darwin":  # macOS
        return build_macos()
    elif system == "Linux":
        return build_linux()
    else:
        print(f"不支持的操作系统: {system}")
        return False

def build_windows():
    """构建Windows版本"""
    print("\n=== 构建Windows版本 ===")
    
    # 清理之前的构建
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    if os.path.exists("build"):
        shutil.rmtree("build")
    
    # 构建命令
    command = 'pyinstaller --onefile --windowed --name "元素周期表查询工具" periodic_table_app.py'
    
    if run_command(command, "构建Windows可执行文件"):
        print("\n✓ Windows版本构建成功！")
        print("可执行文件位置: dist/元素周期表查询工具.exe")
        return True
    else:
        print("\n✗ Windows版本构建失败")
        return False

def build_macos():
    """构建macOS版本"""
    print("\n=== 构建macOS版本 ===")
    
    # 清理之前的构建
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    if os.path.exists("build"):
        shutil.rmtree("build")
    
    # 构建命令
    command = 'pyinstaller --onefile --windowed --name "PeriodicTableApp" periodic_table_app.py'
    
    if run_command(command, "构建macOS可执行文件"):
        print("\n✓ macOS版本构建成功！")
        print("可执行文件位置: dist/PeriodicTableApp")
        
        # 创建.app包
        if create_macos_app():
            print("✓ macOS应用程序包创建成功！")
            print("应用程序包位置: PeriodicTableApp.app/")
        
        return True
    else:
        print("\n✗ macOS版本构建失败")
        return False

def build_linux():
    """构建Linux版本"""
    print("\n=== 构建Linux版本 ===")
    
    # 清理之前的构建
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    if os.path.exists("build"):
        shutil.rmtree("build")
    
    # 构建命令
    command = 'pyinstaller --onefile --windowed --name "PeriodicTableApp" periodic_table_app.py'
    
    if run_command(command, "构建Linux可执行文件"):
        print("\n✓ Linux版本构建成功！")
        print("可执行文件位置: dist/PeriodicTableApp")
        return True
    else:
        print("\n✗ Linux版本构建失败")
        return False

def create_macos_app():
    """创建macOS应用程序包"""
    try:
        # 创建.app目录结构
        app_dir = "PeriodicTableApp.app"
        contents_dir = os.path.join(app_dir, "Contents")
        macos_dir = os.path.join(contents_dir, "MacOS")
        resources_dir = os.path.join(contents_dir, "Resources")
        
        os.makedirs(macos_dir, exist_ok=True)
        os.makedirs(resources_dir, exist_ok=True)
        
        # 复制可执行文件
        shutil.copy("dist/PeriodicTableApp", macos_dir)
        
        # 创建Info.plist文件
        info_plist_content = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>PeriodicTableApp</string>
    <key>CFBundleIdentifier</key>
    <string>com.periodictable.app</string>
    <key>CFBundleName</key>
    <string>PeriodicTableApp</string>
    <key>CFBundleVersion</key>
    <string>1.0.0</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleSignature</key>
    <string>????</string>
    <key>LSMinimumSystemVersion</key>
    <string>10.13.0</string>
    <key>NSHighResolutionCapable</key>
    <true/>
</dict>
</plist>'''
        
        with open(os.path.join(contents_dir, "Info.plist"), "w", encoding="utf-8") as f:
            f.write(info_plist_content)
        
        return True
    except Exception as e:
        print(f"创建macOS应用程序包失败: {e}")
        return False

def main():
    """主函数"""
    print("元素周期表查询工具构建脚本")
    print("=" * 40)
    
    # 检查Python版本
    if sys.version_info < (3, 7):
        print("错误: 需要Python 3.7或更高版本")
        sys.exit(1)
    
    # 检查必要文件
    required_files = ["periodic_table_app.py", "elements_data.py"]
    for file in required_files:
        if not os.path.exists(file):
            print(f"错误: 缺少必要文件 {file}")
            sys.exit(1)
    
    # 检查依赖
    if not check_dependencies():
        print("错误: 依赖检查失败")
        sys.exit(1)
    
    # 构建可执行文件
    if build_executable():
        print("\n🎉 构建完成！")
        print("\n使用说明:")
        print("1. 可执行文件位于 dist/ 目录中")
        print("2. 可以直接运行该文件")
        print("3. 数据已内置，无需外部文件")
    else:
        print("\n❌ 构建失败！")
        sys.exit(1)

if __name__ == "__main__":
    main()
