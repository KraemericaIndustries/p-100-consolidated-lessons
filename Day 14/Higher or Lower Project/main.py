import art
import random
import game_data

def get_index(champ_index):
    index = random.randint(0, len(game_data.data) - 1)
    # In the event the index chosen at random is the same as that of the champion, choose another random number as the index...
    while index == champ_index:
        index = random.randint(0, len(game_data.data) - 1)
    return index

choice = "z"

last_answer_correct = True
score = 0

champion_index = get_index(999) # Get a random number, to index the data list with
challenger_index = get_index(champion_index) # Get a random number, to index the data list with

champion_dictionary = game_data.data[champion_index] # Select a dictionary from the dictionaries list to serve as champion
challenger_dictionary = game_data.data[challenger_index] # Select a dictionary from the dictionaries list to serve as champion

# Champion details...
print(art.logo)
if score != 0:
    print(f"You're right! Current score: {score}.")
print(f"Compare A: {champion_dictionary.get("name")}, a {champion_dictionary.get("description")}, from {champion_dictionary.get("country")}.")

# Challenger details...
print(art.vs)
print(f"Against B: {challenger_dictionary.get("name")}, a {challenger_dictionary.get("description")}, from {challenger_dictionary.get("country")}.")

while last_answer_correct:
    choice = input("Who has more followers? Type 'a' or 'b': ")

    if choice == "a":
        if champion_dictionary.get("follower_count") > challenger_dictionary.get("follower_count"):
            print("\n" * 100)
            score += 1
            print(art.logo)
            champion_index = challenger_index  # challenger becomes champion
            if score != 0:
                print(f"You're right! Current score: {score}.")
            champion_dictionary = game_data.data[champion_index]
            print(f"Compare A: {champion_dictionary.get("name")}, a {champion_dictionary.get("description")}, from {champion_dictionary.get("country")}.")
            challenger_index = get_index(champion_index)  # get a new challenger
            challenger_dictionary = game_data.data[challenger_index]  # Select a dictionary from the dictionaries list to serve as champion
            print(art.vs)
            print(f"Compare B: {challenger_dictionary.get("name")}, a {challenger_dictionary.get("description")}, from {challenger_dictionary.get("country")}.")
        else: last_answer_correct = False
    elif choice == "b":
        if challenger_dictionary.get("follower_count") > champion_dictionary.get("follower_count"):
            print("\n" * 100)
            score += 1
            print(art.logo)
            champion_index = challenger_index  # challenger becomes champion
            if score != 0:
                print(f"You're right! Current score: {score}.")
            champion_dictionary = game_data.data[champion_index]
            print(f"Compare A: {champion_dictionary.get("name")}, a {champion_dictionary.get("description")}, from {champion_dictionary.get("country")}.")
            challenger_index = get_index(champion_index)  # get a new challenger
            challenger_dictionary = game_data.data[challenger_index]  # Select a dictionary from the dictionaries list to serve as champion
            print(art.vs)
            print(f"Compare B: {challenger_dictionary.get("name")}, a {challenger_dictionary.get("description")}, from {challenger_dictionary.get("country")}.")
        else: last_answer_correct = False

print("\n" * 100)
print(art.logo)
print(f"Sorry, that's wrong.  Final score: {score}.")