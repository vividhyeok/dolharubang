# 상태/유틸 (가급적 가장 먼저 초기화)
init -1 python:
    class GST(object):
        def __init__(self):
            self.day = 1
            self.money = 5000
            self.aff = 0
            self.known_prefs = {}
            self.route_flags = {}
            self.last_map_id = None

        def add_money(self, v):
            self.money = max(0, self.money + v)

        def add_aff(self, v):
            self.aff = max(0, min(100, self.aff + v))

        def can_pay(self, cost):
            return self.money >= cost

        def pay(self, cost):
            if self.can_pay(cost):
                self.money -= cost
                return True
            return False

        def set_pref(self, key, value):
            self.known_prefs[key] = value

        def knows_pref(self, key, val):
            return self.known_prefs.get(key) == val

    def unlock_scene(sid):
        persistent.codex.add(sid)

default gst = GST()
default persistent.codex = set()
default persistent.seen_intro = False
default persistent.seen_epilogue = False
default persistent.maps_seen = set()
