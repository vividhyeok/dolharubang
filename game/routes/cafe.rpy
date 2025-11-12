# 아르바이트 장면
label alba_scene:
    scene black with fade
    n "오늘은 알바를 했다. 시간은 빠르게 굳어갔다."
    $ gst.add_money(3000)
    n "₩3,000을 벌었다."
    $ gst.day += 1
    jump day_loop
