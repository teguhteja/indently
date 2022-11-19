class Fruit:
    def __init__(self, name:str):
        self._name = name

    @property
    def fruit_name(self):
        return self._name

    @fruit_name.setter
    def fruit_name(self, value):
        self._name = value

    @fruit_name.deleter
    def fruit_name(self):
        print(f'{self._name} was deleted')
        del self._name


if __name__ == '__main__':
    fruit = Fruit('Banana')

    print(fruit.fruit_name)
    fruit.fruit_name = 'Apple'
    print(fruit.fruit_name)

    del fruit.fruit_name

    print(fruit.fruit_name)