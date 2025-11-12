# 돈/결제 공통
init python:
    def can_pay(cost):
        return gst.money >= cost

    def pay(cost):
        if can_pay(cost):
            gst.money -= cost
            return True
        return False
