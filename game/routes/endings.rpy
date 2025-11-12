label ending_check:
    if gst.aff >= 90:
        jump ending_true
    elif gst.aff <= 10:
        jump ending_meme
    jump ending_normal

label ending_true:
    hide screen hud
    scene black with fade
    n "우리는 오래 함께했고, 아이가 여럿 생겼다. — TRUE END —"
    n "(엔터를 눌러 타이틀로 돌아갑니다)"
    return

label ending_meme:
    hide screen hud
    scene black with fade
    n "슈슉슈슈슉… 화면을 가득 채운 밈. — MEME END —"
    n "(엔터를 눌러 타이틀로 돌아갑니다)"
    return

label ending_normal:
    hide screen hud
    scene black with fade
    n "사랑은 아직 표면을 맴돈다. 더 많은 날이 필요하다. — NORMAL END —"
    n "(엔터를 눌러 타이틀로 돌아갑니다)"
    return
