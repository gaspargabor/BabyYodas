import csv
import time
import os
import connection
import database_common
question_route = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__), "sample_data/question.csv"))
answer_route = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__), "sample_data/answer.csv"))
Q_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
A_HEADER = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']




"""def get_data(route, q_a_id=None):
    returns a list of dictionaries from the given file (question or answer) if no id given, returns a dictionary of
    a single question or answer if id available
    all_data = connection.get_data_from_csv(route)
    qs_or_as = []
    for row in all_data:
        q_or_a = dict(row)
        if q_a_id is not None and q_a_id == q_or_a['id']:
            return q_or_a
        qs_or_as.append(q_or_a)
    return qs_or_as"""

"""def get_answers_for_question(question_id):
    returns a list of dictionaries - all the answers for the given question id
    answers = connection.get_data_from_csv(answer_route)
    answers_for_question = []
    for answer in answers:
        if answer['question_id'] == question_id:
            answers_for_question.append(answer)
    return answers_for_question"""


"""def save_updated_data(route, header, updated_data):
    connection.write_datas_to_csv(route, header, updated_data)"""


"""def get_new_id(filename):
    generates a new id for the new entries
    all_q_or_a = get_data(filename)
    if len(all_q_or_a) == 0:
        return 1
    return str(int(all_q_or_a[-1]['id'])+1)"""


"""def get_question(filename, question_id):
    #why is this here even
    return get_data(filename, question_id)"""


"""def get_answers_for_question(filename, question_id):
    #should delete this too
    answers = []
    all_answers = get_data(filename)
    for answer in all_answers:
        if question_id == answer['question_id']:
            answers.append(answer)
    return answers"""


"""def add_new_question(question):
    #adds new question to question.csv
    question['id'] = get_new_id(filename=question_route)
    question['submission_time'] = int(time.time())
    add_new_q_or_a_to_file(question_route, Q_HEADER, question, True)


def edit_question(question):
    add_new_q_or_a_to_file(question_route, Q_HEADER, question, False)


def edit_answer(answer):
    add_new_q_or_a_to_file(answer_route, A_HEADER, answer, False)


def add_new_answer(answer, question_id):
    answer['id'] = get_new_id(filename=answer_route)
    answer['submission_time'] = int(time.time())
    answer['question_id'] = question_id

    add_new_q_or_a_to_file(answer_route, A_HEADER, answer, True)"""


"""def add_new_q_or_a_to_file(filename, header, q_or_a, append=True):
    qs_or_as = get_data(filename)
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
        for row in qs_or_as:
            if not append:
                if row['id'] == q_or_a['id']:
                    row = q_or_a
            writer.writerow(row)
        if append:
            writer.writerow(q_or_a)"""



"""def sort_qs_or_as(list_to_sort, criteria):
    if criteria in ['view_number', 'vote_number']:
        sorted_list = sorted(list_to_sort, key=lambda i: int(i[criteria]), reverse=True)
    elif criteria in ['submission_time']:
        sorted_list = sorted(list_to_sort, key=lambda i: i[criteria], reverse=True)
    else:
        sorted_list = sorted(list_to_sort, key=lambda i: i[criteria], reverse=False)
    return sorted_list"""


"""def delete_question(filename, question_id):
    #deletes a question based on ID
    questions = get_data(filename)
    for question in questions:
        if question_id == question['id']:
            questions.remove(question)
    return questions"""


"""def delete_answers_for_question(filename, question_id):
    #deletes the answers of the deleted question based on the question ID
    answers = get_data(filename)
    iterations = 0
    while iterations < len(answers):
        for answer in answers:
            if question_id == answer['question_id']:
                answers.remove(answer)
        iterations += 1
    return answers"""
