
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





menu = {"popcorn": 4.00,
        "chips": 3.00,
        "fries": 6.00,
        "burger": 12.00,
        "soda": 10.00,
        "lemonade": 4.25}

cart = []
total = 0
print("------------MENU------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------")

while True:
    food = input("Select an item to buy (press q to quit) :").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"The total is {total:.2f}")




