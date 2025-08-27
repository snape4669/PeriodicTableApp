#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
验证GitHub Actions工作流文件
Validate GitHub Actions workflow files
"""

import yaml
import os
import sys

def validate_yaml_file(file_path):
    """验证YAML文件格式"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            yaml.safe_load(f)
        print(f"✓ {file_path} YAML格式正确")
        return True
    except yaml.YAMLError as e:
        print(f"✗ {file_path} YAML格式错误: {e}")
        return False
    except Exception as e:
        print(f"✗ {file_path} 读取失败: {e}")
        return False

def main():
    """主函数"""
    print("GitHub Actions工作流文件验证")
    print("=" * 40)
    
    # 工作流文件列表
    workflow_files = [
        ".github/workflows/build-windows.yml",
        ".github/workflows/build-macos.yml"
    ]
    
    all_valid = True
    
    for workflow_file in workflow_files:
        if os.path.exists(workflow_file):
            if not validate_yaml_file(workflow_file):
                all_valid = False
        else:
            print(f"⚠️  {workflow_file} 文件不存在")
    
    print("\n" + "=" * 40)
    if all_valid:
        print("🎉 所有工作流文件验证通过！")
        return 0
    else:
        print("❌ 发现工作流文件格式错误，请修复后重试")
        return 1

if __name__ == "__main__":
    sys.exit(main())
