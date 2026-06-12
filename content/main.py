# 메인 페이지 — 허브 역할. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "HealthAndBeautyBusiness",
  "name": "{BRAND}",
  "telephone": "{PHONE}",
  "url": "{BASE_URL}/",
  "image": "{BASE_URL}/assets/og-image.png",
  "description": "성북구 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "서울특별시 성북구"
  }},
  "openingHours": "Mo-Su 00:00-24:00",
  "priceRange": "₩90,000 - ₩180,000"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "성북구 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "기본 범위는 성북구 전체이며, 예약 시간과 정확한 위치, 배정 상황에 따라 최종 확인됩니다. 성북동부터 석관동까지 열두 개 대표 동 페이지에서 동별 조건을 미리 보실 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "성신여대입구역이나 길음역 근처도 와 주시나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "네, 성북구를 지나는 주요 역세권은 모두 안내 범위입니다. 역 상세 페이지에서 인근 생활권 정보를 확인하시고, 정확한 가능 여부는 예약 통화에서 위치 기준으로 확정됩니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "정릉1동 같은 숫자 행정동 페이지는 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "정릉1동부터 정릉4동, 길음1동과 길음2동처럼 숫자로 나뉜 행정동은 생활권이 이어져 있어 대표 동 페이지에서 통합해 안내합니다. 같은 내용을 반복하는 페이지를 만들지 않기 위한 원칙입니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "당일 예약도 받으시나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "받고 있습니다. 다만 저녁 시간대와 주말은 배정이 빨리 차는 편이라, 두어 시간 이상 여유를 두고 연락 주시면 원하는 시간을 잡기가 훨씬 수월합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "어떤 관리 테마가 있는지 어디에서 보나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "스웨디시, 로미로미, 아로마테라피 등 열네 가지 테마를 테마별 안내 페이지에서 하나씩 소개합니다. 특징과 추천 대상을 읽어 보시고 예약 시 원하시는 테마를 말씀해 주시면 됩니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 성북구 전지역</p>
    <h1>성북 출장마사지·홈타이<br>예약 안내</h1>
    <p class="hero-lead">성북구 어디에 계시든 전화 한 통으로 부르는 프리미엄 방문 케어.<br>자택은 물론 오피스텔과 숙소까지, 계신 자리에서 편하게 받아보세요.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/courses/">코스 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>12개</strong><span>대표 지역</span></li>
      <li><strong>12개</strong><span>역세권 안내</span></li>
      <li><strong>14개</strong><span>관리 테마</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="service">
<h2>성북 출장마사지·홈타이 서비스 안내</h2>
<p>성북구에서 방문 관리를 알아보실 때 궁금한 것들 — 우리 동네에 오는지, 비용은 얼마인지, 무엇을 준비해야 하는지 — 를 이 페이지에 모았습니다. 여기는 사이트의 입구 역할이라 큰 흐름만 짚고, 동네별 사정이나 테마별 특징은 각 상세 페이지로 연결해 드립니다. {BRAND}는 상담에서 안내한 그대로 방문이 진행되도록 절차를 지키는 것을 가장 중요하게 생각합니다.</p>
</section>

<section id="coverage">
<h2>성북구 전지역 방문 가능 안내</h2>
<p>방문 범위는 서울특별시 성북구 전체입니다. 지역 안내는 성북동, 삼선동, 동선동, 돈암동, 안암동, 보문동, 정릉동, 길음동, 종암동, 월곡동, 장위동, 석관동 열두 개 대표 동으로 묶었습니다. 정릉1~4동, 장위1~3동처럼 숫자로 갈라진 행정동은 따로 페이지를 두지 않고 대표 동에서 한 번에 다룹니다. 같은 동네를 잘게 쪼개 비슷한 글을 늘리기보다, 생활권 단위로 묶어 정확히 설명하는 쪽이 읽는 분께 도움이 되기 때문입니다.</p>
</section>

<section id="areas">
<h2>지역별 안내</h2>
<p>동마다 분위기가 다르면 방문 조건도 다릅니다. 한옥이 많은 성북동, 대학가인 동선동과 안암동, 뉴타운 대단지의 길음동처럼 각 페이지에 그 동네만의 특징과 예약 팁을 담았으니, 계신 동을 골라 들어가 보세요.</p>
<ul class="card-grid">
<li><a href="/seongbuk/seongbuk-dong/">성북동</a></li>
<li><a href="/seongbuk/samseon-dong/">삼선동</a></li>
<li><a href="/seongbuk/dongseon-dong/">동선동</a></li>
<li><a href="/seongbuk/donam-dong/">돈암동</a></li>
<li><a href="/seongbuk/anam-dong/">안암동</a></li>
<li><a href="/seongbuk/bomun-dong/">보문동</a></li>
<li><a href="/seongbuk/jeongneung-dong/">정릉동</a></li>
<li><a href="/seongbuk/gireum-dong/">길음동</a></li>
<li><a href="/seongbuk/jongam-dong/">종암동</a></li>
<li><a href="/seongbuk/wolgok-dong/">월곡동</a></li>
<li><a href="/seongbuk/jangwi-dong/">장위동</a></li>
<li><a href="/seongbuk/seokgwan-dong/">석관동</a></li>
</ul>
<p>구 전체 구조를 한눈에 보시려면 <a href="/seongbuk/">성북구 전체 안내</a>를 먼저 보시면 됩니다.</p>
</section>

<section id="stations">
<h2>지하철역 인근 안내</h2>
<p>위치를 역 기준으로 설명하는 편이 익숙하다면 역세권 안내를 이용해 주세요. 성북구를 지나는 4호선·6호선과 우이신설선, 구 경계의 1호선까지 열두 개 역을 한 역에 한 페이지씩 안내합니다. 석계역처럼 노선이 두 개인 환승역도 페이지는 하나로만 운영하고, 출구별 페이지는 만들지 않습니다.</p>
<ul class="card-grid">
<li><a href="/seongbuk/stations/seokgye-station/">석계역</a></li>
<li><a href="/seongbuk/stations/hansung-univ-station/">한성대입구역</a></li>
<li><a href="/seongbuk/stations/sungshin-womens-univ-station/">성신여대입구역</a></li>
<li><a href="/seongbuk/stations/gireum-station/">길음역</a></li>
<li><a href="/seongbuk/stations/dolgogi-station/">돌곶이역</a></li>
<li><a href="/seongbuk/stations/sangwolgok-station/">상월곡역</a></li>
<li><a href="/seongbuk/stations/wolgok-station/">월곡역</a></li>
<li><a href="/seongbuk/stations/korea-univ-station/">고려대역</a></li>
<li><a href="/seongbuk/stations/anam-station/">안암역</a></li>
<li><a href="/seongbuk/stations/bomun-station/">보문역</a></li>
<li><a href="/seongbuk/stations/bukhansan-bogungmun-station/">북한산보국문역</a></li>
<li><a href="/seongbuk/stations/jeongneung-station/">정릉역</a></li>
</ul>
</section>

<section id="themes">
<h2>테마별 관리 안내</h2>
<p>같은 60분이라도 테마에 따라 결이 완전히 달라집니다. 테마 페이지마다 기법의 특징과 어울리는 분, 받기 전 알아둘 점을 따로 정리했습니다. 받고 싶은 관리를 먼저 고르신 뒤, 예약 전화에서 위치를 알려주시면 됩니다.</p>
<ul class="card-grid">
<li><a href="/seongbuk/themes/swedish/">스웨디시</a></li>
<li><a href="/seongbuk/themes/lomilomi/">로미로미</a></li>
<li><a href="/seongbuk/themes/thai-massage/">타이마사지</a></li>
<li><a href="/seongbuk/themes/chinese/">중국마사지</a></li>
<li><a href="/seongbuk/themes/aroma/">아로마테라피</a></li>
<li><a href="/seongbuk/themes/homecare/">홈케어</a></li>
<li><a href="/seongbuk/themes/hotel-style/">호텔식마사지</a></li>
<li><a href="/seongbuk/themes/foot/">발마사지</a></li>
<li><a href="/seongbuk/themes/sports/">스포츠·경락</a></li>
<li><a href="/seongbuk/themes/skincare/">스킨케어</a></li>
<li><a href="/seongbuk/themes/waxing/">왁싱</a></li>
<li><a href="/seongbuk/themes/couple/">커플 관리</a></li>
<li><a href="/seongbuk/themes/24hours/">24시간</a></li>
<li><a href="/seongbuk/themes/overnight/">수면 가능</a></li>
</ul>
</section>

<section id="course">
<h2>코스 선택 안내</h2>
<p>코스는 오늘의 목적 하나만 정하면 충분합니다. 피로를 풀고 싶은 날, 조용히 쉬고 싶은 날, 운동 뒤 뭉친 몸을 풀 날, 둘이 함께 받을 날 — 상황별 기준을 <a href="/courses/">코스안내</a>에 적어 두었습니다. 읽어도 고민되면 전화로 컨디션만 말씀해 주세요.</p>
</section>

<section id="how">
<h2>예약 진행 방식</h2>
<p>예약은 다섯 단계입니다. 방문 위치 확인, 희망 시간 확인, 코스·인원 결정, 배정 가능 여부 안내, 예약 확정. 통화 전에 주소와 시간대만 정해 두시면 1~2분이면 끝납니다. 저녁과 주말은 문의가 몰리니 여유를 두고 연락 주시는 편이 좋고, 전체 절차는 <a href="/reservation/">예약안내</a>에 있습니다.</p>
</section>

<section id="check">
<h2>이용 전 확인사항</h2>
<p>방문 전에 도로명 주소와 동·호수, 공동현관 출입 방법, 주차 가능 여부, 매트 한 장을 펼 만한 조용한 공간을 확인해 주세요. 성북동이나 정릉동처럼 언덕길이 있는 동네라면 차량 진입 안내를 함께 주시면 도착이 더 정확해집니다. 준비 방법 전체는 <a href="/guide/">이용가이드</a>에 있습니다.</p>
</section>

<section id="safety">
<h2>위생 및 안전 안내</h2>
<p>시트와 타월은 이용자마다 새것으로 교체하고, 사용한 도구는 회수해 소독합니다. 예약 시 받은 연락처와 주소는 방문 목적 외에 쓰지 않습니다. 서비스는 안내된 관리 범위 안에서만 진행되며, 불법적이거나 범위를 벗어난 요청에는 어떤 경우에도 응하지 않습니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>성북구 전지역 방문이 가능한가요?</h3>
<p>기본 범위는 성북구 전체이며, 예약 시간과 정확한 위치, 배정 상황에 따라 최종 확인됩니다. 성북동부터 석관동까지 열두 개 대표 동 페이지에서 동별 조건을 미리 보실 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>성신여대입구역이나 길음역 근처도 와 주시나요?</h3>
<p>네, 성북구를 지나는 주요 역세권은 모두 안내 범위입니다. 역 상세 페이지에서 인근 생활권 정보를 확인하시고, 정확한 가능 여부는 예약 통화에서 위치 기준으로 확정됩니다.</p>
</div>
<div class="faq-item">
<h3>정릉1동 같은 숫자 행정동 페이지는 왜 따로 없나요?</h3>
<p>정릉1동부터 정릉4동, 길음1동과 길음2동처럼 숫자로 나뉜 행정동은 생활권이 이어져 있어 대표 동 페이지에서 통합해 안내합니다. 같은 내용을 반복하는 페이지를 만들지 않기 위한 원칙입니다.</p>
</div>
<div class="faq-item">
<h3>당일 예약도 받으시나요?</h3>
<p>받고 있습니다. 다만 저녁 시간대와 주말은 배정이 빨리 차는 편이라, 두어 시간 이상 여유를 두고 연락 주시면 원하는 시간을 잡기가 훨씬 수월합니다.</p>
</div>
<div class="faq-item">
<h3>어떤 관리 테마가 있는지 어디에서 보나요?</h3>
<p>스웨디시, 로미로미, 아로마테라피 등 열네 가지 테마를 테마별 안내 페이지에서 하나씩 소개합니다. 특징과 추천 대상을 읽어 보시고 예약 시 원하시는 테마를 말씀해 주시면 됩니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>성북구 방문 관리 상담은 전화가 가장 빠릅니다. 위치와 희망 시간을 알려주시면 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

# 네이버 서치어드바이저 사이트 소유 확인
_NAVER_VERIFY = '<meta name="naver-site-verification" content="46f0c6b7c26ef95c657123a44b16dbc639afd2df" />\n'

PAGE = {
    "path": "",
    "title": "성북 출장마사지·홈타이 | 성북구 전지역 방문 마사지 예약 안내",
    "desc": "성북 출장마사지·홈타이 안내입니다. 성신여대입구역, 길음역, 정릉동, 월곡동 등 성북구 전지역 방문 예약 정보를 확인해보세요.",
    "h1": "성북 출장마사지·홈타이 예약 안내",
    "body": _BODY,
    "extra_head": _NAVER_VERIFY + _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
