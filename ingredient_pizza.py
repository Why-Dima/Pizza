class Name:
    #создаем родительский класс в котором будет храниться title
    def __init__(self, title):
        self.title = title


class Product(Name):
    
    def __init__(self, title, calorific, cost):
        super().__init__(title)
        self.calorific = calorific
        self.cost = cost


class Ingredient(Product):      

    def __init__(self, title, calorific, cost=1, weight=1):
        #проверям вводимый вес, он должен быть положительным иначе выводим искусственное исключение
        if Ingredient.check_weight(weight):
            super().__init__(title, calorific, cost)
            self.__weight = weight
        else:
            raise ValueError
    
    def __str__(self):
        return '{} {} {} {}'.format(self.title, self.calorific, self.cost, self.weight)
    #создаем метод дял подсчета калорий
    def get_colorific(self):
        return self.weight / 100 * self.calorific
    #создаем метод для подсчета стоимости
    def get_cost_price(self):
        return self.weight / 100 * self.cost  
    # делаем метод статичным
    @staticmethod
    def check_weight(weight):
        return weight > 0
    #превращаем метод в свойства
    @property
    def weight(self):
        return self.__weight
    #создаем сетер для обновления свойств, чтобы вес мог меняться
    @weight.setter
    def weight(self, weight):
        if Ingredient.check_weight(weight):
            self.__weight
        else:
            raise ValueError


class Pizza(Name):
    # в конструкторе прописываем title со списком ингредиентов
    def __init__(self, title, ingredients):
        super().__init__(title)
        self.ingredients = ingredients

    def __str__(self):
        return f'{self.title} ({self.get_colorific()} kkal) - {self.get_cost_price()} руб.'
    # следуя полиморфизму создаем метод для подсчета калорий всей пиццы
    def get_colorific(self):
        total_calorific = 0
        for ingredient in self.ingredients:
            total_calorific += ingredient.get_colorific()
        return total_calorific 
    # следуя полиморфизму создаем метод для подсчета общей стоимости
    def get_cost_price(self):
        total_cost = 0
        for cost in self.ingredients:
            total_cost += cost.get_cost_price()
        return total_cost

    @staticmethod
    def check_title(title):
        if title:
            return True
        else:
            return False

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if Pizza.check_title(title):
            self.__title = title
        else:
            raise ValueError


# Создаем продукты с указанием названия, калорийности продукта и его себестоимости
dough_product = Product('Тесто', 200, 20)
tomato_product = Product('Помидор', 100, 50)
cheese_product = Product('Сыр', 100, 120)

# Из продуктов создаем ингредиенты. Для каждого ингредиента указываем продукт, 
# из которого он состоит и вес продукта
dough_ingredient = Ingredient('Тесто', 200, 20, 100)
tomato_ingredient = Ingredient('Помидор',100, 50, 100)
print(tomato_ingredient.get_cost_price())#пример подсчета калорий
cheese_ingredient = Ingredient('Сыр',100, 120, 100)
# Из ингредиентов создаем пиццу
pizza_margarita = Pizza('Маргарита', [dough_ingredient, tomato_ingredient, cheese_ingredient])
# Выводим экземпляр пиццы
print(pizza_margarita)