# Brute Force Password Attack Demonstration

## Overview

This project is an **educational tool** designed exclusively for demonstrating the concept of a brute force password attack in a controlled, ethical environment. It implements a character-by-character brute force approach to guess a user-provided password, illustrating the mechanics of such attacks and the importance of strong password policies.

**WARNING**: This tool is for **EDUCATIONAL PURPOSES ONLY**. Modification, redistribution, or use for any non-educational purpose is strictly prohibited. Unauthorized use on systems you do not own or lack explicit permission to test is **illegal** and **unethical**. The project is licensed under the Educational Use Only License, which forbids modification and restricts use to personal, non-commercial learning.

## Features

- **Character-by-Character Brute Force**: Efficiently guesses passwords by checking each character position sequentially.
- **Input Validation**: Ensures the password meets demo constraints (max 7 characters, lowercase letters, and digits).
- **Command-Line Interface**: Accepts password input via argument or default value (`pass123`).
- **Simulated Delay**: Mimics real-world conditions with a 0.01-second delay between attempts.
- **Comprehensive Logging**: Displays each guess, attempt count, and execution time.

## Requirements

- Python 3.6+
- No external dependencies required.

## Installation

Ensure Python is installed:

   ```bash
   python --version
   ```

## Usage

Run the script with a password (max 7 characters, lowercase letters, and digits):

```bash
python brute_force.py --password pass123
```

Or use the default password (`pass123`):

```bash
python brute_force.py
```

- The script will attempt to guess the password character by character.
- Press `Ctrl+C` to stop the process.
- Output includes each guess, correct character confirmations, total attempts, and time taken.

## Example Output

```
WARNING: This tool is for EDUCATIONAL USE ONLY. Unauthorized use is illegal.
Starting brute force attack demonstration (character-by-character)...
Character set: abcdefghijklmnopqrstuvwxyz0123456789
Maximum password length: 7
NOTE: This is an educational demonstration. Do not use on unauthorized systems.
Attempt #1: a
Attempt #2: b
...
Attempt #15: p
Correct character found for position 1: p
Attempt #16: pa
...
Success! Password found: pass123
Total attempts: 85
Time taken: 0.85 seconds
```

## Educational Value

- **Brute Force Mechanics**: Demonstrates how brute force attacks systematically guess passwords.
- **Efficiency Optimization**: Uses a character-by-character approach to reduce unnecessary guesses compared to full combination generation.
- **Security Insights**: Highlights the importance of long, complex passwords to resist brute force attacks.
- **Ethical Hacking**: Emphasizes the need for authorization and ethical considerations in security testing.

## Limitations

- Limited to lowercase letters and digits (a-z, 0-9) for simplicity.
- Maximum password length is 7 characters to keep demo runtime manageable.
- Simulates a simplified attack; real systems include defenses like rate-limiting or account lockouts.
- Assumes individual character verification, which is not realistic for most systems.

## Ethical and Legal Considerations

This tool is strictly for **educational purposes**. It must only be used on systems you own or have explicit, written permission to test. Unauthorized use, modification, or redistribution is prohibited and may be illegal. For safe practice, use platforms like TryHackMe or Hack The Box. The Educational Use Only License ensures the code remains unchanged and restricted to personal learning.

Contributing

Contributions are not accepted, as modification of this software is prohibited under the Educational Use Only License to prevent misuse.

## License

This project is licensed under the Educational Use Only License. See the LICENSE file for details. Modification and redistribution are prohibited; use is restricted to personal, non-commercial educational purposes only.

## Author

Scipio - Created for educational purposes and cybersecurity.
