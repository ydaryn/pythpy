import db_utils

def start_game():
    username = input("Enter your username: ")
    user_id = db_utils.get_user_id(username)
    current_level = db_utils.get_current_level(user_id)
    print("Your current level is:", current_level)
    # Start the game

def pause_and_save(user_id, score, level):
    db_utils.pause_and_save_state(user_id, score, level)
    print("Game paused and current state saved.")

if __name__ == "__main__":
    start_game()
    # Game logic
    # Implement pause and save functionality
