# 카페 데이트 (유료 선택지 + 기억 체크로 가감점)
label choose_date_scene:
    n "오늘의 만남."
    menu:
        "카페":
            jump cafe_paid_choices
        "경마공원 산책":
            jump horse_park_scene
        "다음에 보자(스킵)":
            $ gst.day += 1
            jump day_loop

label cafe_paid_choices:
    $ COST_SAMDASOO = 4000
    $ COST_BARLEY   = 0
    $ COST_EVIAN    = 1000
    $ COST_TANGERINE= 3000
    $ COST_HALLABONG= 3500

    n "카페. 돌하르방은 메뉴를 보지 않았다. 볼 필요가 없었다."
    menu:
        "보리차 (무료)":
            $ add_aff(+2)
            n "미지근함이 오래된 대답처럼 스며들었다."
            jump cafe_after

        "에비앙 (₩[COST_EVIAN])" if can_pay(COST_EVIAN):
            $ pay(COST_EVIAN)
            $ add_aff(-1)
            n "가볍다. 마음도 가볍게 흘러갔다."
            jump cafe_after

        "삼다수 (₩[COST_SAMDASOO])" if can_pay(COST_SAMDASOO):
            $ pay(COST_SAMDASOO)
            if knows_pref("삼다수","dislike"):
                $ add_aff(-3)
                n "그건 고향의 맛이라 부담스럽다고 했었다."
            else:
                $ add_aff(+1)
                n "맑았다. 그러나 표정은 흐려졌다."
            jump cafe_after

        "감귤 주스 (₩[COST_TANGERINE])" if can_pay(COST_TANGERINE):
            $ pay(COST_TANGERINE)
            if knows_pref("감귤주스","dislike"):
                $ add_aff(-4)
                n "바람이 잠시 멈췄다."
            else:
                $ add_aff(0)
                n "상큼했지만 대화는 비어 있었다."
            jump cafe_after

        "한라봉 주스 (₩[COST_HALLABONG])" if can_pay(COST_HALLABONG):
            $ pay(COST_HALLABONG)
            $ add_aff(-2)  # 상업성 피곤 설정 예시
            n "달콤했지만 조금 피곤했다."
            jump cafe_after

label cafe_after:
    python:
        scene_id = "CAFE_DAY{}".format(gst.day)
    $ unlock_scene(scene_id)
    $ gst.day += 1
    jump day_loop

label alba_scene:
    scene black with fade
    n "오늘은 알바를 했다. 시간은 빠르게 굳어갔다."
    $ add_money(3000)
    n "₩3,000을 벌었다."
    return
