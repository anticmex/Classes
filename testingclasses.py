# Реализуем классы животных для фермы


# def sexchecked(sex):
#     # функция для проверки падежей
#     if sex == 'female':
#         return 'a'



class Animals:
    """ базовый класс животных    """
    name = ''  # кличка животного
    animal_type = ''  # вид животного
    weight = 1.0  # kg вес по умолчанию
    sound = ''  # звук издаваемый животным
    feed_type = ''  # тип любимой еды
    sex = 'male'  # пол животного по умолчанию
    weight_count = 0  # счетчик общего веса
    max_weight = 0  # счетчик максимального веса
    max_weight_name = ''
    max_weight_animal_type = ''

    def __init__(self):
        Animals.weight_count += self.weight


class AnimalsAction(Animals):
    """Класс возможных действий с животными"""

    def __init__(self, name, weight_in=0):
        self.name = name
        if weight_in > 0:
            self.weight = weight_in
        else:
            self.weight = self.weight
        super().__init__()
        if self.weight > Animals.max_weight:
            Animals.max_weight = self.weight
            Animals.max_weight_name = self.name
            Animals.max_weight_animal_type = self.animal_type

    def feed(self, feed_type):
        # функция кормления животного. животное набирает вес, если еда ему нравится.
        if self.feed_type.lower() == feed_type.lower():
            print(f"{feed_type.title()} - Превосходный корм для {self.name}!")
            self.weight += float(self.weight * 10 / 100)
        else:
            print(f"{self.name} не очень распробовал Ваш {feed_type}..")
        return f'{self.sound}\n'

    def interact(self):
        # отдельная функция для взаимодействия с животными в зависимости от их типа
        if self.animal_type.lower() == 'гусь' \
                or self.animal_type.lower() == 'курица' \
                or self.animal_type.lower() == 'утка':

            if self.weight > 0.3:
                if self.sex == 'female':
                    print(f'\n{self.name} снесла для Вас яйцо!')
                else:
                    print(f'\n{self.animal_type.title()} по кличке "{self.name}" успешно ощипан!')
                change_weight = 30
                print(f"Кажется вес животного уменьшился.. где-то на {change_weight} грамм.")
                self.weight -= change_weight / 100
                return f'{self.sound}\n'
            else:
                return f'\nСрочно покормите бедняжку {self.name}!\n'

        elif self.animal_type.lower() == 'корова' or self.animal_type.lower() == 'коза':
            print(f'\nВы подоили {"".join(list(self.animal_type[:-1])) + "у"} {self.name}!')
            return f'{self.sound}\n'
        elif self.animal_type.lower() == 'овца':
            if self.weight == self.base_weight:
                print(f'\nВы успешно подстригли {"".join(list(self.animal_type[:-1])) + "у"} {self.name}!')
                self.weight = self.base_weight / 2
            else:
                print(f'\nБедняжка {self.name} уже подстрижена!')
            return f'{self.sound}\n'


class Chicken(AnimalsAction):
    # Класс описывающий кур
    animal_type = 'курица'
    weight = 2
    feed_type = 'Зерно'
    sound = 'Ко-ко-ко'
    sex = 'female'


class Goose(AnimalsAction):
    # Класс описывающий гусей
    animal_type = 'гусь'
    weight = 5
    feed_type = 'Трава'
    sound = 'Га-га-га'


class Cow(AnimalsAction):
    # Класс описывающий коров
    animal_type = 'корова'
    weight = 100
    feed_type = 'Сено'
    sound = 'Му-у-у'


class Sheep(AnimalsAction):
    # Класс описывающий овец
    animal_type = 'овца'
    weight = 20
    feed_type = 'Трава'
    sound = 'Бе-е-е-е'
    base_weight = weight


class Goat(AnimalsAction):
    # Класс описывающий Коз
    animal_type = 'коза'
    weight = 15
    feed_type = 'Капуста'
    sound = 'Ме-е-е-е'


class Duck(AnimalsAction):
    # Класс описывающий уток
    animal_type = 'утка'
    weight = 3
    feed_type = 'Трава'
    sound = 'Кря-кря'


GrayGoose = Goose("Серый")
WhiteGoose = Goose('Белый')
FarmCow = Cow('Манька')
FirstSheep = Sheep('Барашек')
SecondSheep = Sheep('Кудрявый')
FirstChick = Chicken('Ко-ко')
SecondChick = Chicken('Кукареку')
FirstGoat = Goat('Рога')
SecondGoat = Goat('Копыта')
OneDuck = Duck('Кряква')
farm_animal = {1: [GrayGoose, WhiteGoose],
               2: [FarmCow],
               3: [FirstSheep, SecondSheep],
               4: [FirstChick, SecondChick],
               5: [FirstGoat, SecondGoat],
               6: [OneDuck]}




class UserAction:
    position = 'ферма'

    def __init__(self, user_command):
        self.user_command = user_command
        if len(farm_animal[int(self.user_command)]) > 1:
            UserAction.anim_value0 = list(farm_animal[int(self.user_command)])[0]
            UserAction.anim_value1 = list(farm_animal[int(self.user_command)])[1]
        else:
            UserAction.anim_value0 = list(farm_animal[int(self.user_command)])[0]

    def __oneanimal__(self):
        return f'Тут у нас живут {self.anim_value0.animal_type}' \
               f' {self.anim_value0.name}'

    def __twoanimal__(self):
        def letter_correct():
            if self.anim_value0.animal_type == 'гусь':
                return 'и'
            else:
                return 'ы'

        return (f'Тут у нас живут {"".join(list(self.anim_value0.animal_type)[:-1]) + letter_correct()} '
                f'{self.anim_value0.name} и '
                f'{self.anim_value1.name}.')

    def __section_view__(self):
        print(f'\nПеред Вами секция фермы №{self.user_command}.')
        if len(farm_animal[int(self.user_command)]) > 1:
            print(UserAction.__twoanimal__(self))
        else:
            print(UserAction.__oneanimal__(self))

    def __animallook__(self):
        command = input(f'Выберете действие:\n'
                          f'[1] - подойти к {self.anim_value0.name}\n'
                          f'[2] - подойти к {self.anim_value1.name}\n'
                          f'[3] - вернуться назад. ')
        if bool(command) != False and command != '3':
            if command == '1':
                animal = self.anim_value0
            elif command == '2':
                animal = self.anim_value1

            print(f'\nПеред Вами {animal.animal_type} по кличке {animal.name}')
            print(f'Вы слышите типичный звук "{animal.sound}"')
            UserAction.__animalaction__(self, animal)

    def __animalaction__(self, animal):
        command = input(f'Выберете действие:\n'
                         f'[1] - Покормить {animal.name}\n'
                         f'[2] - Поработать с {animal.name}\n'
                         f'[3] - вернуться назад. ')
        if command == '1':
           animal.feed(input('Напишите чем Вы хотите покормить животное? '))
        elif command == '2':
            animal.interact()

        UserAction.__animallook__(self)


    def __interactinsection__(self):
        if len(farm_animal[int(self.user_command)]) > 1:
            UserAction.__animallook__(self)

    def action(self):
        if int(self.user_command) in farm_animal.keys():
            UserAction.position = self.anim_value0.animal_type
        else:
            UserAction.position = 'ферма'
        UserAction.__section_view__(self)
        UserAction.__interactinsection__(self)

def main():
    while True:
        print('Добро пожаловать на ферму Дядюшки Джо!')
        print('Сейчас на ферме есть следующие животные:')
        for key, val in farm_animal.items():
            if len(val) > 1:
                print(f'{key}: {val[0].animal_type} - {val[0].name} и {val[1].animal_type} - {val[1].name}')
            else:
                print(f'{key}: {val[0].animal_type} - {val[0].name}')
        print('Напечатайте "q" для выхода из программы.')
        command = input('Выберете секцию к которой хотели бы подойти поближе: ')
        if command.lower() == 'q' or command.lower() == 'й':
            break

        while bool(command) == False or not command.isdigit() or not int(command) in list(farm_animal.keys()):
            if bool(command) == False:
                print('\nВы не выбрали ни одной секции!')
            elif not command.isdigit():
                print('\nВы указали буквы вместа номера секции!')
            else:
                print('\nВ настоящий момент данная секция не открыта. Выберети другую.')
            command = input('Выберете секцию к которой хотели бы подойти поближе: ')

        UserAction(command).action()
        print(UserAction.position)


main()
# print(GrayGoose.weight)
# print(GrayGoose.feed('трава'))
# print(GrayGoose.weight)
# print(WhiteGoose.weight)
# print(WhiteGoose.feed('трава'))
# print(WhiteGoose.weight)
# print(FirstGoat.feed('капуста'))
# print(GrayGoose.interact())
# print(farm_animal[1][0].sex)
# print(f'Вес всех животных {Animals.weight_count}!')
# print(f'Самое тяжелое животное - {Animals.max_weight_animal_type} {Animals.max_weight_name} весит {Animals.max_weight}!')
