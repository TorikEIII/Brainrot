import random
import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the smallest common multiple of given numbers.")

    rounds = 3
    for _ in range(rounds):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print(f"Question: {a} {b}")
        answer = input("Your answer: ")

        correct_answer = lcm(a, b)
        if answer.isdigit() and int(answer) == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}")
            return

    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()
