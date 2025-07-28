# Program: KBC Style Quiz
# 1. Displays multiple-choice questions like KBC.
# 2. Uses lists to store questions, options, and answers.
# 3. Displays the final amount the player wins.

questions = [
    "1. What is the capital of India?",
    "2. Which language is used to write Python programs?",
    "3. Who is known as the father of the computer?",
    "4. What is 5 + 7?"
]

options = [
    ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
    ["A. C++", "B. Java", "C. Python", "D. English"],
    ["A. Charles Babbage", "B. Alan Turing", "C. Bill Gates", "D. Steve Jobs"],
    ["A. 10", "B. 11", "C. 12", "D. 13"]
]

answers = ["B", "C", "A", "C"]  # Correct options
prize = [1000, 2000, 3000, 5000]  # Prize for each question

winnings = 0

# Loop through questions
for i in range(len(questions)):
    print("\n" + questions[i])
    for opt in options[i]:
        print(opt)
    user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

    if user_answer == answers[i]:
        winnings += prize[i]
        print(f"Correct! You won ₹{prize[i]}")
    else:
        print("Wrong answer! Game over.")
        break

print(f"\nYou are taking home ₹{winnings}")
