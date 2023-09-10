def quiz():
    questions = (
        "1. What is the pH value of the human body?",
        "2. Which of the following are called Key Industrial animals?",
        "3. Which of the given amendments made it compulsory for the president to consent to the constitutional Amendment bills?",
        "4. Elections to panchayats in state are regulated by",
        "5. Which of the following Himalayan regions is called Shivalik's?",
    )

    options = [
        [
            "a) 9.2 to 9.8",
            "b) 7.0 to 7.8",
            "c) 6.1 to 6.3",
            "d) 5.4 to 5.6",
        ],
        [
            "a) Producers",
            "b) Tertiary consumers",
            "c) Primary consumers",
            "d) None of these",
        ],
        [
            "a) 27th",
            "b) 29th",
            "c) 24th",
            "d) 22nd",
        ],
        [
            "a) Gram panchayat",
            "b) Nagar Nigam",
            "c) Election Commission of India",
            "d) State Election Commission",
        ],
        [
            "a) Upper Himalayas",
            "b) Lower Himalayas",
            "c) Outer Himalayas",
            "d) Inner Himalayas",
        ],
    ]

    answers = ('B', 'C', 'C', 'D', 'C')

    guesses = []

    question_num = 0

    score = 0

    print("""                 Welcome to Quiz Game        """)
    print("\n")
    print("Rules")
    print(""" Eligibility:

        The quiz Game is open to eligible participants (individuals or teams) who have registered in advance.

    Format:

        The quiz format consists of multiple-choice questions (MCQs).
        Each participant/team must select one option as their answer to each question.

    No External Resources:

        Participants are strictly prohibited from using the internet, books, notes, or any external resources during the quiz.
        Any attempt to access external resources will result in immediate disqualification.

    Question Types:

        All questions will be presented in MCQ format.
        Participants should choose the correct option for each question.

    Scoring:

        Participants will earn one point for each correct answer.
        There is no negative marking for incorrect answers. """)



    print("\n")

    choice = input("Do you want to attempt this Quiz? (yes/no): ").lower()

    if choice == "yes":
        while question_num < len(questions):
            print("\n")
            print("Next Question")
            print(questions[question_num])

            for option in options[question_num]:
                print(option)

            guess = input("Please choose one answer: ").upper()
            guesses.append(guess)
            if guess == answers[question_num]:
                score += 1
                print("Correct")
            else:
                print("Incorrect")
                print(f"The Correct Answer is:  {answers[question_num]} ")

            question_num += 1

        print("\n")

        print("""                       Results                 """)

        print("answers", end=' ')
        for answer in answers:
            print(answer, end=' ')
        print("\n")

        print("guesses", end=' ')
        for guess in guesses:
            print(guess, end=' ')
        print("\n")

        score_percentage = (score / len(questions)) * 100
        print(f"Your score is : {score_percentage}%")
    else:
        print("Okay, you choose not to attempt the quiz. Goodbye!")
       

quiz()

while True:
    choice = input("You want to Attempt quiz again yes/no: ")
    if choice!= 'yes' or 'Yes':
        break
    quiz()
