# 맵 003 등록 — 한라산 등반
init python:
    register_map("003", desc="한라산 등반")

label map_003:
    n "오르막은 길었고, 숨은 짧았다. 돌하르방은 바람처럼 느릿했다."
    p "춥지 않아?"
    d "돌도 식는다. 대신 오래 간다."
    menu:
        "에비앙 건네기 (₩1000)":
            if gst.can_pay(1000):
                $ gst.pay(1000)
                $ gst.add_aff(+2)
                n "‘오늘은 이걸로.’ 돌 표면에 김이 얇게 섰다."
                d "너도 숨을 나눴네."
            else:
                n "주머니가 가벼웠다. 바람도 가벼웠다."
            $ set_next_map_from_choice("003", 0)
        "사진만 찍고 ‘정복’이라고 적는다 (₩0)":
            $ gst.add_aff(0)
            n "정복은 글자였고, 산은 여전히 산이었다."
            d "나를 정복하겠다면 더 오래 기다려."
            $ set_next_map_from_choice("003", 1)
    n "정상에서 내려다본 건 풍경이 아니라, 오늘의 말수였다."
    $ mark_map_finished("003")
    jump day_loop
