# -*- coding: utf-8 -*-
"""补充：证道后可改容变貌（初果以上可变年轻·四果罗汉如孙悟空变化万端）"""
import io

repls = [
    ('他的容貌定格在四十四岁——但他知道，这具身体已经不再是"会死"的那一具。',
     '他的容貌停在四十四岁——但他知道，这具身体已经不再是"会死"的那一具。而初果以上便可改容变貌，往后这副皮囊，想回少年、想化青年，都在他一念之间。'),
    ('容貌停在四十四岁，辉光已凝成永不熄灭的金丹',
     '容貌早已不再固定——初果以上便可改容变貌，此刻他把自己凝成青年模样，辉光已凝成永不熄灭的金丹'),
    ('须得四果罗汉圆满、元婴期圆满——**开满十五仙窍，与十五维度联网，那才是全知全觉**，真正走出这座七级浮屠',
     '须得四果罗汉圆满、元婴期圆满——**开满十五仙窍，与十五维度联网，那才是全知全觉**；到那时如孙悟空一般，可大可小、变化万端，任意形态随心而化，真正走出这座七级浮屠'),
]

def process(path, is_txt):
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
    (base + r"\明锜天眼_Seedance动画剧本_1-12集_天眼初开.md", False),
    (base + r"\ai漫剧第一季详细剧本\yfbudong改过的剧本\明锜天眼_Seedance动画剧本_1-12集_天眼初开.txt", True),
]
for path, is_txt in files:
    n = process(path, is_txt)
    print(f"{path.split(chr(92))[-1]}: {n}/{len(repls)}")
print("完成")
