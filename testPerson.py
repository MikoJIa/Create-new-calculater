from Person import Person
import pytest

# @pytest.mark.parametrize('name, surname, age, weight, height, hair_color, skin_color', [
#     ('Bob', 'Willson', 40, 90, 1.80, 'black', 'white')
# ])
# def test__init__(name, surname, age, weight, height, hair_color, skin_color):
def test__init__():
        '''Проверяем полные данные о человеке'''
        person = Person('Bob', 'Willson', 40, 90, 1.80, 'black', 'white')
        assert person.name == 'Bob'
        assert person.surname == 'Willson'
        assert person.age == 40
        assert person.weight == 90
        assert person.height == 1.80
        assert person.hair_color == 'black'
        assert person.skin_color == 'white'


person1 = Person("Mikolai", "Popov", 40, 90, 1.90, "silver", "white")
person2 = Person("Grisha", "Vinokur", 40, 90, 1.90, "black", "black")


def test_compare_by_age():
    '''Сравниваем два экземпляра'''
    assert person1 == person2