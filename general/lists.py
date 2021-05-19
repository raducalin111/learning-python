def test():
    print('test'.__contains__('te'))
    fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
    fruits_containing_a = [fruit for fruit in fruits if fruit.__contains__('a')]
    print(fruits_containing_a)

    combinations = [(x, y, z) for x in range(3) for y in range(3) for z in range(3) if x != y != z != x]
    print(combinations)

    squares = [x**2 for x in range(2, 15) if x % 3 != 2]
    print(squares)

    # range parameters must be integers!
    r = range(3, 100, 9)
    for x in r:
        print(x, end=" ")


test()
