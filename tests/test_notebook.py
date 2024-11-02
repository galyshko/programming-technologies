import unittest
from notebook import Notebook
import queue
from xmlrunner import XMLTestRunner  # Імпорт XMLTestRunner

class TestNotebook(unittest.TestCase):

    def setUp(self):
        self.notebook = Notebook()

    def test_add_note(self):
        self.notebook.add_note("Купити хліб")
        self.assertEqual(self.notebook.notes_queue.qsize(), 1)
        self.notebook.add_note("Зателефонувати другу")
        self.assertEqual(self.notebook.notes_queue.qsize(), 2)

    def test_process_note(self):
        self.notebook.add_note("Купити хліб")
        self.notebook.add_note("Зателефонувати другу")

        self.notebook.process_note()
        self.assertEqual(self.notebook.notes_queue.qsize(), 1)

        self.notebook.process_note()
        self.assertEqual(self.notebook.notes_queue.qsize(), 0)

    def test_process_note_empty_queue(self):
        with self.assertRaises(queue.Empty):
            self.notebook.process_note()

    def test_add_empty_note(self):
        with self.assertRaises(ValueError):
            self.notebook.add_note("")

    def test_view_notes(self):
        self.notebook.add_note("Купити хліб")
        self.notebook.add_note("Зателефонувати другу")

        notes = []
        temp_queue = self.notebook.notes_queue.queue
        for note in temp_queue:
            notes.append(note)

        self.assertIn("Купити хліб", notes)
        self.assertIn("Зателефонувати другу", notes)
        self.assertEqual(len(notes), 2)

if __name__ == "__main__":
    # Створення каталогу, якщо він не існує
    import os
    if not os.path.exists("test/result"):
        os.makedirs("test/result")

    # Запуск тестів з використанням XMLTestRunner
    with open("test/result/TEST-results.xml", "wb") as output:
        runner = XMLTestRunner(output=output, verbosity=2)
        runner.run(unittest.TestLoader().loadTestsFromTestCase(TestNotebook))
