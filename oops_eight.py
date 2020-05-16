# multiple inheritence
class Employee:
    no_of_leaves = 10
    var = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return print(f'{self.name}  {self.salary}  {self.role}')


class Player():
    no_of_game = 4
    var = 9

    def __init__(self, game, name):
        self.game = game
        self.name = name

    def printdetails(self):
        return print(f'{self.name}  {self.game} ')


class Coool_programmer(Player, Employee):
    language = 'c++'

    # var = 10

    def printlanguage(self):
        print(self.language)


karan = Coool_programmer('karan', 'cricket')
print(karan.printdetails())

# the class player uses the methods of  two other classes. the class which is written first  inn bracket
# if player class uses constructor of other classes .. and player class uses the constructor of first class

print(karan.language)
print(karan.var)

# the class in which we are inheriting the two other classses are  employee and playe r
# sequence of classes matters in the class in which we are inheriting the two other classes
