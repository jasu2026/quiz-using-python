import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question['text'])
        for i, option in enumerate(question['options'], 1):
            print(f"{i}. {option}")
        user_answer = input("Your answer (enter the number): ")
        return int(user_answer) - 1  

    def evaluate_answer(self, question, user_choice):
        if question['options'][user_choice] == question['correct']:
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Incorrect! The correct answer is: {question['correct']}\n")

    def run_quiz(self):
        for question in self.questions:
            user_choice = self.display_question(question)
            self.evaluate_answer(question, user_choice)

        print(f"Quiz completed! Your final score is: {self.score}/{len(self.questions)}")

        if self.score == len(self.questions):
            congratulations_symbol = "👏"
            print(f"Congratulations! {congratulations_symbol}")


def main():
    questions = [
        {
            'text': 'What is the capital of France?',
            'options': ['Paris', 'Berlin', 'Madrid'],
            'correct': 'Paris'
        },
        {
            'text': 'Which programming language is this quiz written in?',
            'options': ['Java', 'Python', 'C++'],
            'correct': 'Python'
        },
        {
            'text': 'What is the largest mammal?',
            'options': ['Elephant', 'Blue Whale', 'Giraffe'],
            'correct': 'Blue Whale'
        },
        {
            'text': 'Who developed Python Programming Language?',
            'options': ['Wick van Rossum', 'Rasmus Lerdorf', 'Guido van Rossum' , 'Niene Stom'],
            'correct': 'Guido van Rossum'
        },
        {
            'text': 'Is Python case sensitive when dealing with identifiers?',
            'options': ['no','yes','machine dependent','none of the above'],
            'correct': 'yes'
        }
    ]

    random.shuffle(questions) 
    quiz = QuizGame(questions)
    quiz.run_quiz()

if __name__ == "__main__":
    main()
