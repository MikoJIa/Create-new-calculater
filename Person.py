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
        self.name = value

    def set_surname(self, value):
        self.surname = value

    def set_age(self, value):
        self.age = value

    def set_weight(self, value):
        self.weight = value

    def set_height(self, value):
        self.height = value

    def set_hair_color(self, value):
        self.hair_color = value

    def set_skin_color(self, value):
        self.skin_color = value

    def __eq__(self, obj):
        if isinstance(obj, (tuple, Person)):
            return all((self.weight == obj.weight, self.height == obj.height, self.age == obj.age))
        raise TypeError('Операнды справа должен иметь тип  Person')

    def __lt__(self, obj):
        if isinstance(obj, Person):
            return all((self.weight < obj.weight, self.height < obj.height, self.age < obj.age))
        raise TypeError('Операнды справа должен иметь тип  Person')

    def __gt__(self, obj):
        if isinstance(obj, Person):
            return all((self.weight > obj.weight, self.height > obj.height, self.age > obj.age))
        raise TypeError('Операнды справа должен иметь тип  Person')

    def person_info(self):
        print(
            f"Person name: {self.name}, surname: {self.surname}, age: {self.age}, "
            f"weight: {self.weight} kg, height: {self.height} sm, "
            f"hair_color: {self.hair_color}, skin color: {self.skin_color}"
        )


# person1 = Person("Mikolai", "Popov", 36, 89, 1.90, "silver", "white")
# person1.person_info()
# person1.height = 1.93
# person2 = Person("Grisha", "Vinokur", 40, 90, 1.83, "black", "black")
# person3 = Person('Volodya', 'Pupkin', 34, 82, 1.85, 'silver', 'white')
# person4 = Person('Petya', 'Petrov', 40, 91, 1.87, 'black', 'white')
# person5 = Person('Sasha', 'Shushkevich', 40, 90, 1.87, 'yellow', 'black')
#
# print(person5 == (40, 90, 1.90))
# передача через кортеж
# print(person5 == 90)
# print(person3 < person2)
# print(person5 > person4)
# Person.get_print_weight_height_age(person1, person2)
# Person.__eq__()



