# mychatbot-project

This project is an interactive assistant built in Python that performs basic math calculations, tells jokes, and plays games. It uses the pyttsx3 library for text-to-speech functionality and pyjokes for humor. The goal is to provide an engaging user experience through voice commands and responses.

Features:
- Voice Interaction: Utilizes text-to-speech capabilities to provide audio responses.
- Math Calculations: Performs basic arithmetic operations such as addition, subtraction, multiplication, and division.
- Joke Telling: Offers a collection of jokes to lighten the user's mood.
- Game Playing: Engages users with a classic game of Rock, Paper, Scissors.
- Table Generation: Can generate and write multiplication tables for a specific number to a separate file, as well as store a range of tables in a dedicated folder.

Technologies Used:
- Python
- pyttsx3 for text-to-speech conversion
- pyjokes for fetching jokes

Installation:
To run the project, you will need Python installed on your system along with the required libraries. 
Install the necessary packages using pip:

pip install pyttsx3 pyjokes
Usage:
1. Clone the repository or download the main.py file.
2. Run the script using Python:

python main.py
3. Follow the prompts in the console to interact with the assistant. You can ask it to perform math calculations, tell jokes, or play games.

Functions:
- wspeech(text): Reads and speaks the provided text.
- jokes(): Fetches a random joke from the pyjokes library.
- math(): Handles user requests for mathematical calculations based on the command input.
- games(USER): Manages the Rock, Paper, Scissors game logic.
- create_table(n): Generates the multiplication table for a given number, prompts the user to save it to a separate file, and stores it in the designated folder.
- create_multiple_tables(n1, n2): Creates multiplication tables for a specified range of numbers and stores each table in a separate file within a folder.

Example Commands:
- "Can you do some math?"
- "Tell me a joke."
- "Let's play a game."
- "Generate the multiplication table for 5."

Contributing:
Feel free to fork the repository, make changes, and submit a pull request. Contributions and suggestions are welcome!

License:
This project is open-source and available under the MIT License.

Acknowledgments:
- Special thanks to the creators of pyttsx3 and pyjokes for their contributions to the Python community.
