from random import randint, choice


class Potion:
    def __init__ (self, name, qualiti):
        assert isinstance(name, str), 'Это долэно быть строкой'
        self.__name = name
        self.__qualiti = qualiti

    def __str__(self) :
        return f'This potion named: {self.__name}, qa {self.__qualiti}'
    
    def get_qualiti(self):
        return self.__qualiti
    def get_name(self):
        return self.__name

    def set_qualiti(self, new_value):
        self.__qualiti = new_value

    def set_name(self, new):
        assert isinstance(new, str), 'Это долэно быть строкой'
        self.__name = new

    def __add__(self, other):
        zxc = len(self.__name) // 2 
        qwer = self.__name[:zxc]
        zxc1 = len(other.__name) // 2
        asd = other.__name[zxc1:]
        new_name =qwer + asd
        new_qualiti = (self.__qualiti + other.__qualiti) // 2
        return Potion(new_name, new_qualiti)
    
    def __sub__(self, other):
        new_qualiti = other.__qualiti - randint(1, 100)
        return Potion(self.__name, new_qualiti)

    def  check_qualiti(self):
        if self.__qualiti > 75:
            print("зелье очень хорошее")
        elif self.__qualiti > 50:
            print("сойдет")
        else:
            print("ужасно")

class Qualiti(Potion):
    def spesial(self):
        return Qualiti(self.__name, self.__qualiti + 20)

class Qualitinot(Potion):
    def spesial(self):
        return Qualitinot(self.__name, self.__qualiti - 20)

game = True
potions = {}

while game:
    potion = input("q or n").lower()
    if potion =="exit":
        game = False
    else:
        potion_name = input('Enter potion name: ')
        potion_qualiti = randint(1, 100)
        if potion == "q":
            new_potion = Qualiti(potion_name, potion_qualiti)
        else:
            new_potion = Qualitinot(potion_name, potion_qualiti)
        potions[potion_name] = new_potion

        if len(potions) >= 3:
            actions = input('Add(+) or Subtract(-) your potions? ').lower()
            print(potions)
            potion1 = potions.pop(choice(list(potions.keys())))
            potion2 = potions.pop(choice(list(potions.keys())))
           
            if actions == "+":
                mixed_potions = potion1 + potion2
            else:
                mixed_potions = potion1 - potion2

            print("смешиваниие")
            if mixed_potions.get_qualiti() < 30:
                print("взрыф")
                game = False
            else:
                potions[mixed_potions.get_name()] = mixed_potions
                print(f'имя зелья: {mixed_potions.get_name()}')
                print(f'качество зелья: {mixed_potions.get_qualiti()}')



