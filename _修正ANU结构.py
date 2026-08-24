# -*- coding: utf-8 -*-
"""修正ANU结构表述：每级1680圈·7倍绞合·级间垂直（纠正合计16800/分7层/向内坍缩）"""
import io

repls_1_12 = [
    # 350行：合计16800匝 → 各自独立1680圈
    ('每条力线绕了**1680 匝**莫比乌斯螺旋。合计 16800 匝。',
     '每条力线绕了**1680 匝**莫比乌斯螺旋——10 条力线，各自独立绕满 1680 圈。'),
    # 351行：10条力线分7层 → 每条力线内部7级spirilla垂直细分
    ('- 10 条力线分 7 层螺旋上升——这就是"七级螺旋体"（spirillae）。第 1 级对应胶子（强力），第 4 级对应 W/Z 玻色子（弱力），第 7 级是最高阶力线。',
     '- 每条力线内部，又细分出 7 级更细的螺旋丝（spirillae）——**每一级都是 1680 圈**，但并行丝数按 7 倍递增（1→7→49→343→2401→16807），且每一级的缠绕平面与上一级**垂直**。第 1 级对应胶子（强力），第 4 级对应 W/Z 玻色子（弱力），第 7 级是最细的力线。'),
    # 360行：合计16800 → 每条1680（圈数恒定）
    ('├── 10条力线（3阳7阴）× 1680匝 = 16800 匝总振动基数',
     '├── 10条力线（3阳7阴），每条 1680 匝（圈数恒定，非累计）'),
    # 361-363行：从外层向内层坍缩 → 逐级垂直细分，方向L1→L7
    ('├── 7级螺旋体（spirillae）从外层向内层坍缩\n│   L7(最高阶) → L6 → L5 → L4(W/Z玻色子) → L3 → L2 → L1(胶子)\n│   └── 坍缩到底 → 7个球形泡泡（Bose凝聚态）',
     '├── 7级螺旋丝（spirillae）逐级垂直细分（每级 7 倍绞合，圈数恒为 1680）\n│   L1(最宏观·1条) → L2(7条) → L3(49条) → L4(343条·W/Z玻色子) → L5(2401) → L6(16807) → L7(最微观)\n│   └── 细分到底 → 7个球形泡泡（Bose凝聚态）'),
]

repls_13_24 = [
    # 249行：10股合计16800 → 每股1680
    ('每条力线绕 1680 匝（10 股合计 16800 匝）',
     '每条力线绕 1680 匝（10 股各自独立，圈数恒定）'),
]

def process(path, repls, is_txt):
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
    (base + r"\明锜天眼_Seedance动画剧本_1-12集_天眼初开.md", repls_1_12, False),
    (base + r"\ai漫剧第一季详细剧本\yfbudong改过的剧本\明锜天眼_Seedance动画剧本_1-12集_天眼初开.txt", repls_1_12, True),
    (base + r"\明锜天眼_Seedance动画剧本_13-24集_晶体觉醒.md", repls_13_24, False),
    (base + r"\ai漫剧第一季详细剧本\yfbudong改过的剧本\明锜天眼_Seedance动画剧本_13-24集_晶体觉醒.txt", repls_13_24, True),
]
for path, repls, is_txt in files:
    ok, fail = process(path, repls, is_txt)
    print(f"{path.split(chr(92))[-1]}: 成功 {ok}/{len(repls)}，失败索引 {fail}")
print("完成")
