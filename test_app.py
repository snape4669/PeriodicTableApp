#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
元素周期表查询工具测试脚本
Test script for Periodic Table Query Tool
"""

import json
import os
import sys

def test_json_loading():
    """测试JSON文件加载"""
    print("测试JSON文件加载...")
    
    try:
        with open("PeriodicTableJSON.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if "elements" in data and isinstance(data["elements"], list):
            print(f"✓ JSON文件加载成功，包含 {len(data['elements'])} 个元素")
            return True
        else:
            print("✗ JSON文件格式不正确")
            return False
    except Exception as e:
        print(f"✗ JSON文件加载失败: {e}")
        return False

def test_element_search():
    """测试元素搜索功能"""
    print("\n测试元素搜索功能...")
    
    try:
        with open("PeriodicTableJSON.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 测试通过符号查找
        test_symbols = ["H", "Fe", "Au", "U"]
        for symbol in test_symbols:
            found = False
            for element in data["elements"]:
                if element.get("symbol") == symbol:
                    found = True
                    print(f"✓ 找到元素 {symbol}: {element.get('name')}")
                    break
            if not found:
                print(f"✗ 未找到元素 {symbol}")
                return False
        
        # 测试通过名称查找
        test_names = ["Hydrogen", "Iron", "Gold", "Uranium"]
        for name in test_names:
            found = False
            for element in data["elements"]:
                if element.get("name") == name:
                    found = True
                    print(f"✓ 找到元素 {name}: {element.get('symbol')}")
                    break
            if not found:
                print(f"✗ 未找到元素 {name}")
                return False
        
        return True
    except Exception as e:
        print(f"✗ 元素搜索测试失败: {e}")
        return False

def test_required_fields():
    """测试必需字段"""
    print("\n测试必需字段...")
    
    try:
        with open("PeriodicTableJSON.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        required_fields = ["symbol", "name", "number", "atomic_mass"]
        
        for element in data["elements"]:
            for field in required_fields:
                if field not in element or element[field] is None:
                    print(f"✗ 元素 {element.get('symbol', 'Unknown')} 缺少必需字段: {field}")
                    return False
        
        print("✓ 所有元素都包含必需字段")
        return True
    except Exception as e:
        print(f"✗ 必需字段测试失败: {e}")
        return False

def test_chinese_names():
    """测试中文名称映射"""
    print("\n测试中文名称映射...")
    
    try:
        # 导入主应用程序模块
        sys.path.append('.')
        from periodic_table_app import PeriodicTableApp
        
        # 创建临时根窗口进行测试
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()  # 隐藏窗口
        
        app = PeriodicTableApp(root)
        
        # 测试一些中文名称
        test_chinese = ["氢", "铁", "金", "铀"]
        for chinese_name in test_chinese:
            element = app.find_element(chinese_name)
            if element:
                print(f"✓ 中文名称 '{chinese_name}' 对应元素: {element.get('symbol')}")
            else:
                print(f"✗ 中文名称 '{chinese_name}' 未找到对应元素")
                return False
        
        root.destroy()
        return True
    except Exception as e:
        print(f"✗ 中文名称映射测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("元素周期表查询工具测试")
    print("=" * 40)
    
    tests = [
        ("JSON文件加载", test_json_loading),
        ("元素搜索功能", test_element_search),
        ("必需字段检查", test_required_fields),
        ("中文名称映射", test_chinese_names),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n--- {test_name} ---")
        if test_func():
            passed += 1
        else:
            print(f"❌ {test_name} 测试失败")
    
    print("\n" + "=" * 40)
    print(f"测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print("🎉 所有测试通过！应用程序准备就绪。")
        return True
    else:
        print("❌ 部分测试失败，请检查问题。")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
