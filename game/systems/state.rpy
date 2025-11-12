# 상태/유틸 (가급적 가장 먼저 초기화)
init -1 python:
    class GST(object):
        def __init__(self):
            self.day = 1
            self.money = 5000
            self.aff = 0
            self.known_prefs = {}
            self.route_flags = {}

    def add_money(v):
        gst.money = max(0, gst.money + v)

    def add_aff(v):
        gst.aff = max(0, min(100, gst.aff + v))

    def unlock_scene(sid):
        persistent.codex.add(sid)

    def set_pref(key, value):
        gst.known_prefs[key] = value

    def knows_pref(key, val):
        return gst.known_prefs.get(key) == val

default gst = GST()
default persistent.codex = set()
default persistent.seen_intro = False
default persistent.seen_epilogue = False
default persistent.maps_seen = set()
