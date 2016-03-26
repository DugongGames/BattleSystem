
class Weapon(object):

    def __init__(self, weapon_name, weapon_attack_damage, weapon_modifier):
        self.weapon_name = weapon_name
        self.weapon_attack_damage = weapon_attack_damage
        self.weapon_modifier = weapon_modifier

    def get_weapon_name(self):
        return self.weapon_name

    def get_weapon_attack_damage(self):
        return self.weapon_attack_damage

    def get_weapon_modifier(self):
        return self.weapon_modifier
