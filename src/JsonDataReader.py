# -*- coding: utf-8 -*-
import json
from Types import DataType
from DataReader import DataReader


class JsonDataReader(DataReader):

    def read(self, path: str) -> DataType:
        with open(path, 'r', encoding='utf-8') as file:
            new_data = json.load(file)

        students: DataType = {}
        for student_name, subjects in new_data.items():
            students[student_name] = []
            for subject_name, score in subjects.items():
                students[student_name].append((subject_name, score))

        return students
