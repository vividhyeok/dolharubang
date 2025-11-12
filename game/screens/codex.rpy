screen codex():
    tag menu
    use game_menu("Codex"):
        vbox:
            spacing 12
            text "Unlocked Entries" style "label_text"
            if persistent.codex:
                for entry in sorted(persistent.codex):
                    text entry
            else:
                text "아직 해금된 기록이 없습니다."
