
def read_txt(filename):
    phone_book=[]

    fields=['Фамилия','Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding= 'utf-8') as phb:

        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
        return phone_book
    
def write_txt(filename , phone_book):
       
    with open('phonebook.txt','w' ,encoding='utf-8') as phout:
            
        for i in range(len(phone_book)):
           s=''
           for v in phone_book[i].values():
               s+=v+','
        phout.write(f'{s[:-1]}\n')

def show_menu():
    print('1. Распечатать справочник',
          '2. Найти телефон по фамилии',
          '3. Изменить номер телефона',
          '4. Удалить запись',
          '5. Найти абонента по номеру телефона',
          '6. Добавить абонента в справочник',
          '7. Закончить работу', sep = '\n')
    choice=int(input())
    return choice

def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phonebook (2).csv')
    while (choice!=7):
        if choice ==1:
            print(phone_book)


#Функция для добавления нового контакта в телефонный справочник
def add_contact():
    name = input("Введите имя контакта: ")
    number = input("Введите номер телефона: ")
    phonebook[name] = {"номер": number}
    print("Контакт успешно добавлен")

# Функция для изменения данных контакта
def edit_contact():
    name = input("Введите имя или фамилию контакта: ")
    if name in phonebook:
        number = input("Введите новый номер телефона: ")
        phonebook[name] = {"номер": number}
        print("Контакт успешно изменен")
    else:
        print("Контакт не найден")

# Функция для удаления контакта из телефонный справочник
def delete_contact():
    name = input("Введите имя или фамилию контакта: ")
    if name in phonebook:
        del phonebook[name]
        print("Контакт успешно удален")
    else:
        print("Контакт не найден")

# Главная функция для работы с телефонным справочником
def phonebook_app():
    while True:
        action = input("\nВыберите действие:\n1 - Добавить контакт\n2 - Изменить контакт\n3 - Удалить контакт\n4 - Вывести список контактов\n5 - Выйти из приложения\n")
        if action == "1":
            add_contact()
        elif action == "2":
            edit_contact()
        elif action == "3":
            delete_contact()
        elif action == "4":
            for name, data in phonebook.items():
                print("{0}: {1}, {2}".format(name, data["номер"]))
        elif action == "5":
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Попробуйте снова")
phonebook_app()







    