import os

def clear_terminal():
    """
    Clears the terminal from the previous scene to ensure that we keep a clean view and scenes do not overlap
    """
    print('\n'*80) # terminal clear for development

    # os.system('cls' if os.name=='nt' else 'clear')

def player_stat_details():
    """
    Provides the player with information about the different stats
    """
    print("\033[1mCharacter stat overview:\033[0m\n"
          "health: Determines how much damage you can take before you are defeated\n"
          "attack: Determines how much damage you deal\n"
          "defence: Determines how much damage you take, the higher the number the less damage you take\n"
          "evasion: Gives you a chance to dodge attacks (this means you take no damage), its a percentage chance\n"
          "critrate: Gives you a chance to hit for critical dmg (1,5x dmg), its a percentage chance\n")

    input("Take your time to read all the information, once you are ready press any key to continue ......")
