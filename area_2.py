from random import choice
from colorama import Fore, Style

from objects import pal_list, warr_list, all_things_list


class Thing:
    things = []

    def __init__(self, name, hp=0, damage=0, protection=0):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.protection = protection

    def things_list(self):
        """Создает список вещей для героев."""
        Thing.things.append(self)


class Person:
    RAUND = 'Раунд: {}'
    LOSER = '{} погибает.'
    WINNER = 'Победитель: {}!'
    TOTAL_WINNER = 'Абсолютный чемпион турнира: {}!!!'
    DAMAGE = (
        '{yellow}{person_1}{reset} наносит удар по '
        '{blue}{person_2}{reset} '
        'на {red}{damage}{reset} '
        'у {blue}{person_2}{reset} осталось {green}{hp}{reset}')

    warr_out_equip = []
    warriors = []
    raund = 0

    def __init__(self, name, hp=0, damage=0, protection=0):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.protection = protection
        self.equips = []

    def warriors_list(self):
        """Создает список героев."""
        Person.warriors.append(self)

    def warriors_without_equip(self):
        """Список героев без экипа."""
        Person.warr_out_equip.append(self)

    def opponents(self):
        """Отбирает двух случайных героев."""
        player_1 = choice(Person.warriors)
        player_2 = choice(Person.warriors)
        if player_1 != player_2:
            player_1.equip()
            player_2.equip()
            self.current_round()
            print()
            print(
                f'{Fore.LIGHTRED_EX}{Person.RAUND.format(Person.raund)}\n'
                f'{player_1.name} против {player_2.name}')
            player_1.war(player_2)
            return
        self.opponents()

    def return_of_characteristics(self):
        """Сбрасывает характеристики героя до изначальных."""
        for person in Person.warr_out_equip:
            if self.name == person.name:
                self.hp = person.hp
                self.damage = person.damage
                self.protection = person.protection

    def equip(self):
        """Снаряжает героя случайной экипировкой."""
        if len(self.equips) > 0:
            self.equips = []
        self.return_of_characteristics()
        for i in range(4):
            player_thing = choice(Thing.things)
            self.hp += player_thing.hp
            self.damage += player_thing.damage
            self.protection += player_thing.protection
            self.equips.append(player_thing.name)

    def current_round(self):
        """Увеличивает значение раунда."""
        Person.raund += 1

    def attack(self, enemy):
        """Расчитывает получаемый урон."""
        punch = self.damage - (self.damage / 100 * enemy.protection)
        return punch

    def comments(self, enemy):
        """
        Выводит в консоль информацию об уроне
         и оставшихся очках жизни.
        """
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
        """Бой между героями, определение чемпиона."""
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


for hero in warr_list:
    name, hp, damage, protection = hero
    Warrior(name, hp, damage, protection).warriors_list()

for hero in warr_list:
    name, hp, damage, protection = hero
    Warrior(name, hp, damage, protection).warriors_without_equip()

for hero in pal_list:
    name, hp, damage, protection = hero
    Warrior(name, hp, damage, protection).warriors_list()

for hero in pal_list:
    name, hp, damage, protection = hero
    Warrior(name, hp, damage, protection).warriors_without_equip()

for thing in all_things_list:
    name, hp, damage, protection = thing
    Thing(name, hp, damage, protection).things_list()


start = Person('Judge')
start.opponents()
