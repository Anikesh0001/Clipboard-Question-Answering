# Clipboard Question Answering

This project is a clipboard monitoring bot that automatically generates answers to questions copied to the clipboard using the Gemini API. It displays the generated answers in a dialog box on macOS.

## Features

- **Clipboard Monitoring**: Continuously monitors the clipboard for new text (questions).
- **AI-Powered Answers**: Uses the Gemini API to generate answers for the copied questions.
- **macOS Integration**: Displays the answers in a macOS dialog box using AppleScript.
- **Background Operation**: Runs in the background, checking the clipboard for changes and updating in real-time.

## Demo Video

*Coming soon!*

## Prerequisites

Before you start, make sure you have the following installed:

- **Python 3.x**: Required to run the bot.
- **macOS**: Required for the AppleScript functionality used to display dialog boxes.
- **Gemini API Key**: You need a valid Gemini API key to interact with the Gemini API.
- **Required Python Packages**:
  - `google-generativeai`
  - `customtkinter`
  - `pyperclip`

## Installation

Follow these steps to set up the project:

1. **Clone the repository**:

    ```sh
    git clone https://github.com/Anikesh0001/clipboard-question-answering.git
    cd clipboard-question-answering
    ```

2. **Create a virtual environment**:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required dependencies**:

    ```sh
    pip install -r 'requirements.txt'
    ```

4. **Set up your Gemini API Key**:
    - Open the script and replace the `API_KEY` placeholder with your actual Gemini API key.

## Usage

1. **Activate the virtual environment** (if not already active):

    ```sh
    source venv/bin/activate
    ```

2. **Run the script**:

    ```sh
    python question_answer.py
    ```

3. The bot will start monitoring the clipboard. Copy any question to the clipboard, and the bot will automatically:
   - Fetch the answer using the Gemini API.
   - Display the answer in a macOS dialog box.

## How It Works

1. **API Configuration**: The script sets up the Gemini API with your API key.
2. **Clipboard Monitoring**: It enters a continuous loop that checks the clipboard for any new text (questions).
3. **Generate Answer**: Once new text is detected, the bot sends the text to the Gemini API to get a response.
4. **Display Answer**: The generated answer is then displayed in a macOS dialog box using AppleScript for a seamless user experience.

## Code Explanation

- **`get_answer(question)`**: Sends the given question to the Gemini API and fetches the response.
- **`escape_quotes(text)`**: Escapes quotes in the text for compatibility with AppleScript.
- **`show_answer(answer)`**: Displays the generated answer in a macOS dialog box via AppleScript.
- **`monitor_clipboard()`**: Continuously monitors the clipboard for new questions and triggers the answer generation process when new text is detected.

## Contributing

Contributions are welcome! If you have suggestions, bug fixes, or enhancements, please open an issue or submit a pull request.

### How to Contribute

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new pull request.

## License

This project is open source and available under the [MIT License](LICENSE).

