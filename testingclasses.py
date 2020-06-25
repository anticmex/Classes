# Реализуем классы животных для фермы


class Animals:
    # базовый класс животных
    name = ''  # кличка животного
    animal_type = ''  # вид животного
    weight = 1.0  # kg
    sound = ''  # звук издаваемый животным
    feed_type = ''  # тип любимой еды

    def feed(self, feed_type):
        if self.feed_type.lower() == feed_type.lower():
            print(f"{feed_type.title()} - Превосходный корм для {self.name}!")
            self.weight += int(self.weight*10/100)
        else:
            print(f"{self.name} не очень распробовал Ваш {feed_type}..")
        return f'{self.sound}\n'


class Goose(Animals):
    # Класс описывающий гусей
    animal_type = 'Гусь'
    weight = 5
    feed_type = 'Трава'
    sound = 'Га-га-га'

    def __init__(self, name):
        self.name = name


class Cow(Animals):
    # Класс описывающий коров
    animal_type = 'Корова'
    weight = 100
    feed_type = 'Сено'
    sound = 'Му-у-у'

    def __init__(self, name):
        self.name = name

    def interact(self):
        print(f'\nВы подоили {self.name}!')
        return f'{self.sound}\n'


class Sheep(Animals):
    # Класс описывающий овец
    animal_type = 'Овца'
    weight = 20
    feed_type = 'Трава'
    sound = 'Бе-е-е-е'
    base_weight = weight

    def __init__(self, name):
        self.name = name

    def interact(self):
        if self.weight == self.base_weight:
            print(f'\nВы успешно подстригли {self.name}!')
            self.weight = self.base_weight / 2
        else:
            print(f'\nБедняжка {self.name} уже подстрижена!')
        return f'{self.sound}\n'


class Chicken(Animals):
    # Класс описывающий кур
    animal_type = 'Курица'
    weight = 2
    feed_type = 'Зерно'
    sound = 'Ко-ко-ко'

    def __init__(self, name):
        self.name = name

    def interact(self):
        if self.weight > 0.3:
            print(f'\n{self.name} снесла для Вас яйцо!')
            change_weight = 30
            print(f"Кажется {self.name} слегка похудела.. где-то на {change_weight} грамм.")
            self.weight -= change_weight/100
            return f'{self.sound}\n'
        else:
            print(f'\nСрочно покормите бедняжку {self.name}!')
            return f'Она уже легче воздуха!\n'


class Goat(Cow):
    # Класс описывающий Коз
    animal_type = 'Коза'
    weight = 15
    feed_type = 'Капуста'
    sound = 'Ме-е-е-е'

    def __init__(self, name):
        self.name = name


GrayGoose = Goose("Серый")
WhiteGoose = Goose('Белый')
FarmCow = Cow('Манька')
FirstSheep = Sheep('Барашек')
SecondSheep = Sheep('Кудрявый')
FirstChick = Chicken('Ко-ко')
SecondChick = Chicken('Кукареку')
FirstGoat = Goat('Рога')


# print(GrayGoose.weight)
# print(GrayGoose.feed('трава'))
# print(GrayGoose.weight)
print(FirstGoat.feed('капуста'))
print(FirstGoat.interact())
print(FirstGoat.animal_type)