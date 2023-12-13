import sqlite3

def get_object_info(object_id):
    # Установка соединения с базой данных
    conn = sqlite3.connect('sqllite/database.db')
    cursor = conn.cursor()

    # Подготовка SQL запроса без вставки значения напрямую
    query = "SELECT * FROM objects WHERE id = ?"

    # Выполнение запроса с использованием привязки параметров
    cursor.execute(query, (object_id,))

    # Получение результата и вывод информации об объекте
    result = cursor.fetchone()
    if result is not None:
        object_name = result[1]
        object_description = result[2]
        print("Имя объекта:", object_name)
        print("Описание объекта:", object_description)
    else:
        print("Объект не найден")

    # Закрытие соединения с базой данных
    conn.close()

# Пример использования функции
object_id = input("Введите ID объекта: ")
get_object_info(object_id)