import pytest
from Types import DataType
from StudentFinder import StudentFinder


class TestStudentFinder:
    def test_find_student_with_high_scores_single_qualified(self):
        data = {
            "Иванов Иван": [
                ("математика", 92), ("физика", 85)
            ],
            "Петров Петр": [
                ("математика", 95), ("физика", 91)
            ],
            "Сидоров Алекс": [
                ("химия", 88), ("биология", 87)
            ]
        }
        finder = StudentFinder()
        result = finder.find_student_with_high_scores(data)
        assert result == "Петров Петр"

    def test_find_student_with_high_scores_multiple_qualified(self):
        data = {
            "Иванов Иван": [
                ("математика", 94), ("физика", 92)
            ],
            "Петров Петр": [
                ("математика", 95), ("физика", 91)
            ],
            "Сидоров Алекс": [
                ("химия", 96), ("биология", 93)
            ]
        }
        finder = StudentFinder()
        result = finder.find_student_with_high_scores(data)
        assert result in ["Иванов Иван", "Петров Петр", "Сидоров Алекс"]

    def test_find_student_with_high_scores_none_qualified(self):
        data = {
            "Иванов Иван": [
                ("математика", 89), ("физика", 85)
            ],
            "Петров Петр": [
                ("математика", 88), ("физика", 87)
            ]
        }
        finder = StudentFinder()
        result = finder.find_student_with_high_scores(data)
        expected = "Студентов с 90+ баллами по двум дисциплинам не найдено"
        assert result == expected

    def test_find_student_with_high_scores_exactly_two_high_scores(self):
        data = {
            "Иванов Иван": [
                ("математика", 90), ("физика", 90), ("химия", 85)
            ]
        }
        finder = StudentFinder()
        result = finder.find_student_with_high_scores(data)
        assert result == "Иванов Иван"

    def test_find_student_with_high_scores_more_than_two_high_scores(self):
        data = {
            "Иванов Иван": [
                ("математика", 95), ("физика", 92), ("химия", 90)
            ]
        }
        finder = StudentFinder()
        result = finder.find_student_with_high_scores(data)
        assert result == "Иванов Иван"

    def test_find_student_with_high_scores_empty_data(self):
        data = {}
        finder = StudentFinder()
        result = finder.find_student_with_high_scores(data)
        expected = "Студентов с 90+ баллами по двум дисциплинам не найдено"
        assert result == expected

    def test_count_high_scores(self):
        finder = StudentFinder()
        subjects = [
            ("математика", 95), ("физика", 89), ("химия", 90)
        ]
        count = finder._count_high_scores(subjects)
        assert count == 2

    def test_get_all_qualified_students(self):
        data = {
            "Иванов Иван": [
                ("математика", 94), ("физика", 92)
            ],
            "Петров Петр": [
                ("математика", 95), ("физика", 91)
            ],
            "Сидоров Алекс": [
                ("химия", 88), ("биология", 87)
            ]
        }
        finder = StudentFinder()
        qualified = finder.get_all_qualified_students(data)
        assert set(qualified) == {"Иванов Иван", "Петров Петр"}
     
 
