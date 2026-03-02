import random

def colored(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def mind_game():
    low = 1
    high = 100
    secret = random.randint(low, high)

    attempts = 7
    score = 150
    guesses = []
    random_guess_counter = 0

    print(colored("🧠 MIND GAME MODE ACTIVATED", "36"))

    while attempts > 0:
        print(colored(f"\nCurrent Range: {low} to {high}", "34"))

        try:
            guess = int(input("Enter guess: "))
        except ValueError:
            print(colored("⚠ Invalid number!", "31"))
            continue

        if guess < low or guess > high:
            print(colored("🚫 Guess inside current range!", "31"))
            continue

        guesses.append(guess)
        attempts -= 1
        score -= 15

        if guess == secret:
            bonus = attempts * 10
            score += bonus
            print(colored("\n🎉 Mind Master! You cracked it!", "32"))
            print(f"Guesses: {guesses}")
            print(f"Bonus: {bonus}")
            print(f"Final Score: {score}")
            return

        # Detect random guessing
        if len(guesses) > 1:
            if abs(guesses[-1] - guesses[-2]) > 40:
                random_guess_counter += 1

        # Shrink range
        if guess < secret:
            low = guess + 1
            print("Too Low!")
        else:
            high = guess - 1
            print("Too High!")

        if random_guess_counter >= 2:
            print(colored("⚠ You are guessing randomly!", "33"))
            score -= 10

        print(colored(f"Attempts Left: {attempts}", "35"))

    print(colored(f"\n💀 You Lost! The number was {secret}", "31"))

def main():
    print(colored("🎮 ULTIMATE NUMBER GUESSING GAME 🎮", "36"))
    mind_game()

if __name__ == "__main__":
    main()