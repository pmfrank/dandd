import being
from readchar import readchar
from dice import dice_roll

player = being.Character(name = 'Paladin', strength = 16, dexterity = 10, constitution = 14, intelligence = 11, wisdom = 14, charisma = 14, ac = 19, speed = 30, hp = 28)
player.profbonus = 2

enemy = being.Moster(creature = 'zombie', strength = 13, dexterity = 6, constitution = 16, intelligence = 3, wisdom = 6, charisma = 5, ac = 9, hp = 22, speed = 20)
enemy.profbonus = 2

print('''
    You have found yourself in the crypt of the notorious Salvone family. The leaders of your priesthood have order you here to investigate
the romours of foul deeds carried out by the family. The locals have told you about vampires and other dead that walk, though you secretly
hope that you encounter none of the that nonsense here. Your hopes are dashed as you see a shambeling corpse just on the edge of your torch
light. It's low, gutteral moan tells you that you are about to face off with one of the Salvones that didn't get a dignified unlife, this
is a zombie. You draw your longsword and prepare for battle.

Press any key to start the fight
''')
readchar()

allowedactions = ['attack']

while player.attribute['hp'] > 0 and enemy.attribute['hp'] > 0:

    print('what shall you do? (Sorry, all you can do is attack right now. Spell casting and special abilities are coming)')
    for allowedaction in allowedactions:
        print(allowedaction, end=" | ") 
    print()
    command = input('>>')

    if command.lower().strip() in allowedactions:
        attackroll = dice_roll(1,20) + player.modifier['strength'] + player.profbonus
        if attackroll >= enemy.attribute['ac']:
            print(f'Your long sword strikes the {enemy.creature} and cuts deep')
            damage = dice_roll(1,8) + player.modifier['strength']
            print(f'You do {damage} points of damage to the {enemy.creature}')
            enemy.attribute['hp'] = enemy.attribute['hp'] - damage
        else:
            print(f'Your attack has failed to hit the {enemy.creature}.')
        print(f'The {enemy.creature} comes with a visious attack')
        attackroll = dice_roll(1,20) + enemy.profbonus + enemy.modifier['strength']
        if attackroll >= player.attribute['ac']:
            print(f'The {enemy.creature} has struck you')
            damage = dice_roll(1,6) + enemy.modifier['strength']
            player.attribute['hp'] = player.attribute['hp'] - damage
            print(f'You suffer {damage} points of damage, you have {player.attribute["hp"]} left.')
        else:
            print(f'The {enemy.creature}\'s attack has missed')
    else:
        print('Invalid action, try again.')
        pass

if player.attribute['hp'] <= 0:
    print('Unfortunately, this is where you life comes to an end solder. You will be remembered in the songs by your brothers in faith.')
else:
    print('The foul beast falls to your feet with a dull, sickening thud. You steel yourself for what will come next as you venture forth.')
