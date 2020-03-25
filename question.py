import mysql.connector

class Question:
    def __init__(self, text, choices, correct):
        self.text = text
        self.choices = choices
        self.correct = correct

def setupQuestions(cursor):
    questions = []
    cursor.execute("SELECT * FROM audrey_trivia")
    result = cursor.fetchall()
    for q in result:
        questions.append(Question(
            q[1],
            q[2], q[3], q[4], q[5], 
            q[6]
        ))