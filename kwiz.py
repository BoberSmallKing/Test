questions = ("Как назывался особый головной убор, который носили фараоны в Древнем Египте?",
             "У какого животного самые большие глаза относительно тела?",
             "Как называли строителя в старину?",)
options = (("A. Картуз", "B. Немес", "C. Корона"),
           ("A. У лемкра", "B. У долгопята", "С. У тупайи"),
           ("A. Бондарь", "B. Бондарь", "C. Зодчий"))
answers = ("B", "B", "C")
gusses = []
number_question = 0
score = 0

for question in questions:
    print("------------------------------")
    print(question)
    for option in options[number_question]:
        print(option)

    guss = input("Enter (A, B, C): ").upper()
    gusses.append(guss)
    if guss == answers[number_question]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"Correct answer {answers[number_question]}")
    number_question += 1

print("-------------------------\nRESULT\n-------------------------")
score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")