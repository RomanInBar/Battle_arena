from random import choice
from colorama import Fore, Style


class Thing:
    things = []

    def __init__(self, name, hp=0, damage=0, protection=0):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.protection = protection

    def things_list(self):
        Thing.things.append(self)


Skull_Basher = Thing('Skull Basher', damage=25).things_list()
Gauntlets_of_Strength = Thing('Gauntlets of Strength', damage=3).things_list()
Ring_of_Protection = Thing('Ring of Protection', protection=2).things_list()
Claymore = Thing('Claymore', damage=20).things_list()
Hood_of_Defiance = Thing('Hood of Defiance', protection=10).things_list()
Vanquard = Thing('Vanquard', hp=250, protection=7).things_list()
Blabe_Mail = Thing('Blabe Mail', damage=28, protection=6).things_list()
Aeon_Disk = Thing('Aeon Disk', hp=300).things_list()
Soul_Booster = Thing('Soul Booster', hp=425).things_list()
Eternal_Shroud = Thing('Eternal Shroud', hp=200, protection=4).things_list()
Crimson_Guard = Thing('Crimson Guard', hp=250, protection=6).things_list()
Lotus_Orb = Thing('Lotus Orb', protection=10, hp=250).things_list()
Arcane_Blink = Thing('Arcane Blink', hp=25).things_list()
Swift_Blink = Thing('Swift Blink', protection=7).things_list()
Overwhelming_Blink = Thing('Overwhelming Blink', damage=25).things_list()
Mjollnir = Thing('Mjollnir', damage=24).things_list()
Eye_of_Skadi = Thing(
    'Eye of Skadi', hp=225, damage=25, protection=7).things_list()
Satanic = Thing('Satanic', damage=80).things_list()
Yasha_and_Kaya = Thing(
    'Yasha and Kaya', damage=12, hp=16, protection=7).things_list()
Sange_and_Yasha = Thing('Sange and Yasha', damage=46).things_list()
Heavens_Halberd = Thing("Heaven's Halberd", damage=20).things_list()
Magic_Wand = Thing('Magic Wand', hp=30, damage=30, protection=3).things_list()
Null_Talisman = Thing('Null Talisman', damage=20).things_list()
Wraith_Band = Thing('Wraith Band', damage=20, protection=6).things_list()
Bracer = Thing('Bracer', damage=8, hp=10).things_list()
Soul_Ring = Thing('Soul Ring', damage=6, protection=2).things_list()
Orb_of_Corrosion = Thing('Orb of Corrosion', hp=150).things_list()
Falcon_Blade = Thing(
    'Falcon Blade', hp=175, damage=10, protection=9).things_list()
Phase_Boots = Thing('Phase Boots', damage=30, protection=4).things_list()
Helm_of_the_Overlord = Thing(
    'Helm of the Overlord', hp=280, damage=20, protection=8).things_list()
Blitz_Knuckles = Thing('Blitz Knuckles', damage=35).things_list()
Mithril_Hammer = Thing('Mithril Hammer', damage=24).things_list()
Javelin = Thing('Javelin', damage=70).things_list()
Claymore = Thing('Claymore', damage=20).things_list()
Broadsword = Thing('Broadsword', damage=15).things_list()
Helm_of_Iron_Will = Thing(
    'Helm of Iron Will', hp=50, protection=6).things_list()
Quarterstaff = Thing('Quarterstaff', damage=20).things_list()
Chainmail = Thing('Chainmail', protection=4).things_list()
Blades_of_Attack = Thing('Blades of Attack', damage=9).things_list()
Assault_Cuirass = Thing('Assault Cuirass', protection=10).things_list()


class Person:
    LOSER = '{} погибает.'
    WINNER = 'Победитель: {}!'
    TOTAL_WINNER = 'Абсолютный чемпион турнира: {}!!!'
    DAMAGE = (
        '{yellow}{person_1}{reset} наносит удар по '
        '{blue}{person_2}{reset} '
        'на {red}{damage}{reset} '
        'у {blue}{person_2}{reset} осталось {green}{hp}{reset}')

    equips = []
    warriors = []

    def __init__(self, name, hp=0, damage=0, protection=0):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.protection = protection

    def warriors_list(self):
        Person.warriors.append(self)

    def opponents(self):
        player_1 = choice(Person.warriors)
        player_1.equip()
        player_2 = choice(Person.warriors)
        player_2.equip()
        if player_1 != player_2:
            player_1.war(player_2)
            return
        else:
            self.opponents()

    def equip(self):
        for i in range(4):
            player_thing = choice(Thing.things)
            self.hp += player_thing.hp
            self.damage += player_thing.damage
            self.protection += player_thing.protection
            Person.equips.append(player_thing.name)

    def attack(self, enemy):
        punch = self.damage - (self.damage / 100 * enemy.protection)
        return punch

    def comments(self, enemy):
        print(Person.DAMAGE.format(
            yellow=Fore.YELLOW,
            blue=Fore.BLUE,
            red=Fore.RED,
            green=Fore.GREEN,
            reset=Style.RESET_ALL,
            person_1=self.name,
            person_2=enemy.name,
            damage=round(self.attack(enemy), 2),
            hp=round(enemy.hp, 2)))

    def war(self, opponent):
        self.hp -= self.attack(opponent)
        self.comments(opponent)
        if opponent.hp <= 0:
            self.warriors.remove(opponent)
            if len(self.warriors) == 1:
                print(
                    f'{Fore.RED}{Person.LOSER.format(opponent.name)}\n'
                    f'{Fore.GREEN}{Person.TOTAL_WINNER.format(self.name)}')
                return
            print(
                f'{Fore.RED}{Person.LOSER.format(opponent.name)}\n'
                f'{Fore.GREEN}{Person.WINNER.format(self.name)}')
            return self.opponents()
        opponent.hp -= opponent.attack(self)
        opponent.comments(self)
        if self.hp <= 0:
            self.warriors.remove(self)
            if len(self.warriors) == 1:
                print(
                    f'{Fore.RED}{Person.LOSER.format(self.name)}\n'
                    f'{Fore.GREEN}{Person.TOTAL_WINNER.format(opponent.name)}')
                return
            print(
                f'{Fore.RED}{Person.LOSER.format(self.name)}\n'
                f'{Fore.GREEN}{Person.WINNER.format(opponent.name)}')
            return self.opponents()
        return self.war(opponent)


class Paladin(Person):
    def __init__(self, name, hp, damage, protection):
        super().__init__(name, hp, damage, protection)
        self.protection = protection * 2
        self.hp = hp * 2


class Warrior(Person):
    def __init__(self, name, hp, damage, protection):
        super().__init__(name, hp, damage, protection)
        self.damage = damage * 2


class Hunter(Person):
    pass


class Healer(Person):
    pass


Abaddon = Warrior('Abaddon', 660, 51, 3).warriors_list()
Alchemist = Warrior('Alchemist', 700, 49, 2.4).warriors_list()
Earth_Spirit = Warrior('Earth Spirit', 640, 47, 2.7).warriors_list()
Tusk = Warrior('Tusk', 660, 50, 4.6).warriors_list()
Omniknight = Warrior('Omniknight', 680, 55, 4.4).warriors_list()

Oracle = Paladin('Oracle', 600, 39, 2.4).warriors_list()
Windranger = Paladin('Windranger', 560, 42, 1.7).warriors_list()
Bane = Paladin('Bane', 640, 57, 4.5).warriors_list()
Jakiro = Paladin('Jakiro', 740, 53, 3.4).warriors_list()
Lina = Paladin('Lina', 600, 49, 3.6).warriors_list()


start = Person('Judge')
start.opponents()
