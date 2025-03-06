import random
import string

def generate_username(adjectives, nouns, add_numbers=True, add_special_chars=True, length=8):
    """Generates a random username based on user preferences."""
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun
    
    if add_numbers:
        username += str(random.randint(10, 99))  # Add a random two-digit number
    
    if add_special_chars:
        username += random.choice(string.punctuation)  # Add a random special character
    
    return username[:length]  # Ensure it adheres to the specified length

def save_to_file(username, filename="usernames.txt"):
    """Saves the generated username to a file."""
    with open(filename, "a") as file:
        file.write(username + "\n")

def main():
    adjectives = ["Cool", "Happy", "Fast", "Brave", "Smart", "Clever", "Energetic", "Mighty"]
    nouns = ["Tiger", "Dragon", "Eagle", "Lion", "Panther", "Wolf", "Shark", "Falcon"]
    
    print("Welcome to the Random Username Generator!")
    
    # Get user preferences
    add_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    add_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
    length = input("Enter desired username length (default 8): ").strip()
    length = int(length) if length.isdigit() and int(length) > 0 else 8
    
    # Generate and display the username
    username = generate_username(adjectives, nouns, add_numbers, add_special_chars, length)
    print("Your generated username: ", username)
    
    # Save to file
    save_to_file(username)
    print("Username saved to usernames.txt")
    
if __name__ == "__main__":
    main()
