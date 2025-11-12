# 경마공원: 최소 UI 결과 → 바로 다음 날
init python:
    from python.rng import horse_bet

label horse_park_scene:
    n "경마공원은 시끄러웠다. 환호, 고함, 울음."
    if knows_pref("경마공원","dislike"):
        $ add_aff(-2)
        n "돌하르방은 고개를 돌렸다."
    else:
        $ add_aff(+1)
        n "오늘은 덜 시끄럽게 느껴졌다."
    $ gst.day += 1
    jump day_loop

label horse_bet_quick:
    $ MIN_S = 1000
    $ MIN_M = 5000
    $ MIN_L = 10000
    n "경마공원. 소리와 냄새가 섞여 있었다. (가상 베팅)"
    menu:
        "소액 (₩[MIN_S])" if can_pay(MIN_S):
            $ pay(MIN_S)
            $ (res, delta) = horse_bet(MIN_S, "small")
            $ add_money(delta)
            python:
                formatted_delta = "{:+,d}".format(delta)
            n "[res] [formatted_delta]원"
            $ unlock_scene("BET_S")
            $ gst.day += 1
            jump day_loop
        "중간 (₩[MIN_M])" if can_pay(MIN_M):
            $ pay(MIN_M)
            $ (res, delta) = horse_bet(MIN_M, "med")
            $ add_money(delta)
            python:
                formatted_delta = "{:+,d}".format(delta)
            n "[res] [formatted_delta]원"
            $ unlock_scene("BET_M")
            $ gst.day += 1
            jump day_loop
        "대담하게 (₩[MIN_L])" if can_pay(MIN_L):
            $ pay(MIN_L)
            $ (res, delta) = horse_bet(MIN_L, "large")
            $ add_money(delta)
            python:
                formatted_delta = "{:+,d}".format(delta)
            n "[res] [formatted_delta]원"
            $ unlock_scene("BET_L")
            $ gst.day += 1
            jump day_loop
        "뒤로":
            jump day_loop
