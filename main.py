from notebook import Notebook


def main():
    notebook = Notebook()

    notebook.add_note("Купити квіти")
    notebook.add_note("Сходити в магазин")
    notebook.add_note("Приготувати верерю")
    notebook.add_note("Зробити домашнє завдання")
    notebook.add_note("Зателефонувати лікарю")


    while True:
        print("\nМеню:")
        print("1. Додати нотатку")
        print("2. Обробити нотатку")
        print("3. Переглянути нотатки")
        print("4. Вийти")

        choice = input("Оберіть опцію (1-4): ")

        if choice == '1':
            note = input("Введіть текст нотатки: ")
            notebook.add_note(note)

        elif choice == '2':
            notebook.process_note()

        elif choice == '3':
            notebook.view_notes()

        elif choice == '4':
            print("Вихід з програми...")
            break

        else:
            print("Невірна опція, спробуйте ще раз!")


if __name__ == "__main__":
    main()