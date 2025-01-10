import tools
import stats.classes as class_stats

# Contains all up-to-date player_data
player_data = {
    "player_name": "",
    "player_gender": "",
    "player_race": "",
    "player_class": "",
    "player_health": 0,
    "player_attack": 0,
    "player_defence": 0,
    "player_evasion": 0,
    "player_critrate": 0,
}

# Legacy storage of player_data
# # Holds the player character non combat data
# player_name: str = ""
# player_gender: str = ""
# player_race: str = ""
# player_class: str = ""
# # Holds the player combat stats
# player_health: int = 0
# player_attack: int = 0
# player_defence: int = 0
# player_evasion: int = 0
# player_critrate: int = 0

def collect_fresh_created_player_data():
    # Ensures that all player data is stored for future use in player_data.py
    global player_data

    # Players non combat information is collected and stored
    player_data["player_name"] = tools.player_name
    player_data["player_gender"] = tools.player_gender
    player_data["player_race"] = tools.player_race
    player_data["player_class"] = tools.player_class

    # Players starting combat stats are collected and stored based on the class they choose
    if player_data["player_class"] == "Magician":
        player_data["player_health"] = class_stats.magician["health"]
        player_data["player_attack"] = class_stats.magician["attack"]
        player_data["player_defence"] = class_stats.magician["defence"]
        player_data["player_evasion"] = class_stats.magician["evasion"]
        player_data["player_critrate"] = class_stats.magician["critrate"]
    elif player_data["player_class"] == "Warrior":
        player_data["player_health"] = class_stats.warrior["health"]
        player_data["player_attack"] = class_stats.warrior["attack"]
        player_data["player_defence"] = class_stats.warrior["defence"]
        player_data["player_evasion"] = class_stats.warrior["evasion"]
        player_data["player_critrate"] = class_stats.warrior["critrate"]
    else:
        player_data["player_health"] = class_stats.archer["health"]
        player_data["player_attack"] = class_stats.archer["attack"]
        player_data["player_defence"] = class_stats.archer["defence"]
        player_data["player_evasion"] = class_stats.archer["evasion"]
        player_data["player_critrate"] = class_stats.archer["critrate"]
