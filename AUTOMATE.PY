import os
import random
import string
import subprocess

def random_string(length=8):
    """Generate a random string of the specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_random_file(directory="."):
    """Create a file with a random name and write random text into it."""
    file_name = f"{random_string()}.txt"
    file_path = os.path.join(directory, file_name)
    random_text = random_string(50)  # Random text of 50 characters
    
    with open(file_path, "w") as f:
        f.write(random_text)
    
    print(f"Created file: {file_path}")
    return file_path

def run_git_commands():
    """Run the git commands to add, commit, and push changes."""
    try:
        # Add all changes
        subprocess.run(["git", "add", "."], check=True)
        print("Added all changes to git.")
        
        # Create a random commit message
        commit_message = random_string(20)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print(f"Committed with message: {commit_message}")
        
        # Push changes
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("Pushed changes to origin/main.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def main():
    # Ensure the script runs in a Git repository
    if not os.path.exists(".git"):
        print("This script must be run inside a Git repository.")
        return
    
    # Create a random file and add it to Git
    create_random_file()
    run_git_commands()

if __name__ == "__main__":
    main()
