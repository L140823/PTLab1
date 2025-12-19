from Types import DataType


class StudentFinder:
    def find_student_with_high_scores(self, data: DataType) -> str:
        qualified_students = self._find_qualified_students(data)

        if not qualified_students:
            return "Студентов с 90+ баллами по двум дисциплинам не найдено"

        return qualified_students[0]

    def _find_qualified_students(self, data: DataType) -> list[str]:
        qualified = []

        for student_name, subjects in data.items():
            high_score_count = self._count_high_scores(subjects)
            if high_score_count >= 2:
                qualified.append(student_name)

        return qualified

    def _count_high_scores(self, subjects: list[tuple[str, int]]) -> int:
        count = 0
        for subject_name, score in subjects:
            if score >= 90:
                count += 1
        return count

    def get_all_qualified_students(self, data: DataType) -> list[str]:
        qualified_students = self._find_qualified_students(data)

        if not qualified_students:
            return "Студентов с 90+ баллами по двум дисциплинам не найдено"

        return qualified_students
