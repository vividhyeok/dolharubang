init -1 python:
    # 숫자 id -> 메타 정보
    MAPS = {}

    # 처음 본 맵 추적 (도감/재방문 구분)
    if not hasattr(persistent, "maps_seen"):
        persistent.maps_seen = set()

    def register_map(id, desc="", weight=1, label=None):
        """
        register_map("001", desc="카페 첫 만남")
        기본 라벨 규칙: map_<id>
        """
        if label is None:
            label = f"map_{id}"
        MAPS[id] = dict(id=id, label=label, desc=desc, weight=int(weight))

    def mark_map_finished(id):
        persistent.maps_seen.add(id)
        gst.day += 1

    def get_next_unseen_map_id():
        unseen = [i for i in MAPS.keys() if i not in persistent.maps_seen]
        if not unseen:
            return None
        # 숫자 기준 오름차순
        return sorted(unseen, key=lambda x: int(x))[0]

    def pick_random_maps(n=3, prefer_unseen=True):
        """
        오늘 후보 맵 n개 선택. 미해금 맵 가중치 ↑ 옵션.
        반환: [{id, label, desc, weight}, ...]
        """
        import random
        items = list(MAPS.values())
        if not items:
            return []

        # 가중치 풀 구성
        pool = []
        for m in items:
            w = m["weight"]
            if prefer_unseen and (m["id"] not in persistent.maps_seen):
                w *= 2
            pool.append((m, w))

        result = []
        temp = pool[:]
        for _ in range(min(n, len(temp))):
            total = sum(w for _, w in temp)
            r = random.uniform(0, total)
            acc = 0.0
            choice = temp[0][0]
            for m, w in temp:
                acc += w
                if r <= acc:
                    choice = m
                    break
            result.append(choice)
            temp = [x for x in temp if x[0]["id"] != choice["id"]]
        return result
