init -1 python:
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

    def get_next_map_choices():
        """현재까지 진행 상황을 바탕으로 다음에 선택할 수 있는 맵 목록을 반환."""
        if gst.last_map_id is None:
            return [MAPS["001"]] if "001" in MAPS else []

        children = MAP_TREE.get(gst.last_map_id, tuple())
        return [MAPS[c] for c in children if c in MAPS]
