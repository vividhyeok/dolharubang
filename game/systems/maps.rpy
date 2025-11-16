init -1 python:
    import random

    # 숫자 id -> 메타 정보
    MAPS = {}

    # 고정된 이진 트리 형태의 맵 진행표
    MAP_TREE = {
        "001": ("002", "003"),
        "002": ("004", "005"),
        "003": ("006", "007"),
    }

    def register_map(id, desc="", weight=1, label=None):
        """
        register_map("001", desc="카페 첫 만남")
        기본 라벨 규칙: map_<id>
        """
        if label is None:
            label = f"map_{id}"
        MAPS[id] = dict(id=id, label=label, desc=desc, weight=int(weight))

    def mark_map_finished(id):
        gst.last_map_id = id
        gst.day += 1

    def set_next_map_from_choice(current_id, branch_index):
        """현재 맵에서 고른 선택지(branch_index)가 향할 다음 맵을 예약."""
        children = MAP_TREE.get(current_id)
        if not children or branch_index >= len(children):
            gst.next_map_id = None
            return
        gst.next_map_id = children[branch_index]

    def randomize_next_branch():
        """데이트를 건너뛸 때 다음 분기 중 하나를 무작위로 선택."""
        if gst.next_map_id is None:
            return
        children = MAP_TREE.get(gst.next_map_id)
        if not children:
            gst.next_map_id = None
            return
        gst.next_map_id = random.choice(children)
