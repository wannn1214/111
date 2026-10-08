#!/usr/bin/env python3
"""從 competitors/*.md 的逐項表格產生對照矩陣 matrix.md。

用法：python3 tools/build_matrix.py（在 trust-center-2026-10-08 目錄下執行）
"""
import re, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEAD = ['binance', 'okx', 'coinbase', 'kraken', 'bybit', 'bitget']
PEER = ['toobit', 'btcc', 'biconomy', 'blofin', 'tapbit']
NAMES = {'hotcoin': 'Hotcoin', 'binance': 'Binance', 'okx': 'OKX', 'coinbase': 'Coinbase',
         'kraken': 'Kraken', 'bybit': 'Bybit', 'bitget': 'Bitget', 'toobit': 'Toobit',
         'btcc': 'BTCC', 'biconomy': 'Biconomy', 'blofin': 'BloFin', 'tapbit': 'Tapbit'}
SYM = {'有': '●', '部分': '◐', '沒有': '○', '未驗證': '?'}


def expand(code):
    m = re.match(r'([A-E])(\d+)[–-]([A-E])?(\d+)$', code)
    if not m:
        return [code]
    a, s, _, e = m.groups()
    return [f'{a}{i}' for i in range(int(s), int(e) + 1)]


def norm(result):
    for k in ('未驗證', '部分', '沒有', '有'):
        if result.startswith(k):
            return k
    return '未驗證'


def parse(name):
    rows = {}
    for line in open(os.path.join(BASE, 'competitors', f'{name}.md'), encoding='utf-8'):
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 3 or not re.match(r'^[A-E]\d', cells[0]):
            continue
        for code in expand(cells[0]):
            rows[code] = norm(cells[2])
    return rows


def items():
    out = []
    for line in open(os.path.join(BASE, 'checklist.md'), encoding='utf-8'):
        m = re.match(r'- ([A-E]\d+) (.+)', line.strip())
        if m:
            label = re.sub(r'（.*?）', '', m.group(2)).replace('`', '').strip()
            out.append((m.group(1), label))
    return out


def main():
    data = {n: parse(n) for n in ['hotcoin'] + HEAD + PEER}
    cols = ['hotcoin'] + HEAD + PEER
    lines = ['# 安全與信任內容對照矩陣（2026-10-08）', '',
             '由 `tools/build_matrix.py` 從 `competitors/*.md` 產生，不要手改。',
             '● 有　◐ 部分　○ 沒有　? 未驗證（讀不到，不等於沒有）', '',
             '| 編號 | 項目 | ' + ' | '.join(NAMES[c] for c in cols) + ' | 頭部有／部分 | 同級有／部分 |',
             '|' + '---|' * (len(cols) + 4)]
    for code, label in items():
        vals = [data[c].get(code, '未驗證') for c in cols]
        head = sum(data[c].get(code) in ('有', '部分') for c in HEAD)
        peer = sum(data[c].get(code) in ('有', '部分') for c in PEER)
        lines.append(f'| {code} | {label} | ' + ' | '.join(SYM[v] for v in vals) +
                     f' | {head}/6 | {peer}/5 |')
    out = os.path.join(BASE, 'matrix.md')
    open(out, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    missing = {n: [c for c, _ in items() if c not in data[n]] for n in data}
    print('written', out)
    print({k: v for k, v in missing.items() if v})


if __name__ == '__main__':
    main()
