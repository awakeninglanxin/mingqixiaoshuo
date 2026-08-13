# -*- coding: utf-8 -*-
"""补充修正：102岁残留清理"""
import io

repls_25 = [
    ('明锜在 102 岁结丹', '明锜在 44 岁结丹'),
    ('不是我一个人走了七十年的路——是七十个我，在同一条路上接力',
     '不是我一个人走了这些年的路——是每一层的我，在同一条路上接力'),
]
repls_1_12 = [
    ('容貌停在 102 岁', '容貌停在四十四岁'),
]

def process(path, repls, is_txt):
    s = io.open(path, encoding='utf-8-sig').read()
    orig = s
    cnt = 0
    for old, new in repls:
        if old in s:
            s = s.replace(old, new)
            cnt += 1
    if s != orig:
        enc = 'utf-8-sig' if is_txt else 'utf-8'
        io.open(path, 'w', encoding=enc, newline='').write(s)
    return cnt

base = r"D:\AAA我的文件\明锜小说\03_正文存稿"
files = [
    (base + r"\明锜天眼_Seedance动画剧本_25-36集_零点能时代.md", repls_25, False),
    (base + r"\ai漫剧第一季详细剧本\yfbudong改过的剧本\明锜天眼_Seedance动画剧本_25-36集_零点能时代.txt", repls_25, True),
    (base + r"\明锜天眼_Seedance动画剧本_1-12集_天眼初开.md", repls_1_12, False),
    (base + r"\ai漫剧第一季详细剧本\yfbudong改过的剧本\明锜天眼_Seedance动画剧本_1-12集_天眼初开.txt", repls_1_12, True),
]
for path, repls, is_txt in files:
    n = process(path, repls, is_txt)
    print(f"{path.split(chr(92))[-1]}: {n}/{len(repls)}")
print("完成")
