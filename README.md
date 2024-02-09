    # Typing speed test
    #### Video Demo:  <https://youtu.be/5KdTQSBoKIc>
    #### Description:
    TODO

    Features
        User Registration and Login:

        Users can create accounts with unique usernames and passwords.
        Passwords are required to meet specific criteria (at least one lowercase letter, one uppercase letter, one digit, and a minimum length of 8 characters).
        Typing Test:

        Users are presented with random words and are required to type them within a given time limit (30 seconds).
        The program evaluates the user's accuracy and calculates adjusted words per minute (WPM) based on correct words typed.
        Score Tracking:

        User scores are recorded and saved in separate text files named after the user.
        Users can view their own scores or check the overall scoreboard to see the rankings of all users.
        Account Deletion:

        Users have the option to delete their accounts, which removes their user file and associated scores.
    How to Use
        Run the Program:
            Execute the program by running the provided Python script (typing_speed_test.py) in a command-line environment.
            Choose an Action:

            Upon launching, users are prompted to login, signup, take a typing test, or check the scoreboard.
    Signup:

        Users can create an account by providing a username and password. The program enforces password criteria.
    Login:

        Existing users can log in using their username and password.
    Typing Test:

        Users can take a typing test where random words are presented, and they must type them within the time limit.
    Scoreboard:

        Users can view their own scores or check the overall scoreboard to see the rankings of all users.
    Delete Account:

        Users can choose to delete their accounts, which removes their user file and associated scores.

    Dependencies
        The program uses the tabulate library for displaying a formatted scoreboard. Install it using:

        pip install tabulate
