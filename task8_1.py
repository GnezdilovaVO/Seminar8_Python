# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
# Информация о человеке:
#     Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода. 
#     Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
#     Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
#     Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. 
#           Берем первое совпадение по фамилии.
#     Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
#     Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе
# Усложнение.
# - Сделать тесты для функций
# - Разделить на model-view-controller

# user = ["firstname", "lastname", "phone", "description"]
# phone_dir = {1: ["firstname", "lastname", "phone", "description"], 2: ["firstname", "lastname", "phone", "description"]}
from os.path import join, abspath, dirname
def input_user() -> dict:
    user = list()
    user.append(input("Input first name: "))
    user.append(input("Input second name: "))
    user.append(input("Input phone: "))
    user.append(input("Input description: "))
    return user
def create(phone_dir_local: dict, user: list, idc: int) -> dict:
    idc += 1
    phone_dir_local[idc] = user
    return phone_dir_local, idc
def export_phone_dir(phone_dir: dict, file_name: str):
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name + ".txt")
    with open (full_name, mode = "w", encoding = "UTF-8") as file:
        for idc, user in phone_dir.items():
            file.write(f"{idc}:{user[0]}:{user[1]}:{user[2]}:{user[3]}\n")
def search_user(phone_dir: dict, searching: str) -> int:
    for idc, user in phone_dir.items():
        if user[0].startswith(searching):
            return idc
def print_dect(phone_dir: dict):
    for idc, user in phone_dir.items():
        print(f"{idc}:{user[0]}:{user[1]}:{user[2]}:{user[3]}")

def import_file(phone_dir: dict, file_name: str, idc: int) -> dict:
    MAIN_DIR = abspath(dirname(__file__))
    full_name_import = join(MAIN_DIR, file_name + ".txt")
    with open (full_name_import, mode = "r", encoding="UTF-8") as file_import:
        for line in file_import:
            idc += 1
            phone_dir[idc] =line
    return phone_dir, idc
def delete_phone(phone_dir: dict, idc: int) -> dict:
    phone_dir.pop(idc)
    return phone_dir
def update_phone(phone_dir: dict, idc: int, newdata: str, olddata: int ) -> dict:
    for idx, user in phone_dir.items():
        if idx == idc:
            user[olddata] = newdata
    return phone_dir



def menu():
    key_count = 0
    phone_dir = dict()
    print("Введите 1 если хотите записать пользователя: ")
    print("Введите 2 если хотите распечатать справочник: ")
    print("Введите 3 если хотите перезаписать в файл: ")
    print("Введите 4 если хотите использовать фильтр: ")
    print("Введите 5 если хотите импортировать из файла: ")
    print("Введите 6 если хотите удалить из справочника: ")
    print("Введите 7 если хотите изменить данные в справочнике: ")
    while True:
        num = int(input("Выбиерите операцию: "))
        if num == 0: break
        if num == 1: 
            user = input_user()
            phone_dir, key_count = create(phone_dir, user, key_count)
        if num == 2:
            print_dect(phone_dir)
        if num == 3:
            file_name = input("Введите имя файла: ")
            export_phone_dir(phone_dir, file_name)
        if num == 4:
            searchname = input("Введите фамилию: ")
            search_user(phone_dir, searchname)
        if num == 5:
            file_name_import = input("Введите имя импорт-файла: ")
            phone_dir, key_count = import_file(phone_dir, file_name_import, key_count)
            print(phone_dir)
        if num == 6:
            searchname = input("Введите фамилию: ")
            key_delete = search_user(phone_dir, searchname)
            phone_dir = delete_phone(phone_dir, key_delete)
            print(phone_dir)
        if num == 7:
            searchname = input("Введите фамилию: ")
            key_update = search_user(phone_dir, searchname)
            change_data = int(input("Введите 0, 1, 2, 3 для изменения данных: "))
            new_data = input("Введите новые данные: ")
            phone_dir = update_phone(phone_dir, key_update, new_data, change_data)
            print(phone_dir)



    

menu()
# key_count = 0
# phone_dir = dict()
# user1 = ["firstname", "lastname", "phone", "description"]
# user2 = ["firstname", "lastname", "phone", "description"]
# phone_dir, key_count = create(phone_dir, user1, key_count)
# phone_dir, key_count = create(phone_dir, user2, key_count)
# print(phone_dir)
# export_phone_dir(phone_dir, "phones")
# phonedir = {1: ["Иванов", "Иван", "+7(ххх)ххх-хх-хх", "description_Иванов"],
# 2: ["Петров", "Петр", "+7(---)ххх-хх-хх", "description_Петров"],
# 3: ["Соколов", "Илья", "+7(---)---------", "description_Соколов"],
# 4: ["Павельев", "Андрей", "+7(***)***-**-**", "description_Павельев"],
# 5: ["Пешехов", "Антон", "+7+++++++++++", "description_Пешехов"],
# 6: ["Сааков", "Илья", "+7(+++)+++-++-++", "description_Сааков"]}
# print(search_user(phonedir, "Пеш"))
