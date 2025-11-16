# 맵 001 등록 — 카페 첫 만남
init python:
    register_map("001", desc="카페 첫 만남")

label map_001:
    n "[MAPS['001']['desc']]"
    n "돌하르방은 카운터 옆 의자에 묵직하게 앉아 있었다."
    p "첫 만남이라… 뭘 마실까?"
    d "나는 늘 돌처럼 식은 걸 좋아한다."
    menu:
        "아이스 아메리카노 두 잔 (₩4000)":
            if gst.can_pay(4000):
                $ gst.pay(4000)
                $ gst.add_aff(+1)
                n "컵 사이로 김이 날아가지 않았다. 괜히 마음은 따뜻해졌다."
            else:
                n "지갑을 뒤적였지만 모래만 나왔다."
            $ set_next_map_from_choice("001", 0)
        "머그컵에 물만 따라다 준다 (₩0)":
            $ gst.add_aff(+2)
            d "정직한 온도네."
            n "말수는 적었지만, 주머니는 편안했다."
            $ set_next_map_from_choice("001", 1)
    n "카페 밖으로 나오자 유리문에 둘의 모습이 겹쳐 서 있었다."
    $ mark_map_finished("001")
    jump day_loop
