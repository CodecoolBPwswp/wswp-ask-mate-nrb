import csv
import os

#DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'

def get_all_answers():
    input_file = csv.DictReader(open("sample_data/answer.csv"))
    all_answers = [row for row in input_file]

    return all_answers

def get_all_questions():
    input_file = csv.DictReader(open("sample_data/question.csv"))
    all_questions = [row for row in input_file]

    return all_questions