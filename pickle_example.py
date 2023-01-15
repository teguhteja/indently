import pickle
import json

class Fruit:
    def __init__(self, name:str, calories:float) -> None:
        self.name = name
        self.calories = calories

    def describe_fruit(self):
        print(self.name, self.calories, sep=': ')

# if __name__ == '__main__':
#     fruit:Fruit = Fruit('Banana', 100)
#     fruit.describe_fruit()

#     fruit.calories = 150

#     with open('banana.json','w') as file:
#         data = {'name': fruit.name, 'calories': fruit.calories}
#         json.dump(data,file)

    
#     with open('banana.json','r') as file:
#         data = json.load(file)
#         print(data)

if __name__ == '__main__':
    # fruit:Fruit = Fruit('Banana', 100)
    # fruit.describe_fruit()
    with open('data.pickle','rb') as file:
        fruit: Fruit = pickle.load(file)

    fruit.calories += 150

    with open('data.pickle','wb') as file:
        pickle.dump(fruit, file)
        
    fruit.describe_fruit()