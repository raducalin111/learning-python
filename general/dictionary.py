class TestNoHash:
    def __init__(self, length, name):
        self.length = length
        self.name = name

    def set_name(self, name):
        self.name = name


class TestHash(TestNoHash):
    def __hash__(self):
        return hash((self.name, self.length))


def test():
    p = {'name': 'Calin', 'age': 22}
    capitals = {'Romania': 'Bucharest', 'Spain': 'Madrid', 'Portugal': 'Lisbon'}

    print('Printing a field from dictionary....')
    print(p['name'])

    print('Printing values....')
    for cap in capitals.values():
        print(cap)

    print('Printing keys....')
    for field in p.keys():
        print(field)

    print('Checking if hash remains the same after field change....')
    test_no_hash = TestNoHash(3, 'Name')
    print(test_no_hash.__hash__())
    test_no_hash.set_name('Another')
    print(test_no_hash.__hash__())

    print('Checking if hash changes after overriding hash and field change....')
    test_hash = TestHash(3, 'Name')
    print(test_hash.__hash__())
    test_hash.set_name('Another')
    print(test_hash.__hash__())

    print('Checking how dictionaries behave when overriding hash....')
    dic = {test_hash: 1}
    print(dic.__contains__(test_hash))
    test_hash.set_name('Nameee')
    print(dic.__contains__(test_hash))
    dic[test_hash] = 2
    print('Dictionary now contains 2 equal keys!')
    print(dic)


test()
