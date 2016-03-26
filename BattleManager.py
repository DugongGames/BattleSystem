import threading
import queue
import time
from Player import PlayerState

battleQueue = queue.Queue()


class BattleManager(threading.Thread):

    def __init__(self, entity_list):
        self.entity_list = entity_list
        self.battle_queue_order = sorted(entity_list, key=lambda x: -x.get_player_speed())
        [battleQueue.put(x) for x in self.battle_queue_order]

    def run(self):
        current_player = battleQueue.get()
        current_player.state = PlayerState.NORMAL
        opponent_player = battleQueue.get()
        print(current_player.get_player_name() + "'s  turn!")
        print("Your Opponent... ")
        print(opponent_player.print_stats())
        user_input = input(current_player.print_actions())
        print()

        if user_input == "1":
            damage = current_player.get_player_weapon_attack_damage()
            damage = damage if opponent_player.state == PlayerState.NORMAL else damage/2
            print("DAMAGE: " + str(damage))
            opponent_player.set_player_health(opponent_player.get_player_health() - damage)
        elif user_input == "2":
            current_player.state = PlayerState.DEFENDING

        print("Turn over: Current Stats: ")
        print(current_player.print_stats())
        print(opponent_player.print_stats())

        battleQueue.put(opponent_player)
        battleQueue.put(current_player)

