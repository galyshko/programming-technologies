import queue

class Notebook:
    def __init__(self):
        # Ініціалізуємо чергу для зберігання нотаток
        self.notes_queue = queue.Queue()

    def add_note(self, note):
        #Додає нову нотатку до черги
        #if not note:  # Перевірка на пусту нотатку
            #raise ValueError("Нотатка не може бути пустою")
        self.notes_queue.put(note)
        print(f"Нотатка додана: {note}")

    def process_note(self):
        #Обробляє та видаляє першу нотатку в черзі
        try:
            note = self.notes_queue.get_nowait()  # Отримує нотатку без блокування
            print(f"Обробка нотатки: {note}")
        except queue.Empty:
            print("Черга порожня, немає нотаток для обробки")
            raise queue.Empty  # Піднімаємо виключення queue.Empty

    def view_notes(self):
        #Переглядає всі нотатки в черзі без їх видалення
        if self.notes_queue.empty():
            print("Немає нотаток для відображення")
        else:
            print("\n Нотатки в черзі:")
            temp_queue = queue.Queue()
            while not self.notes_queue.empty():
                note = self.notes_queue.get()
                print(f"- {note}")
                temp_queue.put(note)
            self.notes_queue = temp_queue  # Повертаємо нотатки назад у чергу
