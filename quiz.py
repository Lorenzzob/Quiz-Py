print("Welcome to the Quiz")

answer_user = input("Let's start? (Y/N)")


if answer_user != "Y":
    quit()

score = 0   

print("Let's Go!...")
print("--------------------------------------------------------------")
print("Who developer the game Roller Coaster Tycoon? \n (A) Will Wright \n (B) Roberta Williams \n (C) Chris Sawyer \n")
answer_1 = input("Answer: ")

if answer_1 == "C":
    print("Correct!")
    score += 1
else: 
    print("Incorrect")


print("---------------------------------------------------------------")


print("What's the objective of the game Roller Coaster Tycoon? \n (A) Build Cities \n (B) Build Amusement Parks  \n (C) Build Houses \n")
answer_1 = input("Answer: ")

if answer_1 == "B":
    print("Correct!")
    score += 1
else: 
    print("Incorrect")


print("---------------------------------------------------------------")


print("What's the name of the new TV serie based in a game? \n (A) The Last of Us \n (B) Far Cry \n (C) GTA \n")
answer_1 = input("Answer: ")

if answer_1 == "A":
    print("Correct!")
    score += 1
else: 
    print("Incorrect")


print(f"End of Quiz. Total Score: {score}/3")




