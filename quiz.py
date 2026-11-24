questions = [
    {
        "question": "1. Which language is used for Python development?",
        "options": ["A. HTML", "B. Python", "C. CSS", "D. Java"],
        "answer": "B"
    },
    {
        "question": "2. Which function is used to display output in Python?",
        "options": ["A. input()", "B. print()", "C. type()", "D. len()"],
        "answer": "B"
    },
    {
        "question": "3. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    },
    {
        "question": "4. Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Float", "D. Boolean"],
        "answer": "D"
    },
    {
        "question": "5. Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. class", "D. return"],
        "answer": "B"
    }
]

def display_question(question_data):
    print("\n" + question_data["question"])

    for option in question_data["options"]:
        print(option)

def get_user_answer():
    while True:
        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer in ["A", "B", "C", "D"]:
            return user_answer
        else:
            print("Invalid answer! Please enter A, B, C, or D.")

def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
        return True

    else:
        print(f"Wrong - correct answer is {correct_answer}.")
        return False

def calculate_percentage(score, total_questions):
    return (score / total_questions) * 100

def start_quiz():
    score = 0
    total_questions = len(questions)

    print("===== WELCOME TO THE PYTHON QUIZ =====")
    print(f"Total Questions: {total_questions}")

    for question_data in questions:
        display_question(question_data)

        user_answer = get_user_answer()
        correct_answer = question_data["answer"]

        if check_answer(user_answer, correct_answer):
            score += 1

    percentage = calculate_percentage(score, total_questions)

    print("\n===== QUIZ RESULTS =====")
    print(f"Your Score: {score}/{total_questions}")
    print(f"Your Percentage: {percentage:.2f}%")

start_quiz()
