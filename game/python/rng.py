import random

def horse_bet(bet_amount, tier):
    """
    tier: 'small'|'med'|'large'
    return: (result_str, delta_money)
    """
    cfg = {
        "small": {"win": 0.55, "draw": 0.10, "mul": 1.5},
        "med":   {"win": 0.40, "draw": 0.08, "mul": 2.5},
        "large": {"win": 0.22, "draw": 0.05, "mul": 4.0},
    }
    # .get()을 사용하여 안전하게 값을 가져오고, 없는 경우 기본값을 설정합니다.
    tier_cfg = cfg.get(tier)
    if not tier_cfg:
        # 잘못된 tier 값이 들어올 경우, 기본값으로 'small'을 사용하거나 에러 처리를 할 수 있습니다.
        # 여기서는 'small'로 처리하여 안정성을 높입니다.
        tier_cfg = cfg['small']

    r = random.random()
    if r < tier_cfg["win"]:
        return "win", int(bet_amount * tier_cfg["mul"])
    elif r < tier_cfg["win"] + tier_cfg["draw"]:
        return "draw", bet_amount
    return "lose", 0
