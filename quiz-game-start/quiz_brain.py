class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        correct = True
        while correct:
            next_q = self.question_list[self.question_number]
            self.question_number += 1
            choice = input(f"Q.{self.question_number}: {next_q.text}. (True/False)?: ").lower()
            if choice == "true" and next_q.answer == "True":
                print(f"Correct: ({self.question_number}/12).")
                if self.question_number == 12:
                    correct = False
                    print("Congratulations, you've got them all right!")
            elif choice == "false" and next_q.answer == "False":
                print(f"Correct: ({self.question_number}/12).")
                if self.question_number == 12:
                    correct = False
                    print("Congratulations, you've got them all right!")
            else:
                print(f"Incorrect. Your score is ({self.question_number}/12).")
                correct = False
        if not correct:
            play_again = input("Do you want to play again? 'y' or 'n'?: ").lower()
            if play_again == "y":
                self.question_number = 0
                self.next_question()
