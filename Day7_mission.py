# #10.1
# class Thing:
#     pass
# example = Thing()
#
# print(Thing())
# print(example)
#
# #10.2
#
# class Thing2:
#     letters = 'abc'
#
# print(Thing2.letters)
#
# #10.3
#
# class Thing3():
#     pass
#
# a = Thing3()
# a.letter = "xyz"
# print(a.letter)

#10.4


# class Element():
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number

# el = Element("Hydrogen", "H", 1)

#10.5

# el_dict = {'name':'Hydrogen', 'symbol':'H', 'number':1}
#
# class Element():
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
#
#
# hydrogen = Element(**el_dict)

#10.6

# class Element():
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
#
#     def dump(self):
#         return f"{self.name}, {self.symbol}, {self.number}"
#
# hydrogen = Element("Hydrogen" , "H", 1)
# print(hydrogen.dump())

#10.7

class Element():
    def __init__(self, name, symbol, number):
        self.hidden_name = name
        self.hidden_symbol = symbol
        self.hidden_number = number

    @property
    def name(self):
        return self.hidden_name

    @property
    def symbol(self):
        return self.hidden_symbol

    @property
    def number(self):
        return self.hidden_number

hydrogen = Element("Hydrogen" , "H", 1)
print(hydrogen)
