#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JSON转Python代码转换脚本
Convert JSON file to Python code

将PeriodicTableJSON.json转换为Python模块，避免打包后依赖外部文件
"""

import json
import os

def convert_json_to_python():
    """将JSON文件转换为Python代码"""
    
    # 读取JSON文件
    json_file = "PeriodicTableJSON.json"
    if not os.path.exists(json_file):
        print(f"错误: 找不到文件 {json_file}")
        return
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"✓ 成功读取JSON文件，包含 {len(data.get('elements', []))} 个元素")
        
        # 生成Python代码
        python_code = generate_python_code(data)
        
        # 写入Python文件
        output_file = "elements_data.py"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(python_code)
        
        print(f"✓ 成功生成Python文件: {output_file}")
        print(f"✓ 文件大小: {os.path.getsize(output_file) / 1024:.2f} KB")
        
    except Exception as e:
        print(f"错误: {e}")

def generate_python_code(data):
    """生成Python代码"""
    
    # 文件头部
    header = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
元素周期表数据模块
Periodic Table Data Module

将JSON数据嵌入到Python代码中，避免打包后依赖外部文件
"""

# 元素周期表数据
ELEMENTS_DATA = {
    "elements": [
'''
    
    # 生成元素数据
    elements_code = []
    for element in data.get('elements', []):
        element_code = format_element(element)
        elements_code.append(element_code)
    
    # 文件尾部
    footer = '''    ]
}

def get_elements_data():
    """获取元素周期表数据"""
    return ELEMENTS_DATA

def get_element_by_symbol(symbol: str):
    """根据元素符号获取元素信息"""
    for element in ELEMENTS_DATA["elements"]:
        if element["symbol"] == symbol:
            return element
    return None

def get_element_by_name(name: str):
    """根据元素名称获取元素信息"""
    for element in ELEMENTS_DATA["elements"]:
        if element["name"].lower() == name.lower():
            return element
    return None

def get_all_elements():
    """获取所有元素列表"""
    return ELEMENTS_DATA["elements"]

def get_elements_count():
    """获取元素总数"""
    return len(ELEMENTS_DATA["elements"])

def search_elements(query: str):
    """搜索元素（支持符号、名称、部分匹配）"""
    query = query.lower().strip()
    results = []
    
    for element in ELEMENTS_DATA["elements"]:
        # 检查符号
        if element["symbol"].lower() == query:
            results.append(element)
            continue
        
        # 检查英文名称
        if element["name"].lower() == query:
            results.append(element)
            continue
        
        # 检查部分匹配
        if query in element["symbol"].lower() or query in element["name"].lower():
            results.append(element)
    
    return results

if __name__ == "__main__":
    print(f"元素周期表数据模块")
    print(f"包含 {get_elements_count()} 个元素")
    print(f"示例: {get_element_by_symbol('H')['name'] if get_element_by_symbol('H') else 'N/A'}")
'''
    
    # 组合完整代码
    full_code = header + ',\n'.join(elements_code) + footer
    
    return full_code

def format_element(element):
    """格式化单个元素数据"""
    # 处理特殊字符和格式
    formatted = {}
    
    for key, value in element.items():
        if key == "cpk-hex":
            # 处理带连字符的键名
            formatted['"cpk-hex"'] = repr(value)
        else:
            formatted[repr(key)] = format_value(value)
    
    # 生成元素代码
    element_lines = []
    element_lines.append("        {")
    
    for i, (key, value) in enumerate(formatted.items()):
        if i == len(formatted) - 1:
            element_lines.append(f"            {key}: {value}")
        else:
            element_lines.append(f"            {key}: {value},")
    
    element_lines.append("        }")
    
    return '\n'.join(element_lines)

def format_value(value):
    """格式化值"""
    if value is None:
        return "None"
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, str):
        return repr(value)
    elif isinstance(value, list):
        if all(isinstance(x, (int, float)) for x in value):
            return str(value)
        else:
            return repr(value)
    elif isinstance(value, dict):
        return format_dict(value)
    else:
        return repr(value)

def format_dict(d):
    """格式化字典"""
    if not d:
        return "{}"
    
    lines = ["{"]
    items = list(d.items())
    
    for i, (key, value) in enumerate(items):
        if i == len(items) - 1:
            lines.append(f"                {repr(key)}: {format_value(value)}")
        else:
            lines.append(f"                {repr(key)}: {format_value(value)},")
    
    lines.append("            }")
    return '\n'.join(lines)

if __name__ == "__main__":
    print("JSON转Python代码转换脚本")
    print("=" * 40)
    convert_json_to_python()
