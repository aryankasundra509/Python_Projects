import random

easy_words = [
    "apple", "chair", "house", "water", "pencil", "table", "dog", "cat",
    "sun", "moon", "book", "car", "phone", "shirt", "ball", "tree",
    "milk", "juice", "bed", "hat", "shoe", "bread", "clock", "fish",
    "cake", "lamp", "spoon", "glass", "duck", "kite", "door", "bag",
    "pen", "ice", "key", "fan", "sock", "leaf", "bus", "rain"
]

medium_words = [
    "window", "bottle", "pillow", "garden", "banana", "basket", "rabbit", "guitar",
    "school", "mirror", "tunnel", "beach", "mountain", "pocket", "ticket", "candle",
    "button", "scooter", "trophy", "blanket", "elephant", "airplane", "crayon", "forest",
    "ladder", "camera", "planet", "engine", "helmet", "remote", "rocket", "castle",
    "zebra", "circle", "pirate", "sister", "uncle", "jungle", "monkey", "train"
]

hard_words = [
    "triangle", "oxygen", "reptile", "avalanche", "microscope", "telescope", "dinosaur", "volcano",
    "galaxy", "whistle", "chimney", "crocodile", "alphabet", "parachute", "knapsack", "laboratory",
    "continent", "accordion", "adventure", "calendar", "fireplace", "hieroglyph", "lighthouse", "mechanic",
    "necktie", "octopus", "penguin", "quicksand", "reindeer", "scissors", "tornado", "ukulele",
    "vacuum", "wrestler", "xylophone", "yacht", "zeppelin", "blueprint", "compass", "geyser"
]

print("Welcome to the word guessing game.")
print("Choose a difficulty level: Easy, Medium, Hard")

level = input("Enter Difficuly level: ").lower()

if level == "easy":
    word = random.choice(easy_words)
elif level == "medium":
    word = random.choice(medium_words)
elif level == "hard":
    word = random.choice(hard_words)
else :
    print("Invalid choice. By default Easy difficulty.")
    word = random.choice(easy_words)

attempts = 0
print(" ")

while True:
    guess = input("Guess the word: ")
    attempts += 1

    if guess == word:
        print(f"Congratulations you guess the word in {attempts} attempts.")
        break

    hint = ""

    for i in range(len(word)):
        if i < len(guess) and guess[i] == word[i]:
            hint += word[i]
        else:
            hint += "_"
    
    print("Hint: ", hint)

print("Game Over")
print("Thank You for playing. I hope you enjoyed.")