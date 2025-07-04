#Делаем програму ToDo List
tasks = []

def show_tasks():

    if not tasks:
        print("Список завдань порожній.")
    else:
        print("\nСписок завдань:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def add_task():

    task = input("Введіть нове завдання: ").strip()
    if task:
        tasks.append(task)
        print("Завдання додано.\n")
    else:
        print("Завдання не може бути порожнім.\n")

def delete_task():

    show_tasks()
    if not tasks:
        return

    try:
        task_number = int(input("Введіть номер завдання для видалення: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f"Завдання \"{removed}\" видалено.\n")
        else:
            print("Неправильний номер завдання.\n")
    except ValueError:
        print("Будь ласка, введіть коректне число.\n")

def edit_task():

    show_tasks()
    if not tasks:
        return

    try:
        task_number = int(input("Введіть номер завдання для редагування: "))
        if 1 <= task_number <= len(tasks):
            new_text = input("Введіть новий текст завдання: ").strip()
            if new_text:
                old_task = tasks[task_number - 1]
                tasks[task_number - 1] = new_text
                print(f"Завдання \"{old_task}\" змінено на \"{new_text}\".\n")
            else:
                print("Текст завдання не може бути порожнім.\n")
        else:
            print("Неправильний номер завдання.\n")
    except ValueError:
        print("Будь ласка, введіть коректне число.\n")

def main():

    while True:
        print("Меню:")
        print("1. Переглянути завдання")
        print("2. Додати завдання")
        print("3. Видалити завдання")
        print("4. Редагувати завдання")
        print("5. Вийти")

        choice = input("Виберіть дію (1-5): ").strip()

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            edit_task()
        elif choice == '5':
            print("Дякую за використання ToDo List!")
            break
        else:
            print("Невірний вибір. Попробуйте ще раз.\n")
if __name__ == "__main__":
    main()
