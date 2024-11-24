# Quizzler App 🧠

This project is a Python-based interactive quiz application built with **Tkinter**. It fetches trivia questions from the [Open Trivia Database](https://opentdb.com/) and provides users with a True/False quiz experience. The interface updates dynamically, tracks the score, and gives feedback based on the user's answers.

## Features

- **Interactive GUI**: Built with Tkinter, the app provides a clean and user-friendly graphical interface.
- **Dynamic Question Fetching**: Retrieves trivia questions via an API, ensuring fresh content for every session.
- **Score Tracking**: Displays the user's score in real-time.
- **Feedback Mechanism**: Highlights correct answers with a green background and incorrect answers with red.
- **End of Quiz Notification**: Notifies the user when there are no more questions left.

## Setup

1. **Install Required Libraries**:
   Ensure you have Python installed along with the required libraries. Install the necessary dependencies:
   ```bash
   pip install requests
   
2. **Prepare Assets**:
   Save the true.png and false.png button images in the same directory as your script.

3. **Run the App**: Execute the script:
   python main.py
   
## How It Works
1. **Fetching Questions**:
   Questions are fetched from the Open Trivia Database using the following API endpoint:
    ```bash
   https://opentdb.com/api.php?amount=10&type=boolean
2. **Gameplay**:
  - The quiz displays one question at a time.
  - Players select "True" or "False" by clicking the corresponding button.
  - The app gives immediate feedback by changing the canvas color (green for correct, red for incorrect).
  - The score updates in real-time.
3. **End of Quiz**:
    Once all questions are answered, the app displays a message indicating the end of the quiz and disables the buttons.




   
