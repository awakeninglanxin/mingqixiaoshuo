# -*- coding: utf-8 -*-
"""修正天眼通/肉眼通的区别：肉眼通看物质结构(地基)·天眼通看过去现在未来(时间)"""
import io

repls = [
    # 1. 场景1-2.6 345-346行：两人同时看ANU → 元光肉眼通看结构·明锜天眼只看见时间线
    ('明锜闭眼，天眼展开。元光大师睁着眼，肉眼通展开。  \n两人同时看到一个 ANU（终极物理原子）——',
     '元光大师睁着眼——肉眼通展开。明锜在旁，天眼能看见的却不是这个 ANU 的「样子」，而是它在一整条时间线上的生灭——无数个 ANU 在虚空中此起彼伏，像一池永不干涸的水泡。真正的「里面」，只有肉眼通才看得见。两人一内一外，才拼出一个完整的 ANU——'),

    # 2. 场景1-2.7 运镜：天眼/肉眼通双重视界 → 肉眼通视界
    ('→ 七根绞合 → 天眼/肉眼通双重视界 → 七级螺旋全景',
     '→ 七根绞合 → 肉眼通视界 → 七级螺旋全景'),

    # 3. 场景1-2.7 383行：明锜天眼+元光肉眼通同时展开 → 元光肉眼通看结构·明锜天眼只看时间
    ('明锜的天眼和元光的肉眼通同时展开。他看到的已不是铜线，而是完整的 ANU 七级螺旋在虚空中旋转——一层套一层，每一层的轴都垂直地插进上一层的切线里，像一根被七次折叠的 DNA。',
     '元光大师的肉眼通再展开——明锜在旁，天眼能看见的只是这七级螺旋在时间里千百万次的绕成又散开；唯有肉眼通，才看得进它静止的「里面」：完整的 ANU 七级螺旋在虚空中旋转，一层套一层，每一层的轴都垂直地插进上一层的切线里，像一根被七次折叠的 DNA。'),
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
