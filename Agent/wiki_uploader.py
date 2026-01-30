"""
维基页面修改上传工具
应用已验证的修改到维基页面
"""

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from main import site
import json
from datetime import datetime

def apply_modifications(page_name, modifications, summary):
    """
    应用修改并上传到维基

    Args:
        page_name: 页面名称
        modifications: 修改列表 [(old_text, new_text), ...]
        summary: 编辑摘要
    """
    print(f"正在处理页面: {page_name}")

    # 获取页面
    page = site.pages[page_name]
    if not page.exists:
        print(f"错误: 页面不存在")
        return False

    # 获取当前内容
    content = page.text()
    original_length = len(content)
    print(f"当前页面长度: {original_length} 字符")

    # 应用修改
    modified_content = content
    applied_count = 0
    failed_modifications = []

    for i, (old_text, new_text) in enumerate(modifications, 1):
        if old_text in modified_content:
            # 计算出现次数
            count = modified_content.count(old_text)
            modified_content = modified_content.replace(old_text, new_text)
            applied_count += 1
            print(f"[OK] 修改 {i}: 已应用 ({count} 处)")
        else:
            failed_modifications.append(i)
            print(f"[FAIL] 修改 {i}: 未找到匹配文本")

    # 检查是否有修改
    if modified_content == content:
        print("警告: 没有任何修改被应用")
        return False

    new_length = len(modified_content)
    print(f"\n修改统计:")
    print(f"  - 成功: {applied_count}/{len(modifications)}")
    print(f"  - 失败: {len(failed_modifications)}")
    print(f"  - 字符变化: {original_length} → {new_length} ({new_length - original_length:+d})")

    if failed_modifications:
        print(f"  - 失败的修改: {failed_modifications}")
        response = input("\n是否继续上传? (y/n): ")
        if response.lower() != 'y':
            print("取消上传")
            return False

    # 保存修改后的内容到临时文件
    temp_file = f"Agent/temp/{page_name}_修改后.txt"
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(modified_content)
    print(f"\n已保存修改后的内容到: {temp_file}")

    # 上传到维基
    response = input("\n确认上传到维基? (y/n): ")
    if response.lower() != 'y':
        print("取消上传")
        return False

    try:
        page.save(modified_content, summary=summary)
        print(f"[SUCCESS] 成功上传到维基")
        return True
    except Exception as e:
        print(f"[ERROR] 上传失败: {e}")
        return False


def main():
    """应用自定义世界页面的修正"""

    page_name = "自定义世界"

    # 定义所有修改
    modifications = [
        # 1. 森林石化 - 内容修正
        (
            "影响[[森林石化]]的频率。{{待验证|哪个速度？}}",
            "影响[[森林石化]]事件发生的周期。"
        ),

        # 2. 多枝树 - 内容修正
        (
            "影响[[多枝树]]的[[后代再生]]和[[荒芜再生]]速度。<br>影响多枝树掉落[[树枝]]的频率。{{待验证}}",
            "影响[[多枝树]]的[[后代再生]]和[[荒芜再生]]速度。"
        ),

        # 3. 青蛙雨 - 内容修正
        (
            "影响[[青蛙雨]]的频率和青蛙生成数量。{{待验证|青蛙雨是在降雨时概率发生的，如何影响频率？}}",
            "影响降雨时发生[[青蛙雨]]的概率和青蛙生成数量。"
        ),

        # 4. 盐堆 - 移除待验证标记
        (
            "影响[[盐堆]]被挖掘后重新生长的速度。{{待验证}}",
            "影响[[盐堆]]被挖掘后重新生长的速度。"
        ),

        # 5. 克劳斯 - 移除待验证标记
        (
            "影响[[赃物袋]]的生成时间，以及在一次冬季可以重新生成多少次。{{待验证}}",
            "影响[[赃物袋]]的生成时间，以及在一次冬季可以重新生成多少次。"
        ),

        # 6. 果蝇王 - 移除待验证标记（会替换2处）
        (
            "影响[[果蝇王]]的最早生成时间、重生时间和生成所需的成熟[[农作物]]数量。{{待验证}}",
            "影响[[果蝇王]]的最早生成时间、重生时间和生成所需的成熟[[农作物]]数量。"
        ),

        # 7. 野火 - 移除待验证标记
        (
            "影响[[野火]]发生的频率。{{待验证}}",
            "影响[[野火]]发生的频率。"
        ),
    ]

    summary = "修正自定义世界选项说明：基于代码分析修正森林石化、多枝树、青蛙雨的描述，移除已验证的待验证标记"

    print("=" * 60)
    print("自定义世界页面修正上传工具")
    print("=" * 60)
    print(f"\n页面: {page_name}")
    print(f"修改数量: {len(modifications)}")
    print(f"编辑摘要: {summary}")
    print("\n修改列表:")
    for i, (old, new) in enumerate(modifications, 1):
        print(f"\n{i}. 查找: {old[:50]}...")
        print(f"   替换: {new[:50]}...")

    print("\n" + "=" * 60)
    response = input("\n开始处理? (y/n): ")
    if response.lower() != 'y':
        print("已取消")
        return

    apply_modifications(page_name, modifications, summary)


if __name__ == '__main__':
    main()
