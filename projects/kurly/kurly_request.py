import requests
import json


cates = json.loads("""{
  "categories": [
    {
      "no": "907",
      "name": "채소",
      "show_all_flag": true,
      "pc_icon_url": "https://img-cf.kurly.com/shop/data/category/icon_veggies_inactive_pc@2x.1586324570.png",
      "icon_url": "https://img-cf.kurly.com/shop/data/category/icon_veggies_inactive@3x.1586324413.png",
      "pc_icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_veggies_active_pc@2x.1586324570.png",
      "icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_veggies_active@3x.1586324413.png",
      "categories": [
        {
          "no": "907008",
          "name": "친환경"
        },
        {
          "no": "907001",
          "name": "고구마·감자·당근"
        },
        {
          "no": "907002",
          "name": "시금치·쌈채소·나물"
        },
        {
          "no": "907003",
          "name": "브로콜리·파프리카·양배추"
        },
        {
          "no": "907005",
          "name": "양파·대파·마늘·배추"
        },
        {
          "no": "907004",
          "name": "오이·호박·고추"
        },
        {
          "no": "907007",
          "name": "냉동·이색·간편채소"
        },
        {
          "no": "907006",
          "name": "콩나물·버섯"
        }
      ]
    },
    {
      "no": "908",
      "name": "과일·견과·쌀",
      "show_all_flag": true,
      "pc_icon_url": "https://img-cf.kurly.com/shop/data/category/icon_fruit_inactive_pc@2x.1568684150.png",
      "icon_url": "https://img-cf.kurly.com/shop/data/category/icon_fruit_inactive@3x.1572229045.png",
      "pc_icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_fruit_active_pc@2x.1568684150.png",
      "icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_fruit_active@3x.1572229046.png",
      "categories": [
        {
          "no": "908008",
          "name": "친환경"
        },
        {
          "no": "908006",
          "name": "제철과일"
        },
        {
          "no": "908001",
          "name": "국산과일"
        },
        {
          "no": "908002",
          "name": "수입과일"
        },
        {
          "no": "908007",
          "name": "간편과일"
        },
        {
          "no": "908003",
          "name": "냉동·건과일"
        },
        {
          "no": "908004",
          "name": "견과류"
        },
        {
          "no": "908005",
          "name": "쌀·잡곡"
        }
      ]
    },
    {
      "no": "909",
      "name": "수산·해산·건어물",
      "show_all_flag": true,
      "pc_icon_url": "https://img-cf.kurly.com/shop/data/category/icon_seafood_inactive_pc@2x.1568684352.png",
      "icon_url": "https://img-cf.kurly.com/shop/data/category/icon_seafood_inactive@3x.1572228964.png",
      "pc_icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_seafood_active_pc@2x.1568684353.png",
      "icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_seafood_active@3x.1572228965.png",
      "categories": [
        {
          "no": "909010",
          "name": "제철수산"
        },
        {
          "no": "909001",
          "name": "생선류"
        },
        {
          "no": "909009",
          "name": "굴비·반건류"
        },
        {
          "no": "909002",
          "name": "오징어·낙지·문어"
        },
        {
          "no": "909003",
          "name": "새우·게·랍스터"
        },
        {
          "no": "909004",
          "name": "해산물·조개류"
        },
        {
          "no": "909007",
          "name": "수산가공품"
        },
        {
          "no": "909005",
          "name": "김·미역·해조류"
        },
        {
          "no": "909006",
          "name": "건어물·다시팩"
        }
      ]
    },
    {
      "no": "910",
      "name": "정육·계란",
      "show_all_flag": true,
      "pc_icon_url": "https://img-cf.kurly.com/shop/data/category/icon_meat_inactive_pc@2x.1568684452.png",
      "icon_url": "https://img-cf.kurly.com/shop/data/category/icon_meat_inactive@3x.1572229206.png",
      "pc_icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_meat_active_pc@2x.1568684452.png",
      "icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_meat_active@3x.1572229206.png",
      "categories": [
        {
          "no": "910001",
          "name": "국내산 소고기"
        },
        {
          "no": "910007",
          "name": "수입산 소고기"
        },
        {
          "no": "910002",
          "name": "돼지고기"
        },
        {
          "no": "910005",
          "name": "계란류"
        },
        {
          "no": "910004",
          "name": "닭·오리고기"
        },
        {
          "no": "910003",
          "name": "양념육·돈까스"
        },
        {
          "no": "910006",
          "name": "양고기"
        }
      ]
    },
    {
      "no": "911",
      "name": "국·반찬·메인요리",
      "show_all_flag": true,
      "pc_icon_url": "https://img-cf.kurly.com/shop/data/category/icon_side_inactive_pc@2x.1572243579.png",
      "icon_url": "https://img-cf.kurly.com/shop/data/category/icon_side_inactive@3x.1572243189.png",
      "pc_icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_side_active_pc@2x.1572243579.png",
      "icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_side_active@3x.1572243189.png",
      "categories": [
        {
          "no": "911001",
          "name": "국·탕·찌개"
        },
        {
          "no": "911006",
          "name": "밀키트·메인요리"
        },
        {
          "no": "911002",
          "name": "밑반찬"
        },
        {
          "no": "911003",
          "name": "김치·젓갈·장류"
        },
        {
          "no": "911005",
          "name": "두부·어묵·부침개"
        },
        {
          "no": "911004",
          "name": "베이컨·햄·통조림"
        }
      ]
    },
    {
      "no": "912",
      "name": "샐러드·간편식",
      "show_all_flag": true,
      "pc_icon_url": "https://img-cf.kurly.com/shop/data/category/icon_convenient_inactive_pc@2x.1572243542.png",
      "icon_url": "https://img-cf.kurly.com/shop/data/category/icon_convenient_inactive@3x.1572243452.png",
      "pc_icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_convenient_active_pc@2x.1572243543.png",
      "icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_convenient_active@3x.1572243452.png",
      "categories": [
        {
          "no": "912001",
          "name": "샐러드·닭가슴살"
        },
        {
          "no": "912003",
          "name": "도시락·밥류"
        },
        {
          "no": "912004",
          "name": "파스타·면류"
        },
        {
          "no": "912005",
          "name": "떡볶이·튀김·순대"
        },
        {
          "no": "912008",
          "name": "피자·핫도그·만두"
        },
        {
          "no": "912007",
          "name": "폭립·떡갈비·안주"
        },
        {
          "no": "912006",
          "name": "죽·스프·카레"
        },
        {
          "no": "912002",
          "name": "선식·시리얼"
        }
      ]
    },
    {
      "no": "913",
      "name": "면·양념·오일",
      "show_all_flag": true,
      "pc_icon_url": "https://img-cf.kurly.com/shop/data/category/icon_sauce_inactive_pc@2x.1572243594.png",
      "icon_url": "https://img-cf.kurly.com/shop/data/category/icon_sauce_inactive@3x.1572243130.png",
      "pc_icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_sauce_active_pc@2x.1572243594.png",
      "icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_sauce_active@3x.1572243130.png",
      "categories": [
        {
          "no": "913001",
          "name": "파스타·면류"
        },
        {
          "no": "913007",
          "name": "식초·소스·드레싱"
        },
        {
          "no": "913003",
          "name": "양념·액젓·장류"
        },
        {
          "no": "913006",
          "name": "식용유·참기름·오일"
        },
        {
          "no": "913008",
          "name": "소금·설탕·향신료"
        },
        {
          "no": "913002",
          "name": "밀가루·가루·믹스"
        }
      ]
    },
    {
      "no": "914",
      "name": "생수·음료·우유·커피",
      "show_all_flag": true,
      "pc_icon_url": "https://img-cf.kurly.com/shop/data/category/icon_snacks_inactive_pc@2x.1572243615.png",
      "icon_url": "https://img-cf.kurly.com/shop/data/category/icon_snacks_inactive@3x.1572243151.png",
      "pc_icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_snacks_active_pc@2x.1572243616.png",
      "icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_snacks_active@3x.1572243151.png",
      "categories": [
        {
          "no": "914001",
          "name": "생수·탄산수"
        },
        {
          "no": "914002",
          "name": "음료·주스"
        },
        {
          "no": "914003",
          "name": "우유·두유·요거트"
        },
        {
          "no": "914004",
          "name": "커피"
        },
        {
          "no": "914005",
          "name": "차"
        }
      ]
    },
    {
      "no": "249",
      "name": "간식·과자·떡",
      "show_all_flag": true,
      "pc_icon_url": "https://img-cf.kurly.com/shop/data/category/icon_cookie_inactive_pc.1610074008.png",
      "icon_url": "https://img-cf.kurly.com/shop/data/category/icon_cookie_inactive.1610074009.png",
      "pc_icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_cookie_active_pc.1610074008.png",
      "icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_cookie_active.1610074009.png",
      "categories": [
        {
          "no": "249001",
          "name": "과자·스낵·쿠키"
        },
        {
          "no": "249002",
          "name": "초콜릿·젤리·캔디"
        },
        {
          "no": "249003",
          "name": "떡·한과"
        },
        {
          "no": "249004",
          "name": "아이스크림"
        }
      ]
    },
    {
      "no": "915",
      "name": "베이커리·치즈·델리",
      "show_all_flag": true,
      "pc_icon_url": "https://img-cf.kurly.com/shop/data/category/icon_deli_inactive_pc@2x.1568687352.png",
      "icon_url": "https://img-cf.kurly.com/shop/data/category/icon_deli_inactive@3x.1572229829.png",
      "pc_icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_deli_active_pc@2x.1568687352.png",
      "icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_deli_active@3x.1572229829.png",
      "categories": [
        {
          "no": "915001",
          "name": "식빵·빵류"
        },
        {
          "no": "915002",
          "name": "잼·버터·스프레드"
        },
        {
          "no": "915003",
          "name": "케이크·파이·디저트"
        },
        {
          "no": "915004",
          "name": "치즈"
        },
        {
          "no": "915005",
          "name": "델리"
        },
        {
          "no": "915006",
          "name": "올리브·피클"
        }
      ]
    },
    {
      "no": "032",
      "name": "건강식품",
      "show_all_flag": true,
      "pc_icon_url": "https://img-cf.kurly.com/shop/data/category/icon_health_inactive_pc@2x.1574645922.png",
      "icon_url": "https://img-cf.kurly.com/shop/data/category/icon_health_inactive@3x.1574645923.png",
      "pc_icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_health_active_pc@2x.1574645923.png",
      "icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_health_active@3x.1574645924.png",
      "categories": [
        {
          "no": "032003",
          "name": "영양제"
        },
        {
          "no": "032004",
          "name": "유산균"
        },
        {
          "no": "032002",
          "name": "홍삼·인삼·꿀"
        },
        {
          "no": "032001",
          "name": "건강즙·건강음료"
        },
        {
          "no": "032005",
          "name": "건강분말·건강환"
        },
        {
          "no": "032008",
          "name": "다이어트·이너뷰티"
        },
        {
          "no": "032007",
          "name": "유아동"
        }
      ]
    },
    {
      "no": "722",
      "name": "와인",
      "show_all_flag": true,
      "pc_icon_url": "https://img-cf.kurly.com/category/icon/pc/fcc93d08-3fa0-4760-82e1-7f8484658c73",
      "icon_url": "https://img-cf.kurly.com/category/icon/mobile/78a2c170-69d4-465c-9548-e62fa148096d",
      "pc_icon_active_url": "https://img-cf.kurly.com/category/icon/pc/b2fed528-c5c1-49f2-9db5-e81e1aad57bd",
      "icon_active_url": "https://img-cf.kurly.com/category/icon/mobile/183049ab-7b36-48bf-a7ae-6211a3794321",
      "post_deco_icon_url": "https://res.kurly.com/pc/service/common/1908/ico_new_42x42_v2.png",
      "categories": [
        {
          "no": "722014",
          "name": "레드와인"
        },
        {
          "no": "722012",
          "name": "화이트와인"
        },
        {
          "no": "722013",
          "name": "샴페인·스파클링"
        }
      ]
    },
    {
      "no": "251",
      "name": "전통주",
      "show_all_flag": true,
      "pc_icon_url": "https://img-cf.kurly.com/category/icon/pc/9bead7b8-2a7e-4a2f-910a-ebe5c8f5f4f0",
      "icon_url": "https://img-cf.kurly.com/category/icon/mobile/70338ce8-9153-462f-8d22-99fcb132e3a4",
      "pc_icon_active_url": "https://img-cf.kurly.com/category/icon/pc/ee395c3c-2b71-4304-b730-7b7e09dd62a4",
      "icon_active_url": "https://img-cf.kurly.com/category/icon/mobile/9ab54e28-948d-4ddf-9921-2e4a0763eb6e",
      "categories": [
        {
          "no": "251001",
          "name": "막걸리·약주"
        },
        {
          "no": "251002",
          "name": "증류주·과실주"
        }
      ]
    },
    {
      "no": "918",
      "name": "생활용품·리빙·캠핑",
      "show_all_flag": true,
      "pc_icon_url": "https://img-cf.kurly.com/shop/data/category/icon_living_inactive_pc@2x.1588814089.png",
      "icon_url": "https://img-cf.kurly.com/shop/data/category/icon_living_inactive@3x.1588814090.png",
      "pc_icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_living_active_pc@2x.1588814090.png",
      "icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_living_active@3x.1588814091.png",
      "categories": [
        {
          "no": "918007",
          "name": "휴지·티슈"
        },
        {
          "no": "918016",
          "name": "여성·위생용품"
        },
        {
          "no": "918008",
          "name": "세제·청소용품"
        },
        {
          "no": "918009",
          "name": "화훼·인테리어소품"
        },
        {
          "no": "918010",
          "name": "의약외품·마스크"
        },
        {
          "no": "918011",
          "name": "생활잡화·문구"
        },
        {
          "no": "918017",
          "name": "캠핑용품"
        }
      ]
    },
    {
      "no": "233",
      "name": "스킨케어·메이크업",
      "show_all_flag": true,
      "pc_icon_url": "https://img-cf.kurly.com/shop/data/category/icon_beauty_inactive_pc.1618488987.png",
      "icon_url": "https://img-cf.kurly.com/shop/data/category/icon_beauty_inactive.1618488988.png",
      "pc_icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_beauty_active_pc.1618488987.png",
      "icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_beauty_active.1618488988.png",
      "categories": [
        {
          "no": "233001",
          "name": "스킨·미스트·패드"
        },
        {
          "no": "233002",
          "name": "에센스·앰플·로션"
        },
        {
          "no": "233003",
          "name": "크림·오일"
        },
        {
          "no": "233004",
          "name": "클렌징"
        },
        {
          "no": "233005",
          "name": "마스크팩"
        },
        {
          "no": "233006",
          "name": "선케어"
        },
        {
          "no": "233007",
          "name": "메이크업"
        },
        {
          "no": "233008",
          "name": "맨즈케어"
        },
        {
          "no": "233009",
          "name": "뷰티소품·기기"
        }
      ]
    },
    {
      "no": "012",
      "name": "헤어·바디·구강",
      "show_all_flag": true,
      "pc_icon_url": "https://img-cf.kurly.com/shop/data/category/icon_body_inactive_pc.1618528534.png",
      "icon_url": "https://img-cf.kurly.com/shop/data/category/icon_body_inactive.1618528535.png",
      "pc_icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_body_active_pc.1618528534.png",
      "icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_body_active.1618528535.png",
      "categories": [
        {
          "no": "012010",
          "name": "구강·면도"
        },
        {
          "no": "012009",
          "name": "샴푸·컨디셔너"
        },
        {
          "no": "012014",
          "name": "트리트먼트·팩"
        },
        {
          "no": "012015",
          "name": "헤어에센스·염모"
        },
        {
          "no": "012008",
          "name": "바디워시·스크럽"
        },
        {
          "no": "012016",
          "name": "바디로션·크림"
        },
        {
          "no": "012017",
          "name": "핸드·립·데오"
        },
        {
          "no": "012018",
          "name": "향수·디퓨저"
        },
        {
          "no": "012012",
          "name": "헤어·바디소품"
        }
      ]
    },
    {
      "no": "916",
      "name": "주방용품",
      "show_all_flag": true,
      "pc_icon_url": "https://img-cf.kurly.com/shop/data/category/icon_kitchen_inactive_pc@2x.1574646457.png",
      "icon_url": "https://img-cf.kurly.com/shop/data/category/icon_kitchen_inactive@3x.1574646458.png",
      "pc_icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_kitchen_active_pc@2x.1574646458.png",
      "icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_kitchen_active@3x.1574646459.png",
      "categories": [
        {
          "no": "916006",
          "name": "주방소모품·잡화"
        },
        {
          "no": "916007",
          "name": "주방·조리도구"
        },
        {
          "no": "916008",
          "name": "냄비·팬·솥"
        },
        {
          "no": "916011",
          "name": "보관용기·텀블러"
        },
        {
          "no": "916009",
          "name": "식기·테이블웨어"
        },
        {
          "no": "916010",
          "name": "컵·잔·커피도구"
        }
      ]
    },
    {
      "no": "085",
      "name": "가전제품",
      "show_all_flag": true,
      "pc_icon_url": "https://img-cf.kurly.com/shop/data/category/icon_electronic__inactive_pc@2x.1574417978.png",
      "icon_url": "https://img-cf.kurly.com/shop/data/category/icon_electronic_inactive@3x.1574417979.png",
      "pc_icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_electronic__active_pc@2x.1574417978.png",
      "icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_electronic_active@3x.1574417979.png",
      "categories": [
        {
          "no": "085002",
          "name": "주방가전"
        },
        {
          "no": "085001",
          "name": "생활가전"
        },
        {
          "no": "085003",
          "name": "계절가전"
        },
        {
          "no": "085004",
          "name": "디지털·PC"
        },
        {
          "no": "085005",
          "name": "대형·설치가전"
        }
      ]
    },
    {
      "no": "991",
      "name": "반려동물",
      "show_all_flag": true,
      "pc_icon_url": "https://img-cf.kurly.com/shop/data/category/icon_pet_inactive_pc@2x.1587442293.png",
      "icon_url": "https://img-cf.kurly.com/shop/data/category/icon_pet_inactive@3x.1587442294.png",
      "pc_icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_pet_active_pc@2x.1587442294.png",
      "icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_pet_active@3x.1587442295.png",
      "categories": [
        {
          "no": "991001",
          "name": "강아지 간식"
        },
        {
          "no": "991002",
          "name": "강아지 주식"
        },
        {
          "no": "991003",
          "name": "고양이 간식"
        },
        {
          "no": "991004",
          "name": "고양이 주식"
        },
        {
          "no": "991006",
          "name": "반려동물 용품"
        },
        {
          "no": "991007",
          "name": "배변·위생"
        },
        {
          "no": "991008",
          "name": "소용량·샘플"
        }
      ]
    },
    {
      "no": "919",
      "name": "베이비·키즈·완구",
      "show_all_flag": true,
      "pc_icon_url": "https://img-cf.kurly.com/shop/data/category/icon_kids_inactive_pc@2x.1568687537.png",
      "icon_url": "https://img-cf.kurly.com/shop/data/category/icon_kids_inactive@3x.1572229885.png",
      "pc_icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_kids_active_pc@2x.1568687537.png",
      "icon_active_url": "https://img-cf.kurly.com/shop/data/category/icon_kids_active@3x.1572229885.png",
      "categories": [
        {
          "no": "919011",
          "name": "분유·간편 이유식"
        },
        {
          "no": "919008",
          "name": "이유식 재료"
        },
        {
          "no": "919013",
          "name": "간식·음식·음료"
        },
        {
          "no": "919012",
          "name": "건강식품"
        },
        {
          "no": "919009",
          "name": "이유·수유용품"
        },
        {
          "no": "919014",
          "name": "기저귀·물티슈"
        },
        {
          "no": "919010",
          "name": "세제·위생용품"
        },
        {
          "no": "919015",
          "name": "스킨·구강케어"
        },
        {
          "no": "919016",
          "name": "완구·잡화류"
        }
      ]
    }
  ],
  "recommend_categories": [
    {
      "no": "206",
      "name": "여행·문화",
      "show_all_flag": false,
      "thumbnail_url": "https://img-cf.kurly.com/category/image/99b8796b-d0b7-4744-acab-0639cf761fb5",
      "categories": [
        {
          "no": "206009",
          "name": "국내 숙박·항공·전시"
        },
        {
          "no": "206010",
          "name": "여행 필수템"
        },
        {
          "no": "206011",
          "name": "우리집을 호텔처럼"
        },
        {
          "no": "206012",
          "name": "지난상품보기"
        }
      ]
    },
    {
      "no": "724",
      "name": "홈캉스",
      "show_all_flag": true,
      "thumbnail_url": "https://img-cf.kurly.com/category/image/291b013e-cad1-42f3-81db-d9ddb3c5db03",
      "categories": [
        {
          "no": "724001",
          "name": "브런치"
        },
        {
          "no": "724002",
          "name": "홈카페"
        },
        {
          "no": "724006",
          "name": "홈스토랑"
        },
        {
          "no": "724003",
          "name": "홈술"
        },
        {
          "no": "724004",
          "name": "홈스파"
        },
        {
          "no": "724005",
          "name": "홈테인먼트"
        }
      ]
    },
    {
      "no": "007",
      "name": "식단관리",
      "show_all_flag": false,
      "thumbnail_url": "https://img-cf.kurly.com/shop/data/category/thumbnail_diet.1585551225.jpg",
      "categories": [
        {
          "no": "007001",
          "name": "샐러드"
        },
        {
          "no": "007008",
          "name": "닭가슴살·달걀"
        },
        {
          "no": "007002",
          "name": "도시락·간편식"
        },
        {
          "no": "007009",
          "name": "간식·선식·시리얼"
        },
        {
          "no": "007006",
          "name": "클렌즈 주스"
        },
        {
          "no": "007010",
          "name": "프로틴·보조제"
        }
      ]
    },
    {
      "no": "001",
      "name": "간편한 아침식사",
      "show_all_flag": false,
      "thumbnail_url": "https://img-cf.kurly.com/shop/data/category/thumbnail_breakfast.1585549149.jpg",
      "categories": [
        {
          "no": "001001",
          "name": "베이커리·델리"
        },
        {
          "no": "001005",
          "name": "우유·커피·주스"
        },
        {
          "no": "001002",
          "name": "과일"
        },
        {
          "no": "001003",
          "name": "샐러드·간편식·스프"
        },
        {
          "no": "001004",
          "name": "선식·시리얼·그래놀라"
        }
      ]
    },
    {
      "no": "948",
      "name": "재구매 BEST",
      "show_all_flag": true,
      "thumbnail_url": "https://img-cf.kurly.com/shop/data/category/thumbnail_best_210402.1617341016.png",
      "categories": [
        {
          "no": "948001",
          "name": "신선식품"
        },
        {
          "no": "948002",
          "name": "가공식품"
        },
        {
          "no": "948003",
          "name": "반찬·간편식"
        },
        {
          "no": "948004",
          "name": "리빙·뷰티·펫"
        }
      ]
    },
    {
      "no": "183",
      "name": "3천원의 행복",
      "show_all_flag": true,
      "thumbnail_url": "https://img-cf.kurly.com/shop/data/category/thumbnail_3000_210303.1614667552.png",
      "categories": [
        {
          "no": "183001",
          "name": "1천원 미만"
        },
        {
          "no": "183002",
          "name": "2천원 미만"
        },
        {
          "no": "183003",
          "name": "3천원 미만"
        }
      ]
    },
    {
      "no": "315",
      "name": "컬리마트",
      "show_all_flag": true,
      "thumbnail_url": "https://img-cf.kurly.com/shop/data/category/thumbnail_kp_210108_4.1610088265.jpg",
      "categories": [
        {
          "no": "315008",
          "name": "라면·간편식"
        },
        {
          "no": "315009",
          "name": "김치·반찬"
        },
        {
          "no": "315010",
          "name": "간식·과자·시리얼"
        },
        {
          "no": "315014",
          "name": "유제품·아이스크림"
        },
        {
          "no": "315006",
          "name": "생수·음료·커피"
        },
        {
          "no": "315005",
          "name": "장류·양념·오일"
        },
        {
          "no": "315012",
          "name": "제지·생리대·기저귀"
        },
        {
          "no": "315013",
          "name": "헤어·바디·구강"
        },
        {
          "no": "315007",
          "name": "생활·주방용품"
        }
      ]
    },
    {
      "no": "068",
      "name": "대용량 상품",
      "show_all_flag": true,
      "thumbnail_url": "https://img-cf.kurly.com/category/image/37194cb5-e9c1-4492-ac5a-385a1ff2b624",
      "categories": []
    },
    {
      "no": "228",
      "name": "캠핑",
      "show_all_flag": false,
      "thumbnail_url": "https://img-cf.kurly.com/shop/data/category/thumbnail_camping_210405.1617341339.png",
      "categories": [
        {
          "no": "228006",
          "name": "캠핑용품"
        },
        {
          "no": "228001",
          "name": "바베큐"
        },
        {
          "no": "228002",
          "name": "채소·과일"
        },
        {
          "no": "228003",
          "name": "간편식·반찬"
        },
        {
          "no": "228004",
          "name": "양념·소스"
        },
        {
          "no": "228005",
          "name": "간식·음료"
        }
      ]
    },
    {
      "no": "955",
      "name": "1인 가구",
      "show_all_flag": true,
      "thumbnail_url": "https://img-cf.kurly.com/shop/data/category/thumbnail_single.1594026881.jpg",
      "categories": [
        {
          "no": "955003",
          "name": "한끼채소"
        },
        {
          "no": "955001",
          "name": "과일/쌀"
        },
        {
          "no": "955002",
          "name": "간편식/재료"
        },
        {
          "no": "955004",
          "name": "간식/음료"
        },
        {
          "no": "955005",
          "name": "생활용품"
        }
      ]
    },
    {
      "no": "525",
      "name": "비건",
      "show_all_flag": true,
      "thumbnail_url": "https://img-cf.kurly.com/shop/data/category/thumbnail_vegan_210303.1614667589.png",
      "categories": [
        {
          "no": "525002",
          "name": "대체육·간편식"
        },
        {
          "no": "525008",
          "name": "대체유제품·음료"
        },
        {
          "no": "525004",
          "name": "샐러드"
        },
        {
          "no": "525006",
          "name": "시리얼·선식"
        },
        {
          "no": "525001",
          "name": "간식"
        },
        {
          "no": "525003",
          "name": "베이커리"
        },
        {
          "no": "525007",
          "name": "양념·소스"
        },
        {
          "no": "525005",
          "name": "생활·뷰티"
        }
      ]
    },
    {
      "no": "990",
      "name": "오프라인 맛집",
      "show_all_flag": true,
      "thumbnail_url": "https://img-cf.kurly.com/shop/data/category/thumbnail_offline_210303.1614666430.png",
      "categories": [
        {
          "no": "990003",
          "name": "양식"
        },
        {
          "no": "990004",
          "name": "한식"
        },
        {
          "no": "990005",
          "name": "중식"
        },
        {
          "no": "990006",
          "name": "분식"
        },
        {
          "no": "990007",
          "name": "아시안"
        },
        {
          "no": "990008",
          "name": "베이커리"
        },
        {
          "no": "990009",
          "name": "카페"
        }
      ]
    },
    {
      "no": "726",
      "name": "컬리가 만든 상품",
      "show_all_flag": false,
      "thumbnail_url": "https://img-cf.kurly.com/shop/data/category/thumbnail_kurly_s_210303.1614667608.png",
      "categories": [
        {
          "no": "726003",
          "name": "Kurly`s 식품"
        },
        {
          "no": "726004",
          "name": "Kurly`s 생활용품"
        },
        {
          "no": "726002",
          "name": "일반 상품"
        }
      ]
    },
    {
      "no": "075",
      "name": "Kurly Only",
      "show_all_flag": true,
      "thumbnail_url": "https://img-cf.kurly.com/shop/data/category/thumbnail_only_210303.1614667623.png",
      "categories": [
        {
          "no": "075009",
          "name": "베이커리·간식"
        },
        {
          "no": "075004",
          "name": "반찬·간편식"
        },
        {
          "no": "075005",
          "name": "유제품·음료"
        },
        {
          "no": "075001",
          "name": "농산"
        },
        {
          "no": "075002",
          "name": "수산"
        },
        {
          "no": "075003",
          "name": "정육·계란"
        },
        {
          "no": "075006",
          "name": "가공식품"
        },
        {
          "no": "075007",
          "name": "건강식품"
        },
        {
          "no": "075008",
          "name": "리빙·펫"
        }
      ]
    },
    {
      "no": "316",
      "name": "KF365",
      "show_all_flag": true,
      "thumbnail_url": "https://img-cf.kurly.com/category/image/f8cf5fe6-4123-4147-981e-d7f889f9e316",
      "categories": [
        {
          "no": "316001",
          "name": "채소·과일"
        },
        {
          "no": "316002",
          "name": "정육·달걀"
        },
        {
          "no": "316003",
          "name": "수산"
        },
        {
          "no": "316004",
          "name": "리빙"
        },
        {
          "no": "316005",
          "name": "탄산수"
        }
      ]
    },
    {
      "no": "127",
      "name": "1% Table",
      "show_all_flag": true,
      "thumbnail_url": "https://img-cf.kurly.com/shop/data/category/thumb_kp_1PT_201222.1608611417.jpg",
      "categories": [
        {
          "no": "127001",
          "name": "과일"
        },
        {
          "no": "127002",
          "name": "정육"
        },
        {
          "no": "127003",
          "name": "수산"
        },
        {
          "no": "127004",
          "name": "커피"
        },
        {
          "no": "127005",
          "name": "치즈·잼"
        }
      ]
    }
  ],
  "recommend_categories_name": "컬리의 추천"
}""")


cookies = {
    'PHPSESSID': 'ffmu1gk85ov3nb3dnpih23gkrkqef9du310jc78emn9pnu54vmu0',
    '__cfruid': 'd03de883f58299a0564cd7be82664a67bc49e0db-1648524050',
    '_gid': 'GA1.2.1244548054.1648524050',
    '_gac_UA-90734988-1': '1.1648524050.CjwKCAjwuYWSBhByEiwAKd_n_q25uIszPUTbiCzYx1OwQ6dtclZnmgHVQ6AHPI83kWRKnHvmj5xnXBoCLRoQAvD_BwE',
    'cookie_check': '0',
    '_gat': '1',
    'XSRF-TOKEN': 'eyJpdiI6IkRwUkp0YmVrb2FDTFdqVEZGbVhcL2J3PT0iLCJ2YWx1ZSI6Imtwd2Q4dlkyVFV5ZXlHenhJcyt2bzBIc3ExT0pDcld5T3BKZzBGSEdPTFJ6UDNBNXo1UkJxWmt5cGNjVFgxS2QiLCJtYWMiOiJkZTkxNzEwMWI1MjRjNTM5N2I4MmU0OTYwYzIzYzIwYTM5YjQxZjdjMWY4Yzg3N2ZiMGM0Mjc0ODZkYmM1YzI4In0%3D',
    'api_kurly_com_session': 'eyJpdiI6IjBZZ2F0WElTZjNObTVTXC84T0lEb2ZnPT0iLCJ2YWx1ZSI6IlhMTW8yQmNDSGk3azlmTTl1THQzYWw0WXUyQkYwTnlCbVJoM002RXlRVnhublZLVjJvcVdMM2ZLYVF0MmZXbEMiLCJtYWMiOiIyOWM3Zjk4MmE3YzIwOTdjOGQ0ODQyZjZlMGQ4MjlkZjQyYzFmZWNlZjI0NWNiOWFmMjExNTk2NzM4ZTk2M2JkIn0%3D',
    'amplitude_id_65bebb55595beb82e78d5d1ae808702ckurly.com': 'eyJkZXZpY2VJZCI6IjkxMjg4ZjNjLTIwZmMtNDhhMi04MGE5LTZlOWYwNjQ0NDI5ZFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY0ODUyNDA1MDAyMywibGFzdEV2ZW50VGltZSI6MTY0ODUyNDIxMDIwNywiZXZlbnRJZCI6MzksImlkZW50aWZ5SWQiOjIsInNlcXVlbmNlTnVtYmVyIjo0MX0=',
    '_ga_2K2GN0FFY0': 'GS1.1.1648524050.1.1.1648524210.59',
    '_ga': 'GA1.1.425537756.1648524050',
}

headers = {
    'authority': 'api.kurly.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'accept': 'application/json, text/plain, */*, application/json',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjYXJ0X2lkIjoiZTU2MDNhMTUtYjQ2My00Nzk0LWFhZWMtNDJkYjM4ZDMyOTRiIiwiaXNfZ3Vlc3QiOnRydWUsInV1aWQiOm51bGwsIm1fbm8iOm51bGwsIm1faWQiOm51bGwsImxldmVsIjpudWxsLCJzdWIiOm51bGwsImlzcyI6Imh0dHA6Ly9ta3dlYi5hcGkua3VybHkuc2VydmljZXMvdjMvYXV0aC9ndWVzdCIsImlhdCI6MTY0ODUyNDA1MCwiZXhwIjoxNjQ4NTI3NjUwLCJuYmYiOjE2NDg1MjQwNTAsImp0aSI6Im1ZZU05UFRQMTBkTXhEZDMifQ.8vy3mXDXEk_44PZAsxDo_mrwI5-aCxb_RihUQpo0ku0',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://api.kurly.com/xdomain?ver=1',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'PHPSESSID=ffmu1gk85ov3nb3dnpih23gkrkqef9du310jc78emn9pnu54vmu0; __cfruid=d03de883f58299a0564cd7be82664a67bc49e0db-1648524050; _gid=GA1.2.1244548054.1648524050; _gac_UA-90734988-1=1.1648524050.CjwKCAjwuYWSBhByEiwAKd_n_q25uIszPUTbiCzYx1OwQ6dtclZnmgHVQ6AHPI83kWRKnHvmj5xnXBoCLRoQAvD_BwE; cookie_check=0; _gat=1; XSRF-TOKEN=eyJpdiI6IkRwUkp0YmVrb2FDTFdqVEZGbVhcL2J3PT0iLCJ2YWx1ZSI6Imtwd2Q4dlkyVFV5ZXlHenhJcyt2bzBIc3ExT0pDcld5T3BKZzBGSEdPTFJ6UDNBNXo1UkJxWmt5cGNjVFgxS2QiLCJtYWMiOiJkZTkxNzEwMWI1MjRjNTM5N2I4MmU0OTYwYzIzYzIwYTM5YjQxZjdjMWY4Yzg3N2ZiMGM0Mjc0ODZkYmM1YzI4In0%3D; api_kurly_com_session=eyJpdiI6IjBZZ2F0WElTZjNObTVTXC84T0lEb2ZnPT0iLCJ2YWx1ZSI6IlhMTW8yQmNDSGk3azlmTTl1THQzYWw0WXUyQkYwTnlCbVJoM002RXlRVnhublZLVjJvcVdMM2ZLYVF0MmZXbEMiLCJtYWMiOiIyOWM3Zjk4MmE3YzIwOTdjOGQ0ODQyZjZlMGQ4MjlkZjQyYzFmZWNlZjI0NWNiOWFmMjExNTk2NzM4ZTk2M2JkIn0%3D; amplitude_id_65bebb55595beb82e78d5d1ae808702ckurly.com=eyJkZXZpY2VJZCI6IjkxMjg4ZjNjLTIwZmMtNDhhMi04MGE5LTZlOWYwNjQ0NDI5ZFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY0ODUyNDA1MDAyMywibGFzdEV2ZW50VGltZSI6MTY0ODUyNDIxMDIwNywiZXZlbnRJZCI6MzksImlkZW50aWZ5SWQiOjIsInNlcXVlbmNlTnVtYmVyIjo0MX0=; _ga_2K2GN0FFY0=GS1.1.1648524050.1.1.1648524210.59; _ga=GA1.1.425537756.1648524050',
}


cate_num = [x['no'] for x in cates['categories']]
page_no = 1
cate_sum = {}
goods_list = []
for x in cate_num:
    cnt = 0
    page_no = 1
    while True:
        params = {
            'page_limit': '99',
            'page_no': f'{page_no}',
            'delivery_type': '0',
            'sort_type': '',
            'ver': '1648524210585',
        }


        res = requests.get(f'https://api.kurly.com/v1/categories/{x}', headers=headers, params=params, cookies=cookies)
        data = [x['no'] for x in json.loads(res.text)['data']['products']]
        [goods_list.append(x) for x in data]
        cnt +=len(data)
        try:
            page_no = json.loads(res.text)['paging']['next_page_no']
        except:
            print(data)
            cate_sum[x]=cnt
            break
        print(data)

print(cate_sum)
