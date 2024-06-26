from time import *
from random import *

stat_move = 'stat move'
normal_move = 'normal move'
gamemode = 0
in_gamemode_4 = False
gamemode_4_player = 0
move_type = normal_move
hp = [0, 100, 100]
oppo_hp = 100
strength = [0, 1, 1]
crit_chance = [0, 10, 10]
crit_damage = [0, 3, 3]
double_hit = 20
burning_time = [0, 0, 0]
damage = [0, 0, 0]
defense = [0, 1, 1]
characters = ['', '', '']
p1_moves = ['', '', '', '', '']
p2_moves = ['', '', '', '', '']
moves = ['', p1_moves, p2_moves]
soul = [0, 0, 0]
oppo_turn = 1
resurrect_time = [0, 1, 1]
cc_random = 0
choose_characters = 'a'
stun_random = 100
black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
orange = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
gray = '\033[37m'
white = '\033[38m'
reset = '\033[39m\033[0m'
bold = '\033[1m'
italic = '\033[3m'
underline = '\033[4m'


def character_choice():
    print(bold + underline + f'Player {turn}:' + reset)
    print('What character would you like to select')
    print('[1] Korma        [5] Splitzo')
    print('[2] Zenith       [6] Claec')
    print('[3] Galen        [7] Krysta')
    print('[4] Sharpshot    [r] random\n')


def moves_choice():
    print(bold + underline + f'\nPlayer {turn}:' + reset)

    int(hp[turn])
    print('What move would you like to do:            ' + green + 'HP:', int(hp[turn]), purple + '  CC:', str(crit_chance[turn] + cc_random) + reset)
    print("[1]", moves[turn][1])
    print("[2]", moves[turn][2])
    print("[3]", moves[turn][3])
    print("[4]", moves[turn][4])
    print('')


def oppositing_turn():
    global oppo_turn, oppo_hp
    if turn == 1:
        oppo_turn = 2
        oppo_hp = hp[2]
    if turn == 2:
        oppo_turn = 1
        oppo_hp = hp[1]


def set_character():
    global characters
    global moves
    global choose_characters
    global gamemode
    global luck
    if not in_gamemode_4:
        if choose_characters != 'r':
            character_choice()
    else:
        choose_characters = 'r'
    if choose_characters != 'r':
        choose_characters = 0
    while True:
        if choose_characters != 'r':
            if int(choose_characters) > 7 or int(choose_characters) < 1:
                choose_characters = input()

        if choose_characters == 'r':
            if not in_gamemode_4:
                print('You have selected random')
                sleep(2)
            choose_characters = randint(1, 7)
            continue

        elif choose_characters == 'summon TSJ':
            characters[turn] = 'Teacher Saijai'
            print('You have summoned TSJ!!!')
            sleep(2)
            print('The world SHALL PERISH IN HER HANDS')
            sleep(2)
            moves[turn][1] = 'Emotional damage'
            moves[turn][2] = 'Spare life'
            moves[turn][3] = 'Spare life'
            moves[turn][4] = 'Give homework'
            choose_characters = 1

        elif int(choose_characters) == 1:
            characters[turn] = 'Korma'
            if not in_gamemode_4:
                print('You have selected', bold + red + characters[turn] + reset)
                print('')
                sleep(2)
            moves[turn][1] = 'Hellish slash'
            moves[turn][2] = 'Hellish fire'
            moves[turn][3] = 'Sins redemption'
            moves[turn][4] = "Devil's Wrath"

        elif int(choose_characters) == 2:
            characters[turn] = 'Zenith'
            if not in_gamemode_4:
                print('You have selected', bold + yellow + characters[turn] + reset)
                print('')
                sleep(2)
            moves[turn][1] = 'Zap'
            moves[turn][2] = 'Strategize'
            moves[turn][3] = 'Knowledge'
            moves[turn][4] = 'Checkmate'

        elif int(choose_characters) == 3:
            characters[turn] = 'Galen'
            if not in_gamemode_4:
                print('You have selected', bold + characters[turn] + reset)
                print('')
                sleep(2)
            moves[turn][1] = 'Teachings'
            moves[turn][2] = "God's blessing"
            moves[turn][3] = 'Blessed'
            moves[turn][4] = 'Resurrect'

        elif int(choose_characters) == 4:
            characters[turn] = 'Sharpshot'
            if not in_gamemode_4:
                print('You have selected', characters[turn])
                print('')
                sleep(2)
            moves[turn][1] = 'Bang'
            moves[turn][2] = 'Headshot'
            moves[turn][3] = 'Bandage'
            moves[turn][4] = 'Take cover'

        elif int(choose_characters) == 5:
            characters[turn] = 'Splitzo'
            if not in_gamemode_4:
                print('You have selected', bold + orange + characters[turn] + reset)
                print('')
                sleep(2)
                characters[turn] = 'Sovary'
                moves[turn][1] = 'Slice'
                moves[turn][2] = 'Spice'
                moves[turn][3] = 'Flying croissant'
                moves[turn][4] = 'Switch'
            else:
                luck = randint(1, 2)
                if luck == 1:
                    characters[turn] = 'Sovary'
                    moves[turn][1] = 'Slice'
                    moves[turn][2] = 'Spice'
                    moves[turn][3] = 'Flying croissant'
                    moves[turn][4] = 'Switch'
                if luck == 2:
                    characters[turn] = 'Swete'
                    moves[turn][1] = 'Coffee cake'
                    moves[turn][2] = 'Nutritious carrot'
                    moves[turn][3] = 'Delightful smoothie'
                    moves[turn][4] = 'Switch'

        elif int(choose_characters) == 6:
            characters[turn] = 'Claec'
            if not in_gamemode_4:
                print('You have selected', bold + purple + characters[turn] + reset)
                print('')
                sleep(2)
            moves[turn][1] = 'Gather'
            moves[turn][2] = 'Enhanced soul'
            moves[turn][3] = 'Sacrificing soul'
            moves[turn][4] = 'Soul unleash'

        elif int(choose_characters) == 7:
            characters[turn] = 'Krysta'
            if not in_gamemode_4:
                print('You have selected', bold + cyan + characters[turn] + reset)
                print('')
                sleep(2)
            moves[turn][1] = 'Agonizing amethyst'
            moves[turn][2] = 'Internal refraction'
            moves[turn][3] = 'Ruby of radiance'
            moves[turn][4] = 'Crystal clear'

        else:
            print('That is not a valid choice, please choose the character again\n')
            continue

        if choose_characters == 'summon TSJ' or 1 <= int(choose_characters) <= 7:
            break


def action():
    global characters
    global damage
    global moves
    global hp
    global burning_time
    global double_hit
    global crit_chance
    global crit_damage
    global strength
    global move_type
    global luck
    global soul
    global resurrect_time
    global stun_random

    # Korma movesets
    if characters[turn] == 'Korma':
        if choose_moves == 1:
            damage[turn] = 10
            burning_time[turn] += 1
            move_type = normal_move
        if choose_moves == 2:
            damage[turn] = 5
            burning_time[turn] += 5
            move_type = normal_move
        if choose_moves == 3:
            damage[turn] = 0
            hp[turn] += 5
            if hp[turn] > 100:
                hp[turn] = 100
            move_type = stat_move
            print('Player', turn, 'HP has risen by 5')
        if choose_moves == 4:
            damage[turn] = 0
            strength[turn] += 0.2
            print('Player', turn, 'has risen strength by 20%')
            move_type = stat_move

    # Zenith movesets
    if characters[turn] == 'Zenith':
        if choose_moves == 1:
            damage[turn] = 7
            double_hit = 70
            move_type = normal_move
        if choose_moves == 2:
            crit_chance[turn] += 10
            damage[turn] = 0
            move_type = stat_move
            print('Player', turn, 'has risen critical hit chance by 10%')
        if choose_moves == 3:
            damage[turn] = 10
            move_type = normal_move
        if choose_moves == 4:
            if 35 <= oppo_hp <= 40:
                print('Player', oppo_turn, 'has the perfect amount of HP to get checkmated')
                sleep(0.5)
                print('Player', oppo_turn, 'got checkmated!!')
                sleep(2)
                damage[turn] = oppo_hp
            else:
                print('Move failed')
                sleep(1)
                print("Player", oppo_turn, "doesn't have the right circumstance to get checkmated")
                sleep(1)
                damage[turn] = 0
            move_type = stat_move

    # Galen movesets
    if characters[turn] == 'Galen':
        if choose_moves == 1:
            damage[turn] = 10
            move_type = normal_move
        if choose_moves == 2:
            damage[turn] = 0
            crit_chance[turn] += 5
            print('Player', turn, 'has risen critical hit chance by 5%')
            move_type = stat_move
        if choose_moves == 3:
            damage[turn] = 0
            hp[turn] += 15
            if hp[turn] > 100:
                hp[turn] = 100
            print('Player', turn, 'has heal ' + cyan + '15 HP' + reset)
            move_type = stat_move
        if choose_moves == 4:
            damage[turn] = 0
            if hp[turn] <= 20:
                if resurrect_time[turn] > 0:
                    hp[turn] = hp[turn] + 75
                    print('Player', turn, 'has heal ' + bold + cyan + '75 HP' + reset)
                    resurrect_time[turn] -= 1
                    print('Player', turn, 'now has', resurrect_time[turn], 'chances of resurrecting again')
                else:
                    print('Player', turn, 'has already resurrected and cannot be used again')
            else:
                print('Player', turn, "doesn't have the right circumstance to use resurrect")
            move_type = stat_move

    # Sharpshot movesets
    if characters[turn] == 'Sharpshot':
        if choose_moves == 1:
            damage[turn] = 10
            crit_chance[turn] += 5
            move_type = normal_move
        if choose_moves == 2:
            damage[turn] = 5
            crit_chance[turn] += 10
            print('Player', turn, 'has risen critical hit chance by 10%')
            move_type = normal_move
        if choose_moves == 3:
            damage[turn] = 0
            hp[turn] += 7
            if hp[turn] > 100:
                hp[turn] = 100
            print('Player', turn, 'has heal ' + cyan + '7 HP' + reset)
            move_type = stat_move
        if choose_moves == 4:
            if hp[turn] <= 15:
                damage[turn] = 40
                move_type = normal_move
            else:
                damage[turn] = 0
                print('Move failed')
                sleep(1)
                print('Player', turn, 'HP is not low enough to use this move')
                sleep(1)
                move_type = stat_move

    # Splitzo movesets
    # Sovary movesets
    if characters[turn] == 'Sovary':
        if choose_moves == 1:
            damage[turn] = 10
            move_type = normal_move
        if choose_moves == 2:
            damage[turn] = 2
            burning_time[turn] = 5
            move_type = normal_move
        if choose_moves == 3:
            damage[turn] = 7
            double_hit = 60
            move_type = normal_move
        if choose_moves == 4:
            damage[turn] = 0
            characters[turn] = 'Swete'
            moves[turn][1] = 'Coffee cake'
            moves[turn][2] = 'Nutritious carrot'
            moves[turn][3] = 'Delightful smoothie'
            print('Swete has taken over the body!!')
            move_type = stat_move

    # Swete movesets
    elif characters[turn] == 'Swete':
        damage[turn] = 0
        move_type = stat_move
        if choose_moves == 1:
            strength[turn] += 0.5
            print('Player', turn, 'has risen strength by 50%')
        if choose_moves == 2:
            crit_chance[turn] += 7
            print('Player', turn, 'has risen critical hit chance by 7%')
        if choose_moves == 3:
            hp[turn] += 10
            if hp[turn] > 100:
                hp[turn] = 100
            print('Player', turn, 'has heal ' + cyan + '10 HP' + reset)
        if choose_moves == 4:
            characters[turn] = 'Sovary'
            moves[turn][1] = 'Slice'
            moves[turn][2] = 'Spice'
            moves[turn][3] = 'Flying croissant'
            print('Sovary has taken over the body!!')

    # Claec movesets
    elif characters[turn] == 'Claec':
        if choose_moves == 1:
            damage[turn] = 0
            soul[turn] += 1
            luck = randint(1, 10)
            if luck <= 3:
                soul[turn] += 1
                print('Player', turn, 'got lucky and has gathered ' + purple + '2 souls' + reset)
            else:
                print('Player', turn, 'has gathered ' + purple + '1 soul' + reset)
            sleep(1)
            if soul[turn] == 1:
                print('Player', turn, 'now has' + purple, soul[turn], 'soul' + reset)
            if soul[turn] > 1:
                print('Player', turn, 'now has' + purple, soul[turn], 'souls' + reset)
            move_type = stat_move
        if choose_moves == 2:
            damage[turn] = 0
            strength[turn] += 0.1
            print('Player', turn, 'has risen the strength of the souls by 10%')
            move_type = stat_move
        if choose_moves == 3:
            damage[turn] = 0
            if soul[turn] > 0:
                hp[turn] += 12
                if hp[turn] > 100:
                    hp[turn] = 100
                print('Player', turn, 'has sacrificed 1 soul and healed ' + cyan + '12 HP' + reset)
                soul[turn] -= 1
            else:
                print('Player', turn, "doesn't have enough souls to heal")
            move_type = stat_move
        if choose_moves == 4:
            if soul[turn] <= 3:
                damage[turn] = soul[turn] * 11
            if 4 <= soul[turn] <= 6:
                damage[turn] = soul[turn] * 12
            if soul[turn] >= 7:
                damage[turn] = soul[turn] * 13
            move_type = normal_move
            print('Player', turn, 'has unleashed' + purple + bold, soul[turn], 'soul' + reset)
            soul[turn] = 0
            if strength[turn] > 1:
                strength[turn] = 1
                sleep(1)
                print("Player", turn, "soul's will now have the normal amount of strength")
                sleep(1)

    # Krysta movesets
    if characters[turn] == 'Krysta':
        if choose_moves == 1:
            damage[turn] = 6
            double_hit = 70
            move_type = normal_move
        if choose_moves == 2:
            damage[turn] = 0
            crit_chance[turn] += 10
            print('Player', turn, 'has risen critical hit chance by 10%')
            move_type = stat_move
        if choose_moves == 3:
            damage[turn] = 0
            hp[turn] += 3
            if hp[turn] > 100:
                hp[turn] = 100
            move_type = stat_move
            print('Player', turn, 'HP has risen by 3')
        if choose_moves == 4:
            stun_random = randint(1, 100) + (crit_chance[turn]/2)
            if stun_random <= 40:
                damage[turn] = 5
                print('Her opponent is stunned!!')
                move_type = normal_move
            else:
                damage[turn] = 0
                hp[turn] -= 5
                print('Krysta took 5 damage from her own attack')
                move_type = stat_move

    # TSJ movesets
    elif characters[turn] == 'Teacher Saijai':
        hp[turn] = 100000
        crit_damage[turn] = 1000
        crit_chance[turn] = 300
        double_hit = 200
        move_type = stat_move
        if choose_moves == 1:
            damage[turn] = 99
        if choose_moves == 2:
            damage[turn] = 0
            print('TSJ has spared your life')
        if choose_moves == 3:
            damage[turn] = 0
            print('TSJ has spared your life')
        if choose_moves == 4:
            strength[turn] = 1000
            damage[turn] = 1000
            move_type = normal_move

    damage[turn] *= strength[turn]


def bot_turn():
    global characters
    global damage
    global hp, oppo_hp
    global burning_time
    global double_hit
    global crit_chance
    global strength
    global defense
    global move_type
    global luck
    global soul
    global choose_moves
    global resurrect_time

    while True:

        # Korma bot
        if characters[turn] == 'Korma':
            choose_moves = randint(1, 4)
            if choose_moves == 2:
                if burning_time[turn] == 0:
                    break
            elif choose_moves == 3:
                if hp[turn] <= 95:
                    break
            elif oppo_hp < 20:
                choose_moves = 1
                break
            else:
                break

        # Zenith bot
        if characters[turn] == 'Zenith':
            choose_moves = randint(1, 3)
            if 35 <= oppo_hp <= 40:
                choose_moves = 4
                break
            elif oppo_hp < 20:
                choose_moves = 1
            else:
                break

        # Galen bot
        if characters[turn] == 'Galen':
            choose_moves = randint(1, 3)
            if hp[turn] <= 20:
                if resurrect_time[turn] > 0:
                    choose_moves = 4
                    break
            if choose_moves == 3:
                if hp[turn] <= 80:
                    break
            elif oppo_hp < 20:
                choose_moves = 1
                break
            else:
                break

        # Sharpshot bot
        if characters[turn] == 'Sharpshot':
            choose_moves = randint(1, 3)
            if choose_moves == 3:
                if hp[turn] <= 93:
                    break
            elif hp[turn] <= 15:
                choose_moves = 4
                break
            else:
                break

        # Sovary bot
        if characters[turn] == 'Sovary':
            choose_moves = randint(1, 4)
            if choose_moves == 2:
                if burning_time[turn] <= 0:
                    break
            else:
                break

        # Swete bot
        if characters[turn] == 'Swete':
            choose_moves = randint(1, 4)
            if choose_moves == 3:
                if hp[turn] <= 90:
                    break
            else:
                break

        # Claec bot
        if characters[turn] == 'Claec':
            choose_moves = randint(1, 2)
            luck = randint(1, 10)
            if luck == 1:
                if soul[turn] > 0:
                    choose_moves = 3
                    break
            elif choose_moves == 2:
                if luck >= 3:
                    choose_moves = 2
                else:
                    choose_moves = 1
            elif soul[turn] >= 5:
                choose_moves = 4
                break
            else:
                break

        # Krysta bot
        if characters[turn] == 'Krysta':
            choose_moves = randint(1, 4)
            if choose_moves == 3:
                if hp[turn] <= 97:
                    break
            elif oppo_hp <= 12:
                choose_moves = 1
                break
            else:
                break

        # TSJ bot
        if characters[turn] == 'Teacher Saijai':
            if oppo_hp == 100:
                choose_moves = 1
                break
            else:
                choose_moves = 4
                break


# In the game
print('What mode would you like to select?')
print('[1] Single player')
print('[2] Multiplayer')
print('[3] Sandbag mode')
print('[4] Randomizer mode')
print('')
while True:
    gamemode = int(input())
    if gamemode == 1:
        print('You have selected single player')
        break
    elif gamemode == 2:
        print('You have selected multiplayer')
        break
    elif gamemode == 3:
        print('You have selected sandbag mode')
        break
    elif gamemode == 4:
        print('You have selected randomizer mode')
        crit_chance = [0, 0, 0]
        in_gamemode_4 = True
        sleep(1)
        print('\nHow many people are playing this mode?')
        print('[1] 1 player')
        print('[2] 2 players')
        gamemode_4_player = int(input('\n'))
        if gamemode_4_player == 1:
            print('You have selected 1 player randomizer')
        if gamemode_4_player == 2:
            print('You have selected 2 player randomizer')
        break
    else:
        print('That is not a valid gamemode, please choose the gamemode again')

print('')
sleep(2)
turn = 1
set_character()

if gamemode != 3:
    turn = 2
    set_character()

# main
print('The round will start in...')
print(3), sleep(1)
print(2), sleep(1)
print(1), sleep(1)
print('GO!!')
print()

turn -= 1
while True:
    oppositing_turn()
    if gamemode == 3:
        turn = 1
    choose_moves = 0
    if gamemode == 4:
        choose_characters = 'r'
        set_character()
        cc_random = randint(1, 100)
    if gamemode == 1 or gamemode_4_player == 1:
        if turn == 2:
            sleep(1)
            print('')
            bot_turn()
        if turn == 1:
            moves_choice()
            choose_moves = int(input())
    else:
        moves_choice()
        choose_moves = int(input())

    print(characters[turn], 'used', moves[turn][choose_moves])
    sleep(2)
    action()

    # critical damage
    if move_type == normal_move:
        luck = randint(1, 100)
        if luck <= crit_chance[turn] + cc_random:
            damage[turn] *= 3
            print('Player', turn, 'has landed a ' + bold + italic + red + 'devastating critical hit!!!' + reset)

    # normal damage
    if choose_moves > 4:
        damage[turn] = 0
    oppo_hp -= damage[turn]
    if oppo_hp == oppo_hp + damage[turn]:
        print('Player', oppo_turn, 'still has' + red, int(oppo_hp), 'HP' + reset)
    else:
        print('Player', oppo_turn, 'now has' + red, int(oppo_hp), 'HP left' + reset)
    sleep(2)

    # double hit
    if move_type == normal_move:
        double_hit_luck = randint(1, 100)
        if double_hit_luck <= double_hit:
            print('Player', turn, 'landed a ' + bold + italic + yellow + 'double hit!!!' + reset)
            oppo_hp -= damage[turn]
            sleep(1)
            print('Player', oppo_turn, 'now has', int(oppo_hp), 'HP left')
            sleep(1)
        double_hit = 20

    # burning damage
    if burning_time[turn] > 0:
        luck = randint(1, 100)
        burning_time[turn] -= 1
        if luck <= 90:
            oppo_hp -= 2
            print('Player', oppo_turn, 'has taken 2 damage from ' + orange + 'burning' + reset)
            sleep(0.5)
            print('Player', oppo_turn, 'now has' + red, int(oppo_hp), 'HP ' + reset + 'left')
            sleep(1)

    if oppo_hp <= 0:
        print(f'Player {oppo_turn} has been ' + bold + italic + red + 'knockout!' + reset)
        exit()

    if stun_random >= 40:
        if turn == 1:
            turn = 2
            hp[2] = oppo_hp
        elif turn == 2:
            turn = 1
            hp[1] = oppo_hp

    stun_random = 100
