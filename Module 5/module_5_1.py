class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor: int):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            [print(i) for i in range(1, new_floor + 1)]

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __len__(self):
        if isinstance(self.number_of_floors, int):
            return self.number_of_floors
        else:
            raise TypeError('Этаж должен быть целым числом')

    def __eq__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other, object):
            return self.number_of_floors == other
        else:
            raise TypeError('Этаж должен быть целым числом')

    def __add__(self, value):
        if isinstance(self.number_of_floors, int) and isinstance(value, int):
            self.number_of_floors += value
            return self.number_of_floors
        else:
            raise TypeError('Этаж должен быть целым числом')

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)

    def __gt__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors
        else:
            raise TypeError('Этаж должен быть целым числом')

    def __ge__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors
        else:
            raise TypeError('Этаж должен быть целым числом')

    def __lt__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors
        else:
            raise TypeError('Этаж должен быть целым числом')

    def __le__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors
        else:
            raise TypeError('Этаж должен быть целым числом')

    def __ne__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors != other.number_of_floors
        else:
            raise TypeError('Этаж должен быть целым числом')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)