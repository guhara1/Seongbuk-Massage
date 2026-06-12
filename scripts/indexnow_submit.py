#!/usr/bin/env python3
"""IndexNow 일괄 통보 스크립트.

sitemap.xml 에 있는 색인 대상 URL 전체를 IndexNow 프로토콜로 통보한다.
IndexNow 는 빙·네이버·Seznam 등 참여 엔진이 키를 공유하므로,
한 엔드포인트에 제출하면 참여 엔진 전체에 전파된다.
(구글은 IndexNow 미참여 — 구글은 Search Console 사이트맵 제출로 처리)

사용법:
    python3 scripts/indexnow_submit.py            # 사이트맵 전체 URL 통보
    python3 scripts/indexnow_submit.py URL [URL]  # 지정한 URL만 통보

별도 패키지 설치 불필요 (표준 라이브러리만 사용).
"""
import json
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL, INDEXNOW_KEY

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOST = BASE_URL.split("//", 1)[1].rstrip("/")

# 어느 한 곳에만 보내도 참여 엔진 전체에 공유되지만,
# 만약을 대비해 통합 엔드포인트 + 네이버에 각각 제출한다.
ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://searchadvisor.naver.com/indexnow",
]


def sitemap_urls():
    with open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def submit(urls):
    payload = json.dumps({
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE_URL.rstrip('/')}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }).encode("utf-8")
    for endpoint in ENDPOINTS:
        req = urllib.request.Request(
            endpoint, data=payload,
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as res:
                print(f"{endpoint} → HTTP {res.status} ({len(urls)}개 URL)")
        except urllib.error.HTTPError as e:
            print(f"{endpoint} → HTTP {e.code} {e.reason}")
        except Exception as e:  # noqa: BLE001
            print(f"{endpoint} → 실패: {e}")


if __name__ == "__main__":
    urls = sys.argv[1:] or sitemap_urls()
    if not urls:
        sys.exit("통보할 URL이 없습니다. 먼저 python3 build.py 를 실행하세요.")
    submit(urls)
