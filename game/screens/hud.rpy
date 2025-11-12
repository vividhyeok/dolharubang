# 상단 HUD
screen hud():
    zorder 99
    frame:
        align (0.99, 0.02)
        padding (10, 8)
        background None
        vbox:
            spacing 8
            text "Day: [gst.day]"
            text "₩[gst.money]"
            text "♥ [gst.aff]"
