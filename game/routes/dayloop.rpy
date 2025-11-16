label splashscreen:
    # if not persistent.seen_epilogue:
    #     jump pre_epilogue
    # elif not persistent.seen_intro:
    #     $ persistent.seen_intro = True
    #     jump prologue
    jump day_loop

label pre_epilogue:
    # $ persistent.seen_epilogue = True
    scene black with fade
    window show
    p "(제주는 바람이 모든 것의 방향을 정한다.)"
    d "......"
    p "돌하르방이 나를 똑바로 바라봤다. 그냥 석상인데도."
    p "말을 할 것 같은 얼굴. 말이 전부인 얼굴."
    d "첫날이 오기 전에, 네가 기억해야 할 건 하나다."
    d "바람은 불지만, 우리가 선택하는 건 멈출 곳이라는 것."
    p "그게... 무슨 뜻이야?"
    d "곧 알게 된다."
    jump prologue

label prologue:
    scene black with fade
    window show
    n "제주대 과팅은 시끄러웠다."
    n "그리고— 석상이 의자에 앉아 있었다. 모두는 웃었다."
    n "아무도 이상해하지 않았다. 그래서 이상했다. 나만."
    # $ gst.set_pref("감귤주스","dislike")
    # $ gst.set_pref("삼다수","dislike")
    jump day_loop

label day_loop:
    show screen hud
    if gst.day > 7:
        jump ending_check

    $ options = get_next_map_choices()

    if not options:
        n "더 이상 진행할 맵이 없습니다. 이야기를 정리해 보자."
        jump ending_check

    if gst.last_map_id is None and options:
        n "Day [gst.day]. 첫 만남을 시작한다."
        $ renpy.jump(options[0]["label"])

    n "Day [gst.day]. 어디로 갈까?"
    $ choice_entries = []
    python:
        for opt in options:
            text = f"[{opt['id']}] {opt['desc']}"
            choice_entries.append((text, opt["label"]))
        selected = renpy.display_menu(choice_entries)

    if selected is None:
        n "오늘은 방향을 정하지 못했다."
        jump day_loop

    $ renpy.jump(selected)
