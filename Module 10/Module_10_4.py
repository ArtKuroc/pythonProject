import random
import time
from threading import Thread
from queue import Queue

class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.finished = False

    def run(self):
        time.sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            available_tables = [table for table in self.tables if table.guest is None]
            if available_tables:
                table = available_tables[0]
                table.guest = guest
                table.guest.start()
                print(f'{guest.name} сел(-а) за стол номер {table.number}')
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while True:
            occupied_table = [table for table in self.tables if table.guest]
            if not self.queue.empty() or occupied_table:
                for table in occupied_table:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None
                        if not self.queue.empty():
                            table.guest = self.queue.get()
                            print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                            table.guest.start()
            else:
                break

tables = [Table(number) for number in range(1, 6)]

guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()