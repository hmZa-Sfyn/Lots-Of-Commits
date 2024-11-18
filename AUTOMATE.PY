import os
import random
import string
import subprocess
import time

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
    
    return file_path

def run_git_commands(commit_message):
    """Run the git commands to add, commit, and push changes."""
    try:
        # Add all changes
        subprocess.run(["git", "add", "."], check=True, stdout=subprocess.DEVNULL)
        
        # Commit changes
        subprocess.run(["git", "commit", "-m", commit_message], check=True, stdout=subprocess.DEVNULL)
        
        # Push changes
        subprocess.run(["git", "push", "origin", "main"], check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def main():
    # Ensure the script runs in a Git repository
    if not os.path.exists(".git"):
        print("This script must be run inside a Git repository.")
        return
    
    try:
        # Execute 100 times per second
        for _ in range(100):
            start_time = time.time()
            
            # Create a random file
            create_random_file()
            
            # Generate a random commit message
            commit_message = random_string(20)
            
            # Run Git commands
            run_git_commands(commit_message)
            
            # Ensure we respect the 1-second timeframe
            elapsed_time = time.time() - start_time
            if elapsed_time < 0.01:  # 1/100th of a second
                time.sleep(0.01 - elapsed_time)
    except KeyboardInterrupt:
        print("Execution interrupted by user.")

if __name__ == "__main__":
    main()
