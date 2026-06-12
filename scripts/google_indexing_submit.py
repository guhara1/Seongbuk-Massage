#!/usr/bin/env python3
"""구글 Indexing API 일괄 통보 스크립트.

주의: 구글 Indexing API 는 공식적으로 JobPosting·BroadcastEvent 구조화 데이터가
있는 페이지용입니다. 일반 페이지는 Search Console 사이트맵 제출이 공식 경로이며,
과거의 사이트맵 핑(google.com/ping)은 2023년 폐지되어 더 이상 동작하지 않습니다.
일반 페이지에 이 API를 쓰는 것은 정책 위반 소지가 있어 계정 제재 위험이 있다는 점을
이해하고 사용하세요.

사전 준비:
1. Google Cloud Console에서 프로젝트 생성 → "Web Search Indexing API" 활성화
2. 서비스 계정 생성 → JSON 키 다운로드
3. Search Console 에서 해당 서비스 계정 이메일을 "소유자"로 추가
4. pip install google-auth requests

사용법:
    GOOGLE_APPLICATION_CREDENTIALS=service-account.json \
        python3 scripts/google_indexing_submit.py            # 사이트맵 전체
    GOOGLE_APPLICATION_CREDENTIALS=service-account.json \
        python3 scripts/google_indexing_submit.py URL [URL]  # 지정 URL만
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def sitemap_urls():
    with open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def main():
    try:
        import requests
        from google.oauth2 import service_account
        from google.auth.transport.requests import Request as GoogleRequest
    except ImportError:
        sys.exit("pip install google-auth requests 후 다시 실행하세요.")

    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        sys.exit(
            "GOOGLE_APPLICATION_CREDENTIALS 환경변수에 서비스 계정 JSON 경로를 "
            "지정하세요. (파일 상단 사전 준비 참고)"
        )

    creds = service_account.Credentials.from_service_account_file(
        cred_path, scopes=SCOPES
    )
    creds.refresh(GoogleRequest())
    headers = {
        "Authorization": f"Bearer {creds.token}",
        "Content-Type": "application/json",
    }

    urls = sys.argv[1:] or sitemap_urls()
    ok = fail = 0
    for url in urls:
        res = requests.post(
            ENDPOINT,
            json={"url": url, "type": "URL_UPDATED"},
            headers=headers,
            timeout=30,
        )
        if res.status_code == 200:
            ok += 1
            print(f"OK   {url}")
        else:
            fail += 1
            print(f"FAIL {url} → HTTP {res.status_code} {res.text[:120]}")
    print(f"\n완료: 성공 {ok} / 실패 {fail} (일일 기본 쿼터 200건)")


if __name__ == "__main__":
    main()
