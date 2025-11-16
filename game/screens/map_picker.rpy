default persistent.maps_seen = set()

screen map_picker(options):
    tag menu
    modal True
    frame:
        align (0.5, 0.5)
        padding (24, 18)
        vbox:
            spacing 14
            text "오늘의 맵 선택" size 42
            if not options:
                text "등록된 맵이 없습니다." size 28
                textbutton "닫기" action Return(None)
            else:
                for m in options:
                    $ is_new = (m['id'] not in persistent.maps_seen)
                    $ txt = "[m['id']]  " + (m["desc"] or m["label"]) # + (" (NEW)" if is_new else "")
                    textbutton txt action Return(m)
                null height 12
                textbutton "오늘은 패스" action Return("SKIP")