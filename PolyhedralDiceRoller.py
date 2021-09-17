import random


def roll(nDice, nSides):
    sum = 0
    for dice in range(nDice):
        sum += random.randint(1, nSides)
    return sum

print(roll(1, 20))

def fireball():
    return roll(8, 6)
print(fireball())


def chaosBoltDamageType(damage):
    if damage == 1:
        return 'Acid'
    if damage == 2:
        return 'Cold'
    if damage == 3:
        return 'Fire'
    if damage == 4:
        return 'Force'
    if damage == 5:
        return 'Lightning'
    if damage == 6:
        return 'Poison'
    if damage == 7:
        return 'Psychic'
    if damage == 8:
        return 'Thunder'

def chaosBolt():
    sum = 0
    d8Roll = roll(1, 8)
    sum += d8Roll
    print(chaosBoltDamageType(d8Roll))
    d8Roll = roll(1, 8)
    sum += d8Roll
    print(chaosBoltDamageType(d8Roll))
    sum += roll(1, 6)
    return sum

print(chaosBolt())

print(True or True)