import unittest
import os
import queue
from main import Notebook
import xmlrunner


class TestNotebook(unittest.TestCase):

    def setUp(self):
        #Ця функція виконується перед кожним тестом і створює новий екземпляр Notebook
        self.notebook = Notebook()

    def test_add_note(self):
        #Тестуємо додавання нотатки в чергу
        self.notebook.add_note("Купити хліб")
        self.assertEqual(self.notebook.notes_queue.qsize(), 1)
        self.notebook.add_note("Зателефонувати другу")
        self.assertEqual(self.notebook.notes_queue.qsize(), 2)

    def test_process_note(self):
       #Тестуємо обробку (видалення) нотатки з черги
        self.notebook.add_note("Купити хліб")
        self.notebook.add_note("Зателефонувати другу")

        # Обробляємо одну нотатку
        self.notebook.process_note()
        self.assertEqual(self.notebook.notes_queue.qsize(), 1)

        # Обробляємо ще одну нотатку
        self.notebook.process_note()
        self.assertEqual(self.notebook.notes_queue.qsize(), 0)

    # Перевірка на виникнення виключення
    def test_process_note_empty_queue(self):
        #Тестуємо обробку нотатки, коли черга порожня
        with self.assertRaises(queue.Empty):
            self.notebook.process_note()

    # Тест на негативний сценарій
    @unittest.expectedFailure
    def test_add_empty_note(self):
        #Тестуємо додавання пустої нотатки.
        with self.assertRaises(ValueError):
            self.notebook.add_note("")  # Припускаємо, що додавання пустої нотатки має піднімати ValueError
    # Для того, щоб все тести пройшли успішно, потрібно зняти коментарі у функції add_note


    def test_view_notes(self):
       #Тестуємо перегляд всіх нотаток у черзі
        self.notebook.add_note("Купити хліб")
        self.notebook.add_note("Зателефонувати другу")

        # Створюємо тимчасовий список для перевірки
        notes = []

        temp_queue = self.notebook.notes_queue.queue
        for note in temp_queue:
            notes.append(note)

        self.assertIn("Купити хліб", notes)
        self.assertIn("Зателефонувати другу", notes)
        self.assertEqual(len(notes), 2)


if __name__ == "__main__":
    # Перевірка наявності каталогу для результатів і його створення
    if not os.path.exists('test-reports'):
        os.makedirs('test-reports')

    # Запуск тестів через XMLTestRunner без виклику unittest.main()
    with open('test-reports/test_results.xml', 'wb') as output:
        runner = xmlrunner.XMLTestRunner(output=output)
        unittest.main(testRunner=runner, exit=False)