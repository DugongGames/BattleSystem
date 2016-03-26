
class MagicAbility(object):

    def __init__(self, magic_type, base_damage):
        self.magic_type = magic_type
        self.base_damage = base_damage


class MagicType(object):
    ICE = "ICE"
    FIRE = "FIRE"
    WATER = "WATER"
    EARTH = "EARTH"
