#!/bin/bash
# 在你自己的電腦上跑（雲端環境擋掉交易所網域）。只讀 GET，不登入、不送表單。
# 用法：bash work/trust-center-2026-10-08/tools/verify_local.sh > work/trust-center-2026-10-08/verify-local-$(date +%F).tsv
# 輸出欄位：網址、狀態碼、最終網址、Content-Type、title、第一個 H1、canonical、是否像 security.txt
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
TMP=$(mktemp)
printf 'url\tstatus\tfinal_url\tcontent_type\ttitle\th1\tcanonical\tlooks_like_security_txt\n'
while read -r u; do
  [ -z "$u" ] && continue
  meta=$(curl -sL -m 25 -A "$UA" -o "$TMP" -w '%{http_code}\t%{url_effective}\t%{content_type}' "$u")
  extra=$(python3 - "$TMP" <<'PY'
import re, sys, html
s = open(sys.argv[1], encoding='utf-8', errors='ignore').read()
def first(p):
    m = re.search(p, s, re.I | re.S)
    return html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip()[:80] if m else ''
title = first(r'<title[^>]*>(.*?)</title>')
h1 = first(r'<h1[^>]*>(.*?)</h1>')
canon = first(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']+)')
sectxt = 'yes' if re.search(r'^\s*Contact:', s, re.M) and '<html' not in s[:2000].lower() else 'no'
print('\t'.join([title, h1, canon, sectxt]))
PY
)
  printf '%s\t%s\t%s\n' "$u" "$meta" "$extra"
done <<'URLS'
https://www.binance.com/.well-known/security.txt
https://www.okx.com/.well-known/security.txt
https://www.coinbase.com/.well-known/security.txt
https://www.kraken.com/.well-known/security.txt
https://www.bybit.com/.well-known/security.txt
https://www.bitget.com/.well-known/security.txt
https://www.toobit.com/.well-known/security.txt
https://www.btcc.com/.well-known/security.txt
https://www.biconomy.com/.well-known/security.txt
https://blofin.com/.well-known/security.txt
https://www.tapbit.com/.well-known/security.txt
https://www.coinbase.com/security
https://www.kraken.com/features/security
https://trust.kraken.com/
https://www.okx.com/en-us/protect
https://www.okx.com/en-us/learn/is-okx-safe
https://www.toobit.com/en-US/safety
https://www.btcc.com/en-US/btcc-security
https://www.bybit.com/en/promo/global/user-protection
https://www.bitget.com/promotion/protection-fund
https://www.binance.com/en/legal/licenses
https://www.coinbase.com/legal/licenses
https://www.kraken.com/legal/disclosures
https://www.binance.com/en/support/law-enforcement
https://help.coinbase.com/en/submit-a-complaint
https://support.kraken.com/articles/complaint-handling-process
https://www.okx.com/en-us/help/formal-complaint-handling-process
https://www.biconomy.com/en/about
https://www.hotcoin.com/.well-known/security.txt
https://www.hotcoin.com/en_US/security/
https://www.hotcoin.com/en_US/trust/
URLS
rm -f "$TMP"
