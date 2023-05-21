"property - изучить"
"обстракт.классы - что это"
"мексины - что это"


class Person:
    def __init__(self, name, surname, age, weight, height, hair_color, skin_color):
        self.name = name
        self.surname = surname
        self.age = age
        self.weight = weight
        self.height = height
        self.hair_color = hair_color
        self.skin_color = skin_color

    def compare_by_skin_color(self):
        if self.skin_color is "Black".lower():
            return f"Person {self.name} - black man"
        return f"Person {self.name} - white man"

    def set_name(self, value):
        setattr(self, "name", value)

    def set_surname(self, value):
        setattr(self, "surname", value)

    def set_age(self, value):
        setattr(self, "age", value)

    def set_weight(self, value):
        setattr(self, "weight", value)

    def set_height(self, value):
        setattr(self, "height", value)

    def set_hair_color(self, value):
        setattr(self, "hair_color", value)

    def set_skin_color(self, value):
        setattr(self, "skin_color", value)

    def get_print_weight(self, obj):
        if not self.__gt__(obj):
            print(f'{obj.name} весит больше чем {self.name}')
        else:
            print(f'{self.name} весит больше чем {obj.name}')

    def get_print_height(self, obj):
        if not self.__gt__(obj):
            print(f'{self.name} выше чем {obj.name}')
        else:
            print(f'{obj.name} выше чем {self.name}')

    def compare_by_weight(self, obj: int) -> int:
        if not isinstance(obj, (int, Person)):
            raise TypeError('Операнды справа должен иметь тип int или Clock')
        return obj if isinstance(obj, int) else obj.weight

    def compare_by_height(self, obj):
        if not isinstance(obj, (int, Person)):
            raise TypeError('Операнды справа должен иметь тип int или Clock')
        return obj if isinstance(obj, int) else obj.height

    def __eq__(self, obj):
        if self.weight:
            res = self.compare_by_weight(obj)
            return self.weight == res
        if self.height:
            res = self.compare_by_height(obj)
            return self.height == res

    def __lt__(self, obj):
        if self.weight:
            res = self.compare_by_weight(obj)
            return self.weight < res
        if self.height:
            res = self.compare_by_height(obj)
            return self.height < res

    def __gt__(self, obj):
        if self.weight:
            res = self.compare_by_weight(obj)
            return self.weight > res
        if self.height:
            res = self.compare_by_height(obj)
            return self.height > res

    def person_info(self):
        print(
            f"Person name: {self.name}, surname: {self.surname}, age: {self.age}, "
            f"weight: {self.weight} kg, height: {self.height} sm, "
            f"hair_color: {self.hair_color}, skin color: {self.skin_color}"
        )


person1 = Person("Mikolai", "Popov", 36, 89, 1.90, "silver", "white")
person1.person_info()
person1.height = 1.93
person2 = Person("Grisha", "Vinokur", 40, 90, 1.83, "black", "black")
person3 = Person('Volodya', 'Pupkin', 34, 82, 1.85, 'silver', 'white')
person4 = Person('Petya', 'Petrov', 45, 80, 1.86, 'black', 'white')
person5 = Person('Sasha', 'Shushkevich', 40, 90, 1.87, 'yellow', 'black')
print(person2.weight > person1.weight)
print(person5.height == person4.height)
print(person1.height < person3.height)
Person.get_print_height(person1, person2)
Person.get_print_weight(person2, person1)

# class BankAccount:
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#
#     def get_balance(self):
#         print('get balance')
#         return self.__balance
#
#     def set_balance(self, value):
#         if not isinstance(value, int | float):
#             raise ValueError('Водимое значение должно быть числом!!')
#         self.__balance = value
#         print('set balance')
#
#     def del_balance(self):
#         print('del balance')
#         del self.__balance
#
#     balance = property(fget=get_balance, fset=set_balance, fdel=del_balance)
#
#
# user1 = BankAccount('Tanya', 1000)
# print(user1.balance)
# user1.balance = 777
# print(user1.balance)
# user1.del_balance()
# user1.balance = 786
# print(user1.balance)


