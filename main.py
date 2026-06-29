import os

if __name__ == "__main__":
    print("Welcome to RoboSpeaker created by Manav")

    while True:
        x = input("What do you want me to speak? ")

        if x == "q":
            os.system("say 'bye bye'")
            break

        command = f"say {x}"