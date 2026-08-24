# -*- coding: utf-8 -*-
"""修正392行：天眼能看到结构和演化 → 天眼看过去未来·肉眼通看结构本身"""
import io

repls = [
    ('明锜看着自己的双手。天眼从未让他看到这一层——天眼能看到结构和演化，但需要**数学和肉眼的双重验证**才能揭示"为什么"。',
     '明锜看着自己的双手。天眼从未让他看到这一层——天眼看得见结构的过去与未来，却看不进它静止的「里面」；要揭示这层「为什么」，得靠**肉眼通与数学的双重验证**。'),
]

def process(path, is_txt):
    s = io.open(path, encoding='utf-8-sig').read()
    orig = s
    ok = 0
    fail = []
    for i, (old, new) in enumerate(repls):
        if old in s:
            s = s.replace(old, new)
            ok += 1
        else:
            fail.append(i)
    if s != orig:
        enc = 'utf-8-sig' if is_txt else 'utf-8'
        io.open(path, 'w', encoding=enc, newline='').write(s)
    return ok, fail

base = r"D:\AAA我的文件\明锜小说\03_正文存稿"
files = [
    (base + r"\明锜天眼_Seedance动画剧本_1-12集_天眼初开.md", False),
    (base + r"\ai漫剧第一季详细剧本\yfbudong改过的剧本\明锜天眼_Seedance动画剧本_1-12集_天眼初开.txt", True),
]
for path, is_txt in files:
    ok, fail = process(path, is_txt)
    print(f"{path.split(chr(92))[-1]}: 成功 {ok}/{len(repls)}，失败索引 {fail}")
print("完成")
