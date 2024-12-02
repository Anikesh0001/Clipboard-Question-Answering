# Clipboard Question Answering Bot

This project is a clipboard monitoring bot that uses the Gemini API to generate answers to questions copied to the clipboard. It displays the answers in a dialog box on macOS.

## Features

- Monitors the clipboard for new text (questions).
- Uses the Gemini API to generate answers to the questions.
- Displays the answers in a macOS dialog box.
- Runs continuously in the background, checking the clipboard for changes.

  ## Demo Video

<video width="640" height="360" controls>
  <source src="demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Prerequisites

- Python 3.x
- macOS (for the AppleScript dialog box functionality)
- Gemini API key
- Required Python packages: `google-generativeai`, `pyperclip`

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/clipboard-question-answering-bot.git
    cd clipboard-question-answering-bot
    ```

2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```sh
    pip install google-generativeai pyperclip
    ```

4. Replace the `API_KEY` in the script with your actual Gemini API key.

## Usage

1. Ensure you are in the virtual environment:

    ```sh
    source venv/bin/activate
    ```

2. Run the script:

    ```sh
    python clipboard_bot.py
    ```

3. The bot will start monitoring the clipboard for questions. Copy any question to the clipboard, and the bot will fetch the answer using the Gemini API and display it in a macOS dialog box.

## How It Works

1. The script configures the Gemini API with your API key.
2. It enters a loop that continuously checks the clipboard for new text.
3. If new text is detected, it is sent to the Gemini API to generate an answer.
4. The generated answer is displayed in a macOS dialog box using AppleScript.

## Code Explanation

- `get_answer(question)`: Fetches an answer from the Gemini API for the given question.
- `escape_quotes(text)`: Escapes quotes for use in AppleScript.
- `show_answer(answer)`: Displays the answer in a macOS dialog box using AppleScript.
- `main()`: Monitors the clipboard for changes and processes new text to get and display answers.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.


