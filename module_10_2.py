import threading
from time import sleep

# Глобальное количество врагов для всех рыцарей
total_enemies = 100


# Класс Knight, наследующий от Thread
class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name  # Имя рыцаря
        self.power = power  # Сила рыцаря
        self.days = 0  # Количество дней сражений

    def run(self):
        global total_enemies  # Доступ к глобальному количеству врагов
        print(f"{self.name}, на нас напали!")

        while total_enemies > 0:
            self.days += 1
            sleep(1)  # Ждём 1 день (1 секунду)
            total_enemies -= self.power

            # Если врагов стало меньше 0, обнуляем их
            if total_enemies < 0:
                total_enemies = 0

            print(f"{self.name} сражается {self.days} день(дня/дней)..., осталось {total_enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} день(дня/дней)!")


# Создаем двух рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запускаем потоки
first_knight.start()
second_knight.start()

# Ожидаем завершения обоих потоков
first_knight.join()
second_knight.join()

# Выводим строку об окончании битв
print("Сражение завершилось. Все враги повержены!")
