import assets.art.core.art as core_art
import player.player_data as player
import utils
import tools


# Main Opening Scene
print(core_art.primary_logo)
print("\033[1mWelcome adventurer to the Chronicles of Quests & Secrets\033[0m")
input("Press any key to start your adventure....\n")
utils.clear_terminal()

# Runs the character creation script
tools.character_creator()
# Collects all the player data from the creation fase into the player_data.py file
player.collect_fresh_created_player_data()

print(player.player_data)

