
from Statistics import Statistics
from Weapon import Weapon


class PlayerState(object):
    NORMAL = 'NORMAL'
    DEFENDING = 'DEFENDING'

class Player(object):

    def __init__(self, player_name, player_health, player_magic_points, player_speed, player_strength,
                 player_intelligence, player_weapon):

        self.player_name = player_name

        self.statistics = Statistics(player_health, player_magic_points, player_strength, player_speed,
                                     player_intelligence)

        self.state = PlayerState.NORMAL

        self.weapon = player_weapon

        self.stat_map = {
            "str": self.set_player_strength,
            "mp": self.set_player_magic,
            "spd": self.set_player_speed,
            "int": self.set_player_int,
            "hp": self.set_player_health
        }

        self.apply_modifier("apply")

    def print_actions(self):
        action_string = self.player_name + "'s Command List: \n"
        action_string += "1: Attack\n"
        action_string += "2: Defend\n"
        return action_string

    def print_stats(self):
        stat_string = "-------------------------------\n"
        stat_string += self.player_name + "'s Status: \n"
        stat_string += "HP: " + str(self.get_player_health()) + "\n"
        stat_string += "MP: " + str(self.get_player_magic()) + "\n"
        stat_string += "Str: " + str(self.get_player_strength()) + "\n"
        stat_string += "Spd: " + str(self.get_player_speed()) + "\n"
        stat_string += "Int: " + str(self.get_player_intelligence()) + "\n"
        stat_string += "-------------------------------\n"
        return stat_string

    def apply_modifier(self, apply_or_remove):
        if apply_or_remove is "apply":
            if self.weapon.get_weapon_modifier()[0] in self.stat_map:
                self.stat_map[self.weapon.get_weapon_modifier()[0]](self.weapon.get_weapon_modifier()[1])
        else:
            if self.weapon.get_weapon_modifier()[0] in self.stat_map:
                self.stat_map[self.weapon.get_weapon_modifier()[0]](-(self.weapon.get_weapon_modifier()[1]))

    def equip_weapon(self, weapon):
        self.apply_modifier("remove")
        self.weapon = weapon
        self.apply_modifier("apply")

    # Getters
    def get_player_name(self):
        return self.player_name

    def get_player_health(self):
        return self.statistics.get_health_points()

    def get_player_magic(self):
        return self.statistics.get_magic_points()

    def get_player_strength(self):
        return self.statistics.get_strength_points()

    def get_player_speed(self):
        return self.statistics.get_speed_points()

    def get_player_intelligence(self):
        return self.statistics.get_intelligence_points()

    def get_player_weapon_attack_damage(self):
        return self.get_player_strength() + self.weapon.get_weapon_attack_damage()

    # Setters
    def set_player_health(self, player_health):
        self.statistics.set_health_points(player_health)

    def set_player_magic(self, player_magic):
        self.statistics.set_magic_points(player_magic)

    def set_player_strength(self, player_strength):
        self.statistics.set_strength_points(player_strength)

    def set_player_speed(self, player_speed):
        self.statistics.set_speed_points(player_speed)

    def set_player_int(self, player_int):
        self.statistics.set_intelligence_points(player_int)
