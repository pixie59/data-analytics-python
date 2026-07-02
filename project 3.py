def run_quiz():
    score = 0
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A)London", "B)Berlin", "C)Paris", "D)Madrid"],
            "answer": "C)Paris"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["A)3", "B)4", "C)5", "D)6"],
            "answer": "B)4"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A)Atlantic Ocean", "B)Indian Ocean", "C)Arctic Ocean", "D)Pacific Ocean"],
            "answer": "D)Pacific Ocean"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A)William Shakespeare", "B)Charles Dickens", "C)Mark Twain", "D)Jane Austen"],
            "answer": "A)William Shakespeare"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A)O2", "B)H2O", "C)CO2", "D)NaCl"],
            "answer": "B)H2O"
        }
    ]
    for index, q in enumerate(questions):
        print(f"\nQuestion {index + 1}: {q['question']}")
        for opt in q['options']:
            print(opt)
        answer = input("Your answer (A/B/C/D): ").strip()
        if answer.upper() == q['answer'][0]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. Correct answer: {q['answer']}")
    print(f"\nQuiz finished. Your score: {score}/{len(questions)}")


run_quiz()