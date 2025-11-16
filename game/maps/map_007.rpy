# 맵 007 등록 — 동문시장 야경 산책
init python:
    register_map("007", desc="동문시장 야경 산책")

label map_007:
    n "시장 천장은 주황빛 네온으로 엮여 있었다. 돌하르방의 표면도 밤색으로 물들었다."
    p "뭐부터 먹을까?"
    d "밤엔 냄새만으로도 배가 부르지."
    menu:
        "야시장 국수 한 그릇 나눠 먹기 (₩4000)":
            if gst.can_pay(4000):
                $ gst.pay(4000)
                $ gst.add_aff(+2)
                n "김이 얼굴을 가리자 우리는 한 그릇에 숨어 웃었다."
                d "국물은 뜨겁고 마음은 조용하네."
            else:
                n "주머니가 텅 비어 국물 대신 공기만 들이켰다."
            $ set_next_map_from_choice("007", 0)
        "돌하르방에게 네온팔찌 걸어주기 (₩1000)":
            if gst.can_pay(1000):
                $ gst.pay(1000)
                $ gst.add_aff(0)
                n "형광빛이 돌 표면을 따라 번졌다."
                d "빛나는 팔이라니, 잠깐은 움직일 수 있을 것 같아."
            else:
                n "팔찌 하나 못 사주고 마음만 걸어놓았다."
            $ set_next_map_from_choice("007", 1)
    n "시장 끝에서 바람이 골목으로 스며들었다. 오늘 밤은 잠들기 어렵겠다."
    $ mark_map_finished("007")
    jump day_loop
