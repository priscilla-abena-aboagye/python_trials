
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



import random
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True


print("Python guessing game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That is number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again")
        elif guess > answer:
            print("Too high! Try again")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")




options = ("rock", "paper", "scissors")

running = True

while running:

    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player : {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
        running = False

print("Thanks for playing")


