# 맵 001 등록
init python:
    register_map("001", desc="카페 첫 만남")

label map_001:
    n "[MAPS['001']['desc']]"
    $ mark_map_finished("001")
    jump day_loop
