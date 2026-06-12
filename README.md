# 간다GO — 성북 출장마사지·홈타이 안내 사이트

성북구 전지역 방문 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
예약전화: **0508-202-4719**

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함

```
build.py            # 빌드 스크립트 (레이아웃·글자수 검사·sitemap 생성)
content/
  site.py           # 상호·전화·BASE_URL·메뉴 구조
  main.py           # 메인 페이지 (+ LocalBusiness/FAQPage JSON-LD)
  areas.py          # 지역별: 성북구 허브 + 대표 동 12개
  stations.py       # 지하철역별: 허브 + 12개 역
  themes.py         # 테마별: 허브 + 14개 테마
  info.py           # 출장마사지 안내·코스·예약·가이드·후기·고객센터·약관
  about.py          # 운영자 소개 (E-E-A-T)
  pricing.py        # 공용 요금 블록
assets/             # CSS, 모바일 내비 JS, 파비콘·OG 이미지
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다.

## URL 구조

```
/                                  메인 (성북 출장마사지·홈타이 예약 안내)
/massage/                          성북 출장마사지 종합 안내
/seongbuk/                         지역 허브
/seongbuk/{dong}-dong/             대표 동 12개 (성북동·삼선동·동선동·돈암동·안암동·
                                   보문동·정릉동·길음동·종암동·월곡동·장위동·석관동)
/seongbuk/stations/                역 허브
/seongbuk/stations/{station}/      역 12개 (석계·한성대입구·성신여대입구·길음·돌곶이·
                                   상월곡·월곡·고려대·안암·보문·북한산보국문·정릉)
/seongbuk/themes/{theme}/          테마 14개
/courses/ /reservation/ /guide/ /reviews/ /support/ /about/
```

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 지역은 대표 동 12개만 — 정릉1동·장위3동 같은 숫자 행정동, 보문동5가 같은 가 단위 페이지 없음
  - 통합 규칙: 성북동·성북동1가→성북동 / 삼선동1~5가→삼선동 / 동선동1~5가→동선동 /
    돈암1·2동→돈암동 / 안암동1~5가→안암동 / 보문동1~7가→보문동 / 정릉1~4동→정릉동 /
    길음1·2동→길음동 / 월곡1·2동(상·하월곡동)→월곡동 / 장위1~3동→장위동
- 역은 역 1개당 페이지 1개 — **환승역(석계 1·6호선, 성신여대입구 4호선·우이신설선,
  보문 6호선·우이신설선)도 URL 하나**, 출구별 페이지 없음
- **지역+역+테마 조합 페이지 없음** (도어웨이 방지) — 테마는 독립 페이지로만 운영
- 상단/하위 메뉴와 푸터에 키워드·지역명·역명 대량 나열 없음 (하위 메뉴는 지역명·역명만)
- 모든 페이지 본문은 페이지별 고유 작성 (지역명만 바꾼 복붙 없음)

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. `python3 build.py` 재실행 (canonical·sitemap·robots.txt에 반영됨)
3. Google Search Console에 `sitemap.xml` 제출
