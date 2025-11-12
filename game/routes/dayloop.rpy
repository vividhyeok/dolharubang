# 캐릭터 & 진입/메인루프
define p = Character("나", color="#c8ffc8")
define d = Character("돌하르방", color="#c8c8ff")
define n = Character(None)

default persistent.seen_epilogue = False

label splashscreen:
    # 첫 실행: 에필로그(프롤로그 느낌) -> 기존 prologue -> 메인 루프
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
    # 에필로그 후 기존 프롤로그(힌트 설정 등)로 진입
    jump prologue

label prologue:
    scene black with fade
    window show
    n "제주대 과팅은 시끄러웠다."
    n "그리고— 석상이 의자에 앉아 있었다. 모두는 웃었다."
    n "아무도 이상해하지 않았다. 그래서 이상했다. 나만."
    # 힌트 한두 개 살짝
    $ set_pref("감귤주스","dislike")
    $ set_pref("삼다수","dislike")
    jump day_loop

label day_loop:
    show screen hud
    if gst.day > 7:     # 엔딩 체험 임계치, 원하면 늘리세요
        jump ending_check

    n "Day [gst.day]. 오늘은 무엇을 할까?"
    menu:
        "다음 번호 맵 자동 진행":
            $ nid = get_next_unseen_map_id()
            if nid is None:
                n "새로운 맵이 없습니다. 랜덤으로 진행합니다."
                $ opts = pick_random_maps(1)
                if not opts:
                    $ gst.day += 1
                    jump day_loop
                $ renpy.jump(opts[0]["label"])
            else:
                $ renpy.jump(MAPS[nid]["label"])

        "랜덤 후보 3개 중 고르기":
            $ opts = pick_random_maps(3)
            call screen map_picker(opts)
            $ sel = _return
            if sel == "SKIP" or sel is None:
                $ gst.day += 1
                jump day_loop
            else:
                $ renpy.jump(sel["label"])

        "아르바이트를 한다 (돈 +, 오늘 스토리 스킵)":
            call alba_scene
            $ gst.day += 1
            jump day_loop

        "경마공원에서 베팅한다 (결과만 보고 다음 날)":
            jump horse_bet_quick
