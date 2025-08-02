# STEP 1: IMPORT RANDOM FOR RANDOM CHOICES
import random

# STEP 2: CREATED A DIFFERENT LISTS WITH UNIQUE WORDS 
subjects = [
    "Tom Cruize", "M.S. Dhoni", "Nirmala Sitaraman", "A mumbai Dog", "Auto Rikshawman",
    "Salman Khan", "Virat Kohli", "A Delhi Street Cat", "Tea Stall Owner", "Modiji",
    "Traffic Police", "A Rickshaw Puller", "Karan Johar", "A School Kid", "College Professor",
    "The Mumbai Local", "Street Magician", "Pani Puri Wala", "Ratan Tata", "Tiffin Delivery Boy",
    "A Stray Cow", "Metro Announcer", "News Reporter", "Local MLA", "Amitabh Bachchan",
    "Temple Priest", "Railway Coolie", "Cricket Fanatic Uncle", "Yoga Teacher", "Film Director",
    "Ice Cream Vendor", "A Lost Foreigner", "Zomato Delivery Guy", "Bollywood Choreographer", "Dabbawala"
]

actions = [
    "danced in the rain", "argued with a parrot", "gave a motivational speech", "missed the last train",
    "sang a love song", "ordered 10 plates of pani puri", "got chased by a cow", "won a staring contest",
    "delivered a TED Talk", "tried to bribe a robot", "took a selfie with an alien", "invented a new snack",
    "fainted after watching horror movie", "drove an auto on Mars", "mistook soap for ice cream",
    "recited a poem to a buffalo", "hosted a cooking show", "did yoga on a moving train", "broke a world record",
    "became invisible", "got stuck in a revolving door", "saved a cat from a tree", "went viral on Instagram",
    "confused Mumbai for Dubai", "forgot their own name", "won a dance battle", "proposed on live TV",
    "started a street band", "ran a marathon backwards", "played cricket with coconuts"
]

places_or_things = [
    "on a flying bus", "at India Gate", "under the sea", "in a haunted mansion", "on a rooftop café",
    "inside a washing machine", "at a wedding in Jaipur", "in the middle of a cricket stadium",
    "on top of a water tank", "at the Mumbai airport", "in a crowded metro", "inside a giant dosa",
    "on a banana boat", "in a traffic jam", "under a banyan tree", "on a film set", "at a political rally",
    "inside a food truck", "on a rainy footpath", "in a fancy mall", "at a college fest",
    "on a broken bicycle", "inside a chai kettle", "on a moving train", "on a temple gopuram",
    "inside a makeup van", "in a dhaba kitchen", "at Marine Drive", "in a VR video game",
    "on top of a coconut tree"
]
# STEP 3: CREAT A LIST TO STORE HEADLINES
generated_headlines = []

# STEP 4: START THE HEADLINE GENERATOR LOOP
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)
    generated_headlines.append(headline)

    user_input = input("Do you want to Generate another headline ? (Yes / No): ").strip().lower()
    if user_input == "no":
        break

# ASK IF USER WANT TO SAVE THE SESSION
save_input = input("Would you like to save your headline to a fil ? (Yes / No)").strip().lower()
if save_input == "yes":
    with open("headlines.txt", 'w') as f:
        for h in generated_headlines:
            f.write(h + "\n")
    print("Headline save to 'headline.txt' .")

# PRINT A GOODBYE MESSAGE
print("\nThanks for using the Fake Headline Generator. Have a great day.")
