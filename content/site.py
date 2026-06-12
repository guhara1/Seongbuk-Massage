# 사이트 공통 설정
BASE_URL = "https://seongbuk-massage.pages.dev"

# IndexNow 인증 키 — 빌드 시 /{키}.txt 파일로 생성되어 도메인 소유를 증명한다.
INDEXNOW_KEY = "86342216957187b8329f3d200e9f130d"

BRAND = "간다GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 상단 메뉴 — 하위 메뉴에는 키워드를 반복하지 않고 지역명·역명만 표시한다.
NAV = [
    ("홈", "/", []),
    ("성북 출장마사지", "/massage/", [
        ("출장마사지 안내", "/massage/#service"),
        ("홈타이 안내", "/massage/#hometai"),
        ("전지역 방문 안내", "/massage/#coverage"),
        ("지하철역 인근 안내", "/massage/#stations"),
        ("예약 가능 시간", "/massage/#hours"),
        ("코스 선택 안내", "/massage/#course"),
        ("이용 전 확인사항", "/massage/#check"),
        ("위생·안전 안내", "/massage/#safety"),
        ("자주 묻는 질문", "/massage/#faq"),
    ]),
    ("지역별 안내", "/seongbuk/", [
        ("성북구 전체", "/seongbuk/"),
        ("성북동", "/seongbuk/seongbuk-dong/"),
        ("삼선동", "/seongbuk/samseon-dong/"),
        ("동선동", "/seongbuk/dongseon-dong/"),
        ("돈암동", "/seongbuk/donam-dong/"),
        ("안암동", "/seongbuk/anam-dong/"),
        ("보문동", "/seongbuk/bomun-dong/"),
        ("정릉동", "/seongbuk/jeongneung-dong/"),
        ("길음동", "/seongbuk/gireum-dong/"),
        ("종암동", "/seongbuk/jongam-dong/"),
        ("월곡동", "/seongbuk/wolgok-dong/"),
        ("장위동", "/seongbuk/jangwi-dong/"),
        ("석관동", "/seongbuk/seokgwan-dong/"),
    ]),
    ("지하철역별 안내", "/seongbuk/stations/", [
        ("역 전체", "/seongbuk/stations/"),
        ("석계역", "/seongbuk/stations/seokgye-station/"),
        ("한성대입구역", "/seongbuk/stations/hansung-univ-station/"),
        ("성신여대입구역", "/seongbuk/stations/sungshin-womens-univ-station/"),
        ("길음역", "/seongbuk/stations/gireum-station/"),
        ("돌곶이역", "/seongbuk/stations/dolgogi-station/"),
        ("상월곡역", "/seongbuk/stations/sangwolgok-station/"),
        ("월곡역", "/seongbuk/stations/wolgok-station/"),
        ("고려대역", "/seongbuk/stations/korea-univ-station/"),
        ("안암역", "/seongbuk/stations/anam-station/"),
        ("보문역", "/seongbuk/stations/bomun-station/"),
        ("북한산보국문역", "/seongbuk/stations/bukhansan-bogungmun-station/"),
        ("정릉역", "/seongbuk/stations/jeongneung-station/"),
    ]),
    ("테마별 안내", "/seongbuk/themes/", [
        ("전체 테마", "/seongbuk/themes/"),
        ("스웨디시", "/seongbuk/themes/swedish/"),
        ("로미로미", "/seongbuk/themes/lomilomi/"),
        ("타이마사지", "/seongbuk/themes/thai-massage/"),
        ("중국마사지", "/seongbuk/themes/chinese/"),
        ("아로마테라피", "/seongbuk/themes/aroma/"),
        ("홈케어", "/seongbuk/themes/homecare/"),
        ("호텔식마사지", "/seongbuk/themes/hotel-style/"),
        ("발마사지", "/seongbuk/themes/foot/"),
        ("스포츠·경락", "/seongbuk/themes/sports/"),
        ("스킨케어", "/seongbuk/themes/skincare/"),
        ("왁싱", "/seongbuk/themes/waxing/"),
        ("커플 관리", "/seongbuk/themes/couple/"),
        ("24시간", "/seongbuk/themes/24hours/"),
        ("수면 가능", "/seongbuk/themes/overnight/"),
    ]),
    ("코스안내", "/courses/", [
        ("전체 코스", "/courses/"),
        ("피로 회복 관리", "/courses/#recovery"),
        ("아로마 관리", "/courses/#aroma"),
        ("스포츠 관리", "/courses/#sports"),
        ("홈타이 코스", "/courses/#hometai"),
        ("커플·가족 방문 관리", "/courses/#couple"),
        ("기업·단체 방문 관리", "/courses/#group"),
        ("가격 안내", "/courses/#price"),
        ("코스 선택 가이드", "/courses/#guide"),
    ]),
    ("예약안내", "/reservation/", [
        ("예약 방법", "/reservation/#how"),
        ("예약 가능 시간", "/reservation/#hours"),
        ("방문 가능 장소", "/reservation/#place"),
        ("결제 안내", "/reservation/#payment"),
        ("변경·취소 안내", "/reservation/#change"),
        ("예약 전 체크사항", "/reservation/#check"),
    ]),
    ("이용가이드", "/guide/", [
        ("처음 이용하시는 분", "/guide/#first"),
        ("방문 전 준비사항", "/guide/#prepare"),
        ("위생 및 안전 기준", "/guide/#hygiene"),
        ("관리 후 주의사항", "/guide/#after"),
        ("금지행위 안내", "/guide/#prohibited"),
        ("이용 FAQ", "/guide/#faq"),
    ]),
    ("후기", "/reviews/", [
        ("전체 후기", "/reviews/"),
        ("지역별 후기", "/reviews/#area"),
        ("역세권 후기", "/reviews/#station"),
        ("후기 작성 안내", "/reviews/#write"),
    ]),
    ("고객센터", "/support/", [
        ("공지사항", "/support/#notice"),
        ("자주 묻는 질문", "/support/#faq"),
        ("1:1 문의", "/support/#contact"),
        ("제휴·기업 문의", "/support/#biz"),
        ("개인정보처리방침", "/support/privacy/"),
        ("이용약관", "/support/terms/"),
    ]),
]
