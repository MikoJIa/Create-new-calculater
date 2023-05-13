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
        return setattr(self, "name", value)

    def set_surname(self, value):
        return setattr(self, "surname", value)

    def set_age(self, value):
        return setattr(self, "age", value)

    def set_weight(self, value):
        return setattr(self, "weight", value)

    def set_height(self, value):
        return setattr(self, "height", value)

    def set_hair_color(self, value):
        return setattr(self, "hair_color", value)

    def set_skin_color(self, value):
        return setattr(self, "skin_color", value)

    def compare_by_weight(self, person2):
        if person1.weight > person2.weight:
            print(f"{person1.name} the weight is greater than that of {person2.name}")
        else:
            print(f"{person2.name} the weight is greater than that of {person1.name}")

    def compare_by_height(self, person2):
        if person1.height > person2.height:
            print(
                f"{person1.name} {person1.surname} higher than {person2.name} {person2.surname}"
            )
        else:
            print(
                f"{person2.name} {person1.surname} higher than {person1.name} {person2.surname}"
            )

    def person_info(self):
        print(
            f"Person name: {self.name}, surname: {self.surname}, age: {self.age}, "
            f"weight: {self.weight} kg, height: {self.height} sm, "
            f"hair_color: {self.hair_color}, skin color: {self.skin_color}"
        )


person1 = Person("Mikolai", "Popov", 36, 93, 1.82, "silver", "white")
person1.set_name("Misha")
person1.set_surname("Petricov")
person1.person_info()
person2 = Person("Grisha", "Vinokur", 40, 90, 1.83, "black", "black")
person2.person_info()
Person.compare_by_weight(person1, person2)
Person.compare_by_height(person1, person2)


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
