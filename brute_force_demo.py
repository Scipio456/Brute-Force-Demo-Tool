import string
import time

# Character set for brute force (lowercase letters and digits)
CHARSET = string.ascii_lowercase + string.digits  # a-z, 0-9
MAX_LENGTH = 10  # Maximum password length to attempt
DELAY = 0.01  # Delay in seconds between attempts to simulate real-world conditions

def brute_force(target_password):
    print("Starting brute force attack demonstration (character-by-character)...")
    print(f"Using character set: {CHARSET}")
    print(f"Maximum password length: {MAX_LENGTH}")
    
    attempts = 0
    start_time = time.time()
    current_guess = [''] * len(target_password)  # Initialize guess with empty characters
    
    # Iterate through each position of the password
    for pos in range(len(target_password)):
        found = False
        # Try each character in the charset for the current position
        for char in CHARSET:
            attempts += 1
            current_guess[pos] = char  # Update the current position
            guess = ''.join(current_guess)  # Form the current guess string
            
            # Simulate a password check
            time.sleep(DELAY)  # Add delay to mimic real-world conditions
            print(f"Attempt #{attempts}: {guess}")
            
            # Check if the character at this position is correct
            if char == target_password[pos]:
                found = True
                print(f"Correct character found for position {pos + 1}: {char}")
                break  # Move to the next position
            
        if not found:
            print(f"\nFailed to find correct character for position {pos + 1}.")
            return False
        
        # If we've filled all positions correctly, check the full password
        if pos == len(target_password) - 1:
            end_time = time.time()
            print(f"\nSuccess! Password found: {guess}")
            print(f"Attempts: {attempts}")
            print(f"Time taken: {end_time - start_time:.2f} seconds")
            return True
    
    print("\nFailed to find password within constraints.")
    return False

if __name__ == "__main__":
    try:
        # Prompt user to enter the target password
        target_password = input("Enter the password to brute force (max 7 characters, lowercase letters and digits only): ").strip()
        if not target_password:
            print("Error: No password entered.")
        elif len(target_password) > MAX_LENGTH:
            print(f"Error: Password length exceeds maximum of {MAX_LENGTH} characters.")
        elif not all(c in CHARSET for c in target_password):
            print("Error: Password contains characters not in the allowed set (a-z, 0-9).")
        else:
            brute_force(target_password)
    except KeyboardInterrupt:
        print("\nBrute force attack stopped by user.")