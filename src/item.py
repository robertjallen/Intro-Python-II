class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    # def get(self):
    #     print("You got" + self.name)

    # def drop(self):
    #     print("You dropped" + self.name)
        # print(f'{self.name} , {self.description}')
        
    def __str__(self):
        return f'Item: {self.name}, {self.description}'