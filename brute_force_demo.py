import string
import time
import argparse

# WARNING: This script is for EDUCATIONAL PURPOSES ONLY.
# Unauthorized use or modification for malicious purposes is strictly prohibited and illegal.
# Use only on systems you own or have explicit permission to test.

CHARSET = string.ascii_lowercase + string.digits  # a-z, 0-9
MAX_LENGTH = 7  # Maximum password length
DELAY = 0.01  # Delay between attempts (seconds)

def validate_password(password: str) -> bool:
    """Validate the input password against demo constraints."""
    if not password:
        print("Error: No password provided.")
        return False
    if len(password) > MAX_LENGTH:
        print(f"Error: Password length exceeds maximum of {MAX_LENGTH} characters.")
        return False
    if not all(c in CHARSET for c in password):
        print("Error: Password contains characters not in allowed set (a-z, 0-9).")
        return False
    return True

def brute_force(target_password: str) -> bool:
    """
    Perform a character-by-character brute force attack for demonstration.
    
    Args:
        target_password (str): The password to brute force.
    
    Returns:
        bool: True if password is found, False otherwise.
    """
    print("Starting brute force attack demonstration (character-by-character)...")
    print(f"Character set: {CHARSET}")
    print(f"Maximum password length: {MAX_LENGTH}")
    print("NOTE: This is an educational demonstration. Do not use on unauthorized systems.")
    
    attempts = 0
    start_time = time.time()
    current_guess = [''] * len(target_password)
    
    for pos in range(len(target_password)):
        found = False
        for char in CHARSET:
            attempts += 1
            current_guess[pos] = char
            guess = ''.join(current_guess)
            
            time.sleep(DELAY)
            print(f"Attempt #{attempts}: {guess}")
            
            if char == target_password[pos]:
                found = True
                print(f"Correct character found for position {pos + 1}: {char}")
                break
        
        if not found:
            print(f"\nFailed to find correct character for position {pos + 1}.")
            return False
        
        if pos == len(target_password) - 1:
            end_time = time.time()
            print(f"\nSuccess! Password found: {guess}")
            print(f"Total attempts: {attempts}")
            print(f"Time taken: {end_time - start_time:.2f} seconds")
            return True
    
    return False

def main():
    """Main function to handle command-line arguments and run the brute force demo."""
    parser = argparse.ArgumentParser(
        description="Educational brute force password attack demo. For learning purposes only."
    )
    parser.add_argument(
        "--password",
        type=str,
        help="Password to brute force (max 7 chars, a-z, 0-9)",
        default="pass123"
    )
    args = parser.parse_args()
    
    try:
        print("WARNING: This tool is for EDUCATIONAL USE ONLY. Unauthorized use is illegal.")
        if validate_password(args.password):
            brute_force(args.password)
    except KeyboardInterrupt:
        print("\nBrute force attack stopped by user.")

if __name__ == "__main__":
    main()