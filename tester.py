
questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 204", "B. 765", "C. 118", "D. 2222"),
           ("A. Egg", "B. Crocodile", "C. Turkey", "D. Ostrich"),
           ("A. Oxygen", "B. Carbon-dioxide", "C. Nitrogen", "D. Helium"),
           ("A. 206", "B. 207", "C. 119", "D. 116"),
           ("A. Earth", "B. Saturn", "C. Venus", "D. Mercury"))

answers = ("D", "D", "C", "A", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D: )").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("---------------------")
print("      RESULT        ")
print("----------------------")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guess: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is : {score}%")



capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "Ghana": "Acrra",
            "Korea": ""}
if capitals.get("USA"):
    print("The capital exit")
else:
    print("The capital does not exit")

capitals.update({"Japan": "Tokyo",
                 "Germany": "Berlin"})
capitals.pop("Ghana")
capitals.popitem()

print(capitals)


