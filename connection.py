import csv
import os

#DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'

def get_all_answers():

    input_file = csv.DictReader(open("sample_data/answer.csv", "r+", newline=''), fieldnames=None, restkey=None, restval='0')
    all_answers = [row for row in input_file]
    return all_answers

def get_all_questions():

    input_file = csv.DictReader(open("sample_data/question.csv", "r+", newline=''), fieldnames=None, restkey=None, restval='0')
    all_questions = [row for row in input_file]
    return all_questions

def save_question(question, fieldnames):
    with open("sample_data/question.csv", 'a') as inFile:
        writer = csv.DictWriter(inFile, fieldnames=fieldnames)
        writer.writerow(question)

def save_answer(answer, fieldnames):
    with open("sample_data/answer.csv", 'a') as inFile:
        writer = csv.DictWriter(inFile, fieldnames=fieldnames)
        writer.writerow(answer)