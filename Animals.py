def summary_weight(animals_list):
  animals_list = []
  sum_weight = 0
  for animal in animals_list:
    sum_weight += animal.weight
    print('Общий вес животных: {} кг'.format(sum_weight))


def heaviest_animal(animals):
    animals_list = []
    for animal in animals:
        animals_list.append([animal.name, animal.weight])
        animals_list.sort(key=lambda i: i[1], reverse=True)
    print('Самое тяжелое животное: {} весит {} кг'.format(animals_list[0][0], animals_list[0][1]))

class animal:
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def eat(self):
    feed = 0
    feed = int(input('Сколько кг корма насыпать {}?: '.format(self.name)))
    print('Накормили {}.'.format(self.name))
    self.weight = self.weight + feed
    feed = 0


class goose(animal):
  def speak(self):
    print('{}: Га-га-га!'.format(self.name))

  def action(self):
    print('Собрали яйца у {}.'.format(self.name))


class cow(animal):
  def speak(self):
    print('Му-му-му!'.format(self.name))

  def action(self):
    print('Подоили корову {}.'.format(self.name))

class goat(cow, animal):
  def speak(self):
    print('{}: Ме-ме-ме!'.format(self.name))

  def action(self):
    print('Подоили козу {}.'.format(self.name))

class sheep(animal):
  def speak(self):
    print('{}: Бе-бе-бе!'.format(self.name))

  def action(self):
    print('Постригли овцу {}.'.format(self.name))


class chicken(goose, animal):
  def speak(self):
    print('{}: Ко-ко-ко!'.format(self.name))


class duck(goose, animal):
  def speak(self, name):
    print('{}: Кря-кря-кря!'.format(self.name))


gray_goose = goose('Серый', 6, )
white_goose = goose('Белый', 5)
cow_manka = cow('Манька', 350)
goat_horn = goat('Рога', 50)
goat_hoov = goat('Копыта', 45)
sheep_male = sheep('Барашек', 40)
sheep_female = sheep('Кудрявый', 35)
chicken_coco = chicken('Ко-Ко', 2)
chicken_cucu = chicken('Кукареку', 3)
duck_crya = duck('Кряква', 4)

animals = [gray_goose, white_goose, cow_manka, goat_horn, goat_hoov, sheep_male, sheep_female, chicken_coco, chicken_cucu, duck_crya]

# for animal in animals:
#   print('Имя животного: {}'.format(animal.name))
#   animal.eat()
#   animal.action()
#   print()

summary_weight(animals)
heaviest_animal(animals)

cow_manka.eat()
print(cow_manka.weight)