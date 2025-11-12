init python:
    def apply_preference_bonus(keyword):
        if gst.known_prefs.get(keyword):
            add_affection(3)

    def register_preference(keyword):
        gst.known_prefs[keyword] = True
