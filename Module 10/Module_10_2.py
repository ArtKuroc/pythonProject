import threading
import time

class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.fight()

    def fight(self):
        enemies = 100
        counter = 0
        while enemies > 0:
            if self.power > 0:
                enemies -= self.power
                counter += 1
                if enemies > 0:
                    print(f'{self.name} сражается {counter} дней(дня)..., осталось {enemies} врагов.')
                else:
                    print(f'{self.name} сражается {counter} дней(дня)..., осталось 0 врагов.')
            else:
                print(f'{self.name} не может нанести удар, сила равна {self.power}.\n')
                break
            time.sleep(1)
        if enemies <= 0:
            print(f'{self.name} одержал победу спустя {counter} дней(дня)!\n')
        else:
            print(f'{self.name} потерпел поражение спустя {counter} дней!\n')

knight1 = Knight('Оберин "Красный Змей" Мартелл', 10)
knight2 = Knight('Григор "Гора" Клиган', 20)
knight1.start()
knight2.start()

knight1.join()
knight2.join()

print('Все битвы закончились!')