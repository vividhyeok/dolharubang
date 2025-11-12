label splashscreen:
    if not persistent.seen_epilogue:
        jump pre_epilogue
    elif not persistent.seen_intro:
        $ persistent.seen_intro = True
        jump prologue
    jump day_loop

label pre_epilogue:
    $ persistent.seen_epilogue = True
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
    $ gst.set_pref("감귤주스","dislike")
    $ gst.set_pref("삼다수","dislike")
    jump day_loop

label day_loop:
    show screen hud
    if gst.day > 7:
        jump ending_check

    n "Day [gst.day]. 오늘은 무엇을 할까?"
    menu:
        "다음 번호 맵 자동 진행":
            jump day_action_auto_map

        "랜덤 후보 3개 중 고르기":
            jump day_action_pick_map

        "아르바이트를 한다 (돈 +, 오늘 스토리 스킵)":
            jump day_action_alba

        "경마공원에서 베팅한다 (결과만 보고 다음 날)":
            jump day_action_betting

label day_action_auto_map:
    $ nid = get_next_unseen_map_id()
    if nid is None:
        n "새로운 맵이 없습니다. 랜덤으로 진행합니다."
        jump day_action_pick_map
    else:
        $ renpy.jump(MAPS[nid]["label"])

label day_action_pick_map:
    $ opts = pick_random_maps(3)
    if not opts:
        n "진행할 수 있는 맵이 없습니다. 하루를 쉽니다."
        $ gst.day += 1
        jump day_loop

    call screen map_picker(opts)
    $ sel = _return

    if sel == "SKIP" or sel is None:
        n "오늘은 아무것도 하지 않고 쉬었다."
        $ gst.day += 1
        jump day_loop
    else:
        $ renpy.jump(sel["label"])

label day_action_alba:
    jump alba_scene

label day_action_betting:
    jump horse_bet_quick
