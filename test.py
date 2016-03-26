
from Weapon import Weapon
from Player import Player
from BattleManager import BattleManager, battleQueue


def main():
    player = Player("Ryu", 100, 10, 5, 5, 5, Weapon("Claymore", 10, ("str", 2)))
    player2 = Player("Nina", 100, 10, 5, 5, 5, Weapon("Mace", 5, ("int", 2)))

    battle_manager = BattleManager([player, player2])

    print("Battle Started!")
    while battleQueue.qsize() > 1:
        battle_manager.run()


    # print(player.get_player_health())
    # print(player.get_player_magic())
    # print(player.get_player_strength())
    # print(player.get_player_intelligence())
    # print(player.get_player_speed())
    #
    # player.equip_weapon(Weapon("Masamune", 50, ("str", 100)))
    # print(player.get_player_strength())
    # print(player.get_player_weapon_attack_damage())
    # player.equip_weapon(Weapon("Murasame", 70, ("str", 220)))
    # print(player.get_player_strength())
    # print(player.get_player_weapon_attack_damage())

if __name__=="__main__":
    main()
