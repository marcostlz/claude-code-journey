name = input("What's your name? ")
level = input("Are you a beginner or expert? ")

if level.lower() == "beginner":
    print("Welcome " + name + "! Let's start from zero.")
else:
    print("Welcome " + name + "! Let's build something serious.")
