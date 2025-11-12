# 맵 001 등록
init python:
    register_map("001", desc="카페 첫 만남")

label map_001:
    n "[MAPS['001']['desc']]"
    n "여기에 001 장면 내용을 씁니다."
    $ mark_map_finished("001")
    $ gst.day += 1
    jump day_loop
