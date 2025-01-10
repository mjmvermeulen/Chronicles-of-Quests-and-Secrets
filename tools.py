import assets.art.classes.art as class_art
import stats.classes as class_stats
import data
import utils

player_name: str = ""
player_gender: str = ""
player_race: str = ""
player_class: str = ""

def character_creator():
    """
    Helps the player create their character for their adventure,
    this script should only run at the start of the game
    """
    global player_name
    global player_gender
    global player_race
    global player_class
    # Player Creation
    print("Lets start by creating your hero")
    player_name = input("What is your name?\n").lower().capitalize()

    player_gender = input("Are you a male/female?\n").lower().capitalize()
    gender_chosen = False
    while not gender_chosen:
        if player_gender == "Male":
            gender_chosen = True
        elif player_gender == "Female":
            gender_chosen = True
        else:
            print(f"Apologies Hero it appears this world only knows: Male and Female and therefore we cannot let you be a {player_gender}")
            player_gender = input("Are you a male/female?\n").lower().capitalize()

    print(f"Example races: {data.races}\n")
    print("You are free to create your own race.\n")
    player_race = input(f"Which race do you belong to? \n").lower().capitalize()

    # Class selection
    utils.clear_terminal()
    print(class_art.classes)
    print(f"Warrior stats: {class_stats.warrior}")
    print(f"Archer stats: {class_stats.archer}")
    print(f"Magician stats: {class_stats.magician}\n")

    stats_info_request = input("Would you like more information about what each stat does? write 'y' or 'n'\n").lower()

    while stats_info_request != "n":
        if stats_info_request == "y":
            utils.player_stat_details()
        else:
            print(f"{stats_info_request} is not a valid option please try again.")
            stats_info_request = input("Would you like more information about what each stat does? write 'y' or 'n'\n").lower()

    player_class = input("\nWhich class would you like to play?\n").lower().capitalize()

    class_chosen = False
    while not class_chosen:
        if player_class == "Magician":
            class_chosen = True
        elif player_class == "Warrior":
            class_chosen = True
        elif player_class == "Archer":
            class_chosen = True
        else:
            print(f"{player_class} is not a existing class in this world please choose between: Warrior, Archer or Magician")
            player_class = input("Which class would you like to play?\n").lower().capitalize()