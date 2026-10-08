#!/bin/bash
# 競品 Hub 截圖。必須在你自己的終端機、專案根目錄執行（shot.py 不能在沙盒跑）。
# 用法：cd ~/Desktop/SEO顧問-決策副本 && bash work/trust-center-2026-10-08/tools/shots.sh
OUT="outputs/信任中心競品截圖-2026-10-08"
mkdir -p "$OUT"
while IFS='|' read -r name url; do
  [ -z "$name" ] && continue
  python3 腳本工具/shot.py "$url" "$OUT/$name.png" --full
done <<'LIST'
01-coinbase-security|https://www.coinbase.com/security
02-kraken-security|https://www.kraken.com/features/security
03-kraken-trust-center|https://trust.kraken.com/
04-okx-protect|https://www.okx.com/en-us/protect
05-okx-is-okx-safe|https://www.okx.com/en-us/learn/is-okx-safe
06-toobit-safety|https://www.toobit.com/en-US/safety
07-btcc-security|https://www.btcc.com/en-US/btcc-security
08-bybit-user-protection|https://www.bybit.com/en/promo/global/user-protection
09-binance-licenses|https://www.binance.com/en/legal/licenses
10-coinbase-complaint|https://help.coinbase.com/en/submit-a-complaint
11-bitget-protection-fund|https://www.bitget.com/promotion/protection-fund
12-blofin-fake-domains|https://support.blofin.com/hc/en-us/articles/9990180550159-Risk-Warning-Recent-Fake-BloFin-Platform-Scams
LIST
