# 顔グラフィック（ドット絵風 SVG）生成スクリプト
# 使い方: python tools/make_portraits.py
# 24x24 のドットマップから img/portraits/<name>.svg を書き出す。
# 記号の意味は各キャラの palette で色に割り当てる（'.' は背景）。

import os

OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'img', 'portraits')
OUTLINE = '#101018'
BG = {
    'player': ('#1e2a48', '#2c3d68'),
    'enemy':  ('#3a1c22', '#54262f'),
}

# ---- 共通パーツ ----
# 標準の顔（目・鼻・口）行 7〜15。各キャラで上下を差し替える
FACE = [
    "......hSSSSSSSSSSh......",
    "......hSSWESSWESSh......",
    "......hSSEESSEESSh......",
    ".......SSSSSSSSSS.......",
    ".......SSSsSSsSSS.......",
    ".......sSSSMMSSSs.......",
    "........sSSSSSSs........",
    ".........ssSSss.........",
    "..........SSSS..........",
]

# ---- キャラ定義 ----
CHARACTERS = {}

def define(name, team, palette, rows):
    assert len(rows) == 24, f'{name}: {len(rows)} rows'
    for i, r in enumerate(rows):
        assert len(r) == 24, f'{name}: row {i} has {len(r)} cols: {r}'
        for ch in r:
            assert ch == '.' or ch in palette, f'{name}: row {i} unknown symbol {ch!r}'
    CHARACTERS[name] = (team, palette, rows)

# アルス（ロード）：黒髪に金の額冠、青い衣
define('ars', 'player', {
    'H': '#4a3222', 'h': '#2f1e14', 'S': '#f2cfa8', 's': '#d9a97f', 'E': '#2f6fd6', 'W': '#ffffff',
    'M': '#b5563f', 'C': '#2f5fc4', 'c': '#1f3f8a', 'G': '#e2b640', 'L': '#d8dde8', 'l': '#8d94a8',
}, [
    "..........HH.H..........",
    ".......HHHHHHHHHH.H.....",
    "......HHHHHHHHHHHHH.....",
    ".....HHGGGGGGGGGGHHH....",
    ".....HHhHHHHHHHHhHH.....",
    ".....HHSSSSSSSSSSHh.....",
    ".....hHSSSSSSSSSSHh.....",
    "......hSSSSSSSSSSh......",
    "......hSSWESSWESSh......",
    "......hSSEESSEESSh......",
    ".......SSSSSSSSSS.......",
    ".......SSSsSSsSSS.......",
    ".......sSSSMMSSSs.......",
    "........sSSSSSSs........",
    ".........ssSSss.........",
    "..........SSSS..........",
    "........GGSSSSGG........",
    "......CCCGSSSSGCCC......",
    ".....CCCCCGSSGCCCCC.....",
    "....CCCCCCCCCCCCCCCC....",
    "...LCCCCCCCCCCCCCCCCL...",
    "...LlCCCCCCCCCCCCCClL...",
    "...ccLCCCCCCCCCCCCLcc...",
    "...cccccccccccccccccc...",
])

# ガルド（ソシアルナイト）：白髪に髭、鋼の鎧と赤いマント
define('gald', 'player', {
    'H': '#9aa0a8', 'h': '#6b7079', 'X': '#9aa0a8', 'S': '#e8c39e', 's': '#c99a74', 'E': '#5a4632', 'W': '#ffffff',
    'M': '#a8604a', 'L': '#c7cedb', 'l': '#8d94a8', 'R': '#8e1f2f',
}, [
    "........................",
    "........HHHHHHHH........",
    ".......HHHHHHHHHH.......",
    "......HHHHHHHHHHHH......",
    "......HhhHHHHHHhhH......",
    "......HHSSSSSSSSHH......",
    "......hSSSSSSSSSSh......",
    "......hSsSSSSSSsSh......",
    "......hSSWESSWESSh......",
    "......hSSEESSEESSh......",
    ".......SSSSSSSSSS.......",
    ".......SSXsSSsXSS.......",
    ".......XXXSMMSXXX.......",
    ".......XXXXXXXXXX.......",
    "........XXXXXXXX........",
    "..........SSSS..........",
    "........LLSSSSLL........",
    "......LLLLLSSLLLLL......",
    ".....LLLLLLLLLLLLLL.....",
    "....RLLlLLLLLLLLlLLR....",
    "...RRLLLlLLLLLLlLLLRR...",
    "...RRlLLLLLLLLLLLLlRR...",
    "...RRllLLLLLLLLLLllRR...",
    "...RRlllllllllllllllRR..",
])

# リーナ（アーチャー）：緑の長髪、緑の狩人服に革の肩当て
define('lina', 'player', {
    'H': '#3f9a5a', 'h': '#2c6e3e', 'S': '#f5d6b4', 's': '#dcae86', 'E': '#2d8c4e', 'W': '#ffffff',
    'M': '#c4604c', 'C': '#5a8f3c', 'c': '#3a5f26', 'L': '#8b5a2b',
}, [
    "........................",
    ".......HHHHHHHHHH.......",
    "......HHHHHHHHHHHH......",
    ".....HHHHHHHHHHHHHH.....",
    ".....HHhHHHHHHHHhHHH....",
    ".....HHSSSSSSSSSSHHHh...",
    ".....HHSSSSSSSSSSHHHh...",
    ".....HHSSSSSSSSSSHHHh...",
    ".....HHSSWESSWESSHHHh...",
    ".....HHSSEESSEESSHHHh...",
    ".....HHSSSSSSSSSSHHHh...",
    ".....HHSSSsSSsSSSHHhh...",
    ".....HHsSSSMMSSSsHHhh...",
    ".....HH.sSSSSSSs.HHh....",
    ".....Hh..ssSSss..Hhh....",
    ".....Hh...SSSS...Hh.....",
    ".....H..LLSSSSLL..h.....",
    "......CCCLLSSLLCCC......",
    ".....CCCCCLLSSLLCCCCC...",
    "....CCCCCCCCCCCCCCCC....",
    "...CCCCCCCCCCCCCCCCCC...",
    "...cCCCCCCCCCCCCCCCCc...",
    "...ccCCCCCCCCCCCCCCcc...",
    "...cccccccccccccccccc...",
])

# ベルン（ファイター）：赤いバンダナ、無精髭、革の胸当てに裸の肩
define('bern', 'player', {
    'H': '#6b3f1f', 'h': '#4a2a14', 'R': '#c23a3a', 'r': '#8a2525', 'S': '#e0b088', 's': '#b98560',
    'E': '#3a2a1a', 'W': '#ffffff', 'M': '#a8604a', 'X': '#7a5636', 'C': '#7a4a24', 'c': '#4f2f16',
}, [
    "........................",
    "........HHHHHHHH........",
    ".......HHHHHHHHHH.......",
    "......RRRRRRRRRRRRRR....",
    "......RrRRRRRRRRrRRR....",
    "......RRSSSSSSSSSSRRrR..",
    "......hSSSSSSSSSSh..r...",
    "......hSsSSSSSSsSh......",
    "......hSSWESSWESSh......",
    "......hSSEESSEESSh......",
    ".......SSSSSSSSSS.......",
    ".......SXSsSSsSXS.......",
    ".......XXXSMMSXXX.......",
    "........XXXXXXXX........",
    ".........ssXXss.........",
    "..........SSSS..........",
    "........SSSSSSSS........",
    "......SSSSSSSSSSSS......",
    ".....SSSSCSSSSCSSSS.....",
    "....SSSSCCSSSSCCSSSS....",
    "...SSSSCCSSSSSSCCSSSS...",
    "...SSSCCSSSSSSSSCCSSS...",
    "...ssCCCcccccccCCCss....",
    "...cccccccccccccccccc...",
])

# セリア（マージ）：紫のとんがり帽子、金髪、紫のローブ
define('celia', 'player', {
    'P': '#6b3fa0', 'p': '#472a6e', 'H': '#e8c860', 'h': '#c9a23c', 'S': '#f6dcc0', 's': '#dcb294',
    'E': '#7a4fd6', 'W': '#ffffff', 'M': '#c4604c', 'C': '#6b3fa0', 'c': '#472a6e', 'G': '#e2b640',
}, [
    "...........PP...........",
    "..........PPPP..........",
    "..........PPPP..........",
    ".........PPPPPP.........",
    "........PPPPPPPP........",
    ".......PPPGGPPPPP.......",
    "....PPPPPPPPPPPPPPPP....",
    "...ppppHHHHHHHHHHpppp...",
    "......HHhSSSSSShHH......",
    "......HSSSSSSSSSSH......",
    "......HSSWESSWESSH......",
    "......HSSEESSEESSH......",
    "......HSSSSsSSsSSH......",
    "......HsSSSMMSSSsH......",
    "......H.sSSSSSSs.H......",
    "......H..ssSSss..H......",
    "......H...SSSS...H......",
    "......H.CCGSSGCC.H......",
    ".......CCCCSSCCCC.......",
    ".....CCCCCCCCCCCCCC.....",
    "....CCCCCCGGGGCCCCCC....",
    "...CCCCCCCCGGCCCCCCCC...",
    "...ccCCCCCCCCCCCCCCcc...",
    "...cccccccccccccccccc...",
])

# ミラ（シスター）：白いベール、水色の前髪、白い法衣に金の十字
define('mira', 'player', {
    'V': '#f4f4f8', 'v': '#c9c9d6', 'H': '#8ec5e8', 'h': '#6aa5cc', 'S': '#f8e0c8', 's': '#e0b99c',
    'E': '#4a86c8', 'W': '#ffffff', 'M': '#c4604c', 'C': '#f0f0f5', 'c': '#b9b9cc', 'G': '#e2b640',
}, [
    "........................",
    "........VVVVVVVV........",
    "......VVVVVVVVVVVV......",
    ".....VVVVVVVVVVVVVV.....",
    ".....VVHHHHHHHHHHVV.....",
    ".....VVHhSSSSSShHVV.....",
    ".....VVSSSSSSSSSSVV.....",
    ".....VVSSSSSSSSSSVV.....",
    ".....VVSSWESSWESSVV.....",
    ".....VVSSEESSEESSVV.....",
    ".....VVSSSSSSSSSSVV.....",
    ".....VVSSSsSSsSSSVV.....",
    ".....VVsSSSMMSSSsVV.....",
    ".....VV.sSSSSSSs.VV.....",
    ".....VV..ssSSss..VV.....",
    ".....VV...SSSS...VV.....",
    ".....VVv..SSSS..vVV.....",
    ".....VVCCCGSSGCCCVV.....",
    "....VVCCCCCGGCCCCCVV....",
    "...vvCCCCCCCCCCCCCCvv...",
    "...CCCCCCCCGGCCCCCCCC...",
    "...CCCCCCCGGGGCCCCCCC...",
    "...ccCCCCCCGGCCCCCCcc...",
    "...cccccccccccccccccc...",
])

# ヴォルグ（ボス・ジェネラル）：赤い前立ての黒兜、顔の傷、黒鉄の鎧
define('volg', 'enemy', {
    'R': '#c23a3a', 'K': '#2a2a33', 'k': '#15151b', 'L': '#9aa0b4', 'l': '#5f6578', 'S': '#d9b48f', 's': '#b78f6b',
    'X': '#b05050', 'E': '#d63a3a', 'W': '#f0e6e6', 'M': '#8a4a3a', 'C': '#3a3a48', 'c': '#222230', 'G': '#c9a227',
}, [
    "..........RRR...........",
    ".........RRRRR..........",
    "........KKKKKKKK........",
    ".......KKKKKKKKKK.......",
    "......KKKKKKKKKKKK......",
    "......KKLLLLLLLLKK......",
    "......KKSSSSSSSSKK......",
    "......KkSXSSSSSSkK......",
    "......KkSWESSWESkK......",
    "......KkSEESSEESkK......",
    "......KkSSSXSSSSkK......",
    "......KkSSSsSSsSkK......",
    "......KksSSSMMSSkK......",
    "......Kk.sSSSSs.kK......",
    "......Kk..ssSs..kK......",
    "......KK..SSSS..KK......",
    ".....LLLLLLSSLLLLLL.....",
    "....LCCCCCGSSGCCCCCL....",
    "...LCCCCCCCGGCCCCCCCL...",
    "...LlCCCCCCCCCCCCCClL...",
    "...LlCCCGGCCCCGGCCClL...",
    "...llCCCCCCCCCCCCCCll...",
    "...ccCCCCCCCCCCCCCCcc...",
    "...cccccccccccccccccc...",
])

# ---- 汎用の敵（兜・頭巾などで差別化） ----
SOLDIER_ROWS = [
    "........................",
    "........KKKKKKKK........",
    "......KKKKKKKKKKKK......",
    ".....KKKKKKKKKKKKKK.....",
    ".....KKKLLLLLLLLKKK.....",
    ".....KKSSSSSSSSSSKK.....",
    "......kSSSSSSSSSSk......",
    "......kSsSSSSSSsSk......",
    "......kSSWESSWESSk......",
    "......kSSEESSEESSk......",
    ".......SSSSSSSSSS.......",
    ".......SSSsSSsSSS.......",
    ".......sSSSMMSSSs.......",
    "........sSSSSSSs........",
    ".........ssSSss.........",
    "..........SSSS..........",
    "........CCSSSSCC........",
    "......CCCCCSSCCCCC......",
    ".....CCCCCCCCCCCCCC.....",
    "....LCCCCCCCCCCCCCCL....",
    "...LLCCCCCCCCCCCCCCLL...",
    "...LlCCCCCCCCCCCCCClL...",
    "...ccCCCCCCCCCCCCCCcc...",
    "...cccccccccccccccccc...",
]
ENEMY_FACE = {'S': '#dcb48e', 's': '#b78f6b', 'E': '#3a2a2a', 'W': '#f4f0f0', 'M': '#8a4a3a'}

# 兵士：鉄兜に赤茶の軍服
define('soldier', 'enemy', dict(ENEMY_FACE, **{
    'K': '#6b6f7a', 'k': '#4a4d57', 'L': '#9aa0b4', 'l': '#5f6578', 'C': '#8a3b32', 'c': '#5a2620',
}), SOLDIER_ROWS)

# 騎士：兜＋面頬風（口元まで鉄）に鋼の鎧
define('knight', 'enemy', dict(ENEMY_FACE, **{
    'K': '#5a5e6c', 'k': '#3a3d47', 'L': '#b8bfcc', 'l': '#737a8c', 'C': '#8d94a8', 'c': '#5a6072',
}), [
    "........................",
    "........KKKKKKKK........",
    "......KKKKKKKKKKKK......",
    ".....KKKKKKKKKKKKKK.....",
    ".....KKKLLLLLLLLKKK.....",
    ".....KKKSSSSSSSSKKK.....",
    ".....KkSSSSSSSSSSkK.....",
    ".....KkSsSSSSSSsSkK.....",
    ".....KkSSWESSWESSkK.....",
    ".....KkSSEESSEESSkK.....",
    ".....KkSSSSSSSSSSkK.....",
    ".....KkKKKKKKKKKKkK.....",
    ".....KkKkKKKKKKkKkK.....",
    "......KKKKKKKKKKKK......",
    ".......KKKKKKKKKK.......",
    "..........SSSS..........",
    "........LLSSSSLL........",
    "......CCCCCSSCCCCC......",
    ".....CCCCCCCCCCCCCC.....",
    "....LCCCCCCCCCCCCCCL....",
    "...LLCCCCCCCCCCCCCCLL...",
    "...LlCCCCCCCCCCCCCClL...",
    "...ccCCCCCCCCCCCCCCcc...",
    "...cccccccccccccccccc...",
])

# 戦士：ベルンと同じ型で、黒いバンダナ・暗い髪色
define('fighter', 'enemy', dict(ENEMY_FACE, **{
    'H': '#3a2a1a', 'h': '#241a10', 'R': '#2a2a33', 'r': '#15151b', 'X': '#6a4a36', 'C': '#5a3a24', 'c': '#3a2416',
}), CHARACTERS['bern'][2])

# 弓兵：ミラと同じ型で、濃緑の頭巾と狩人服
define('archer', 'enemy', dict(ENEMY_FACE, **{
    'V': '#3f6b3a', 'v': '#2a4a28', 'H': '#5a4a2a', 'h': '#3e331d', 'C': '#4a6b34', 'c': '#2f4722', 'G': '#8b5a2b',
}), CHARACTERS['mira'][2])

# 魔道士：セリアと同じ型で、黒紫の帽子とローブ
define('mage', 'enemy', dict(ENEMY_FACE, **{
    'P': '#3b2a5a', 'p': '#251a3a', 'H': '#4a3a5a', 'h': '#33283f', 'C': '#3b2a5a', 'c': '#251a3a', 'G': '#8a6fc0',
}), CHARACTERS['celia'][2])


def render(name, team, palette, rows):
    bg1, bg2 = BG[team]
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="96" height="96" shape-rendering="crispEdges">',
        f'<rect width="24" height="24" fill="{bg1}"/>',
        f'<polygon points="0,24 24,0 24,24" fill="{bg2}"/>',
    ]
    # 輪郭: 背景のうち、ドットに隣接するマスを暗色で塗る
    def filled(x, y):
        return 0 <= x < 24 and 0 <= y < 24 and rows[y][x] != '.'
    for y in range(24):
        for x in range(24):
            if rows[y][x] == '.' and any(filled(x+dx, y+dy) for dx, dy in ((1,0),(-1,0),(0,1),(0,-1))):
                parts.append(f'<rect x="{x}" y="{y}" width="1" height="1" fill="{OUTLINE}"/>')
    # ドット本体（同色の連続は1つの rect にまとめる）
    for y in range(24):
        x = 0
        while x < 24:
            ch = rows[y][x]
            if ch == '.':
                x += 1; continue
            x2 = x
            while x2 + 1 < 24 and rows[y][x2 + 1] == ch:
                x2 += 1
            parts.append(f'<rect x="{x}" y="{y}" width="{x2 - x + 1}" height="1" fill="{palette[ch]}"/>')
            x = x2 + 1
    parts.append('</svg>')
    return '\n'.join(parts) + '\n'


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for name, (team, palette, rows) in CHARACTERS.items():
        path = os.path.join(OUT_DIR, f'{name}.svg')
        with open(path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(render(name, team, palette, rows))
        print('wrote', os.path.relpath(path, os.path.join(os.path.dirname(__file__), '..')))


if __name__ == '__main__':
    main()
