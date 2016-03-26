from common.character import Character
from common.core.BattleManager import BattleManager, battleQueue
from common.items.Weapon import Weapon


def main():
    player = Character("Ryu", 100, 10, 5, 5, 5, Weapon("Claymore", 10, ("str", 2)))
    player2 = Character("Nina", 100, 10, 5, 5, 5, Weapon("Mace", 5, ("int", 2)))

    battle_manager = BattleManager([player, player2])

    print("Battle Started!")
    while battleQueue.qsize() > 1:
        battle_manager.run()

    winner = battleQueue.get()
    print("Winner! : " + winner.get_player_name())

    # print(character.get_player_health())
    # print(character.get_player_magic())
    # print(character.get_player_strength())
    # print(character.get_player_intelligence())
    # print(character.get_player_speed())
    #
    # character.equip_weapon(Weapon("Masamune", 50, ("str", 100)))
    # print(character.get_player_strength())
    # print(character.get_player_weapon_attack_damage())
    # character.equip_weapon(Weapon("Murasame", 70, ("str", 220)))
    # print(character.get_player_strength())
    # print(character.get_player_weapon_attack_damage())

if __name__=="__main__":
    main()
