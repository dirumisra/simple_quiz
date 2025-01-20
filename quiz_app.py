# Main Application Logic in app.py

import random
from questions import questions

def ask_question(question_data):
    print(question_data['question'])
    for idx, option in enumerate(question_data["options"], 1):
        print(f"{idx}.{option}")
    user_answer = input("Your Answer: ")


    # Checking if the user answer is correct
    if question_data["options"][int(user_answer) - 1] == question_data["answer"]:
        return True
    return False

def main():
    score = 0
    random.shuffle(questions) # Shuffle the questions for randomness

    for question_data in questions:
        is_correct = ask_question(question_data)
        if is_correct:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question_data['answer']}\n")
    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    main()