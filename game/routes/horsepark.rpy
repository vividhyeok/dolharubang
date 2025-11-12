init python:
    from python.rng import horse_bet

label horse_park_scene:
    n "경마공원은 시끄러웠다. 환호, 고함, 울음."
    if gst.knows_pref("경마공원","dislike"):
        $ gst.add_aff(-2)
        n "돌하르방은 고개를 돌렸다."
    else:
        $ gst.add_aff(+1)
        n "오늘은 덜 시끄럽게 느껴졌다."
    $ gst.day += 1
    jump day_loop

label horse_bet_quick:
    $ MIN_S = 1000
    $ MIN_M = 5000
    $ MIN_L = 10000
    menu:
        "소액 (₩[MIN_S])" if gst.can_pay(MIN_S):
            $ _bet_amount = MIN_S
            $ _bet_tier = "small"
            $ _scene_id = "BET_S"
            jump .bet_processing

        "중간 (₩[MIN_M])" if gst.can_pay(MIN_M):
            $ _bet_amount = MIN_M
            $ _bet_tier = "med"
            $ _scene_id = "BET_M"
            jump .bet_processing

        "대담하게 (₩[MIN_L])" if gst.can_pay(MIN_L):
            $ _bet_amount = MIN_L
            $ _bet_tier = "large"
            $ _scene_id = "BET_L"
            jump .bet_processing

        "뒤로":
            jump day_loop

label .bet_processing:
    $ gst.pay(_bet_amount)
    $ result, delta = horse_bet(_bet_amount, _bet_tier)
    jump .bet_result

label .bet_result:
    $ gst.add_money(delta)
    python:
        formatted_delta = "{:+,d}".format(delta)
    n "[result] [formatted_delta]원"
    $ unlock_scene(_scene_id)
    $ gst.day += 1
    jump day_loop
