

class Statistics(object):

    def __init__(self, health_points, magic_points, strength_points, speed_points, intelligence_points):
        self.health_points = health_points
        self.magic_points = magic_points
        self.strength_points = strength_points
        self.speed_points = speed_points
        self.intelligence_points = intelligence_points

    def get_health_points(self):
        return self.health_points

    def get_magic_points(self):
        return self.magic_points

    def get_strength_points(self):
        return self.strength_points

    def get_speed_points(self):
        return self.speed_points

    def get_intelligence_points(self):
        return self.intelligence_points

    def set_health_points(self, health_points):
        self.health_points = health_points

    def set_magic_points(self, magic_points):
        self.magic_points += magic_points

    def set_strength_points(self, strength_points):
        self.strength_points += strength_points

    def set_speed_points(self, speed_points):
        self.speed_points += speed_points

    def set_intelligence_points(self, int_points):
        self.intelligence_points += int_points
