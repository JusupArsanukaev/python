import random

def start_game():
    print("Добро пожаловать в Подземелье!")
    player_health = 100
    monster_health = random.randint(50, 100)
    player_action(player_health, monster_health)

def player_action(player_health, monster_health):
    action = random.choice(['attack', 'heal'])
    
    if action == 'attack':
        damage = random.randint(10, 30)
        monster_health -= damage
        print(f"Вы атакуете монстра и наносите {damage} урона!")
    else:
        heal = random.randint(5, 20)
        player_health += heal
        print(f"Вы лечите себя на {heal} здоровья!")

    if monster_health > 0:
        monster_attack = random.randint(5, 15)
        player_health -= monster_attack
        print(f"Монстр атакует вас и наносит {monster_attack} урона!")

    game_status(player_health, monster_health)

def game_status(player_health, monster_health):
    print(f"Ваше здоровье: {player_health}, здоровье монстра: {monster_health}")

    if player_health <= 0:
        print("Вы погибли! Игра окончена.")
    elif monster_health <= 0:
        print("Вы победили монстра! Поздравляем!")
    else:
        player_action(player_health, monster_health)

start_game()
