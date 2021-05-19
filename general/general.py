import math
import itertools


class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def add_character_to_name(self, c):
        self.name += c

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'


def test():
    # classical sort
    a = [1, 2, 9, 8, 22, 2.5, 14]
    print(sorted(a))

    # sort by custom key
    b = ['Calin', 'Mircea', 'Valeriu', 'Zoe', 'Trahanache', 'Bisbal', 'Van Dijk']
    print(f'Sorted alphabetically: {sorted(b)}')
    print(f'Sorted by string length: {sorted(b, key= str.__len__)}')
    print(f'Sorted alphabetically by the 3rd letter in each word: {sorted(b, key = lambda x: x[2 if len(x) > 2 else 1])}')

    # sort reverted
    c = [9.33, 12, 1.77, math.pi, math.sqrt(12), math.pow(3, 9), math.sqrt(5.23138219831823128312)]
    print(f'Sorted descending {sorted(c, reverse=True)}')

    # Test sum functions and alternatives
    print('Sum of elements in a is: {0}'.format(sum(a)))
    print('Sum of last 3 elements in a is: {0}'.format(sum(a[-3:])))
    print('Sum of 1000 and all elements in a is {0}'.format(sum(a, start=1000)))

    print('Using sum for a float list : {0}'.format(sum(c)))
    print('Using math.fsum() for a float list: ', math.fsum(c))

    persons = [Person('Calin', 22), Person('Zoe'), Person('Trahanache', 44), Person('Mircea', 90)]
    other_persons = [Person('Valeriu', 14), Person('Bisbal', 19)]

    print('Using itertools.chain to iterate over multiple lists')
    for p in itertools.chain(persons, other_persons):
        print(p)

    print('itertools.chain with lists of different types')
    for t in itertools.chain(a, persons):
        print(t)
