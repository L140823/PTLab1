# -*- coding: utf-8 -*-
import pytest
import json
import tempfile
import os
from Types import DataType
from JsonDataReader import JsonDataReader


class TestJsonDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        new_data = {
            "Иванов Иван Иванович": {
                "математика": 92,
                "физика": 85
            },
            "Петров Петр Петрович": {
                "программирование": 95,
                "английский": 90
            }
        }

        expected_data = {
            "Иванов Иван Иванович": [
                ("математика", 92),
                ("физика", 85)
            ],
            "Петров Петр Петрович": [
                ("программирование", 95),
                ("английский", 90)
            ]
        }

        return json.dumps(new_data,
                          ensure_ascii=False,
                          indent=2), expected_data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType]
                          ) -> tuple[str, DataType]:
        with tempfile.NamedTemporaryFile(
            mode='w', encoding='utf-8', delete=False, suffix='.json'
        ) as f:
            f.write(file_and_data_content[0])
            temp_path = f.name

        yield temp_path, file_and_data_content[1]
        os.unlink(temp_path)

    def test_read_normal_data(self,
                              filepath_and_data: tuple[str, DataType]) -> None:
        file_content = JsonDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]

    def test_read_empty_file(self) -> None:
        with tempfile.NamedTemporaryFile(
            mode='w', encoding='utf-8', delete=False, suffix='.json'
        ) as f:
            f.write('{}')
            temp_path = f.name

        try:
            file_content = JsonDataReader().read(temp_path)
            assert file_content == {}
        finally:
            os.unlink(temp_path)

    def test_read_file_with_one_student(self) -> None:
        new_data = {
            "Сидоров Алексей": {
                "математика": 100
            }
        }

        expected_data = {
            "Сидоров Алексей": [
                ("математика", 100)
            ]
        }

        with tempfile.NamedTemporaryFile(
            mode='w', encoding='utf-8', delete=False, suffix='.json'
        ) as f:
            json.dump(new_data, f, ensure_ascii=False)
            temp_path = f.name

        try:
            file_content = JsonDataReader().read(temp_path)
            assert file_content == expected_data
        finally:
            os.unlink(temp_path)

    def test_read_file_with_multiple_subjects(self) -> None:
        new_data = {
            "Козлова Мария": {
                "математика": 85,
                "физика": 90,
                "химия": 88,
                "биология": 92
            }
        }

        expected_data = {
            "Козлова Мария": [
                ("математика", 85),
                ("физика", 90),
                ("химия", 88),
                ("биология", 92)
            ]
        }

        with tempfile.NamedTemporaryFile(
            mode='w', encoding='utf-8', delete=False, suffix='.json'
        ) as f:
            json.dump(new_data, f, ensure_ascii=False)
            temp_path = f.name

        try:
            file_content = JsonDataReader().read(temp_path)
            assert file_content == expected_data
        finally:
            os.unlink(temp_path)

    def test_read_file_not_found(self) -> None:
        reader = JsonDataReader()
        with pytest.raises(FileNotFoundError):
            reader.read("nonexistent_file.json")

    def test_read_invalid_json(self) -> None:
        invalid_json = "{ invalid json }"

        with tempfile.NamedTemporaryFile(
            mode='w', encoding='utf-8', delete=False, suffix='.json'
        ) as f:
            f.write(invalid_json)
            temp_path = f.name

        try:
            reader = JsonDataReader()
            with pytest.raises(json.JSONDecodeError):
                reader.read(temp_path)
        finally:
            os.unlink(temp_path)

    def test_read_structure_validation(self,
                                       filepath_and_data: tuple[str, DataType]
                                       ) -> None:
        file_content = JsonDataReader().read(filepath_and_data[0])

        # Проверяем структуру данных
        for student_name, subjects in file_content.items():
            assert isinstance(student_name, str)
            assert isinstance(subjects, list)
            for subject in subjects:
                assert isinstance(subject, tuple)
                assert len(subject) == 2
                assert isinstance(subject[0], str)  # название предмета
                assert isinstance(subject[1], int)  # оценка
