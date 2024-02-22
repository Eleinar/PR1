class Person:
    def __init__(self, head_center, head_radius, body_height, body_width, arm_length, arm_corner, leg_length, leg_corner): # конструктор
        self.__head_center = head_center # центр головы
        self.__head_radius = head_radius # радиус головы
        self.__body_top_left = head_center # левый верхний угол туловища присоединяется к центру головы
        self.__body_height = body_height # высота туловища
        self.__body_width = body_width # ширина туловища
        self.__arm_length = arm_length # длинна рук
        self.__arm_corner = arm_corner # угол наклона рук
        self.__leg_length = leg_length # длинна ног
        self.__leg_corner = leg_corner # угол наклона ног

    def height(self): # функция для измерения роста
        # Высота = высота туловища + длина ног + диаметр головы
        return self.__body_height + self.__leg_length + (self.__head_radius * 2)
    
    def get_head(self): # геттер головы
        return self.__head_radius
    
    def get_body_height(self): # геттер для высоты туловища
        return self.__body_height
    
    def get_body_width(self): # геттер для ширины туловища
        return self.__body_width
    
    def get_arm_length(self): # геттер для длинны рук
        return self.__arm_length
    
    def get_arm_corner(self): # геттер для угла наклона рук
        return self.__arm_corner
    
    def get_leg_corner(self): # геттер для угла наклона ног
        return self.__leg_corner

    def get_leg_length(self): # геттер для длинны ног
        return self.__leg_length
    
    def setHead(self, head_radius): # сеттер для головы
        self.__head_radius = head_radius
    
    def setBody(self, body_height, body_width): # сеттер для туловища
       self.__body_height = body_height
       self.__body_width = body_width
    
    def setArms(self, arm_length, arm_corner): # сеттер для рук
       self.__arm_length = arm_length
       self.__arm_corner = arm_corner
    
    def setLegs(self, leg_length, leg_corner): # сеттер для ног
       self.__leg_length = leg_length
       self.__leg_corner = leg_corner

    def body_square(self): # метод для получения площади туловища
        return self.__body_height * self.__body_width # возвращается произведение высоты туловища на его ширину
    
    def show(self): # метод, выводящий все параметры объекта
        print(f"Центр головы: {self.__head_center}")
        print(f"Радиус головы: {self.__head_radius}")
        print(f"Начало туловища: {self.__body_top_left}")
        print(f"Высота туловища: {self.__body_height}")
        print(f"Ширина туловища: {self.__body_width}")
        print(f"Длинна рук: {self.__arm_length}")
        print(f"Угол наклона рук: {self.__arm_corner}")
        print(f"Длинна ног: {self.__leg_length}")
        print(f"Угол наклона ног: {self.__leg_corner}")


class Cyborg(Person): # Класс Cyborg-убийца наследуется от класса Person 

    def __init__(self, head_center, head_radius, body_height, body_width, arm_length, arm_corner, leg_length, leg_corner, exoskeleton):
        super().__init__(head_center, head_radius, body_height, body_width, arm_length, arm_corner, leg_length, leg_corner)
        self.__head_center = head_center # центр головы
        self.__head_radius = head_radius # радиус головы
        self.__body_top_left = head_center # левый верхний угол туловища присоединяется к центру головы
        self.__body_height = body_height # высота туловища
        self.__body_width = body_width # ширина туловища
        self.__arm_length = arm_length # длинна рук
        self.__arm_corner = arm_corner # угол наклона рук
        self.__leg_length = leg_length # длинна ног
        self.__leg_corner = leg_corner # угол наклона ног

        if(exoskeleton >= self.body_square): # проверка условия для выставления значения экзоскелета
            self.__exoskeleton = exoskeleton
        else:
            self.__exoskeleton = self.body_square

    def set_exoskeleton(self, exoskeleton): # метод для установки значения экзоскелета
        if(exoskeleton >= self.body_square):
            self.__exoskeleton = exoskeleton
        else:
            self.__exoskeleton = self.body_square
    
    def get_exoskeleton(self):
        return self.__exoskeleton
    
    def show(self): # метод, переопределяющий родительский класс
        super().show()
        print(f"Мощность экзоскелета: {self.__exoskeleton}")
        
