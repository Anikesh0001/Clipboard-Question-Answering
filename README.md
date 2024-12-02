# Clipboard Question Answering

This project is a clipboard monitoring bot that automatically generates answers to questions copied to the clipboard using the Gemini API. It displays the generated answers in a dialog box.

## Features

- **Clipboard Monitoring**: Continuously monitors the clipboard for new text (questions).
- **AI-Powered Answers**: Uses the Gemini API to generate answers for the copied questions.
- **Background Operation**: Runs in the background, checking the clipboard for changes and updating in real-time.

## Demo Video

*Coming soon!*

## Prerequisites

Before you start, make sure you have the following installed:

- **Python 3.x**: Required to run the bot.
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
   - Display the answer in a dialog box.

## How It Works

1. **API Key Validation**: The script starts by verifying that your Gemini API key is valid by making a test request. If the key is valid, it proceeds; otherwise, it logs an error and exits.
2. **Clipboard Monitoring**: The bot continuously monitors the clipboard for new text (questions). Once new text is detected, the bot sends the question to the Gemini API to fetch an answer.
3. **Answer Generation**: The question is processed using the Gemini API, which generates a response. The answer is then returned and displayed in the application window.
4. **UI Updates**:
   - **Current QNA Tab**: Displays the copied question and its generated answer. A button is available to copy the answer back to the clipboard.
   - **History Tab**: Displays all previously asked questions and their corresponding answers, with an option to clear the history.
5. **Continuous Operation**: The bot runs in the background, checking the clipboard every second for changes. Whenever new content is copied, the bot updates the interface with the question and its answer.

## Code Explanation

- **`test_api_key()`**: Validates the Gemini API key by making a sample request. If the key is valid, it logs the success message; otherwise, it logs an error.
- **`get_answer(question)`**: Sends the given question to the Gemini API and fetches the response. If there’s an error, it returns a message indicating the failure.
- **`copy_to_clipboard(text)`**: Copies the provided text to the clipboard using the `pyperclip` library.
- **`clear_history(tab)`**: Clears the history stored in the `history_data` list and updates the history tab in the GUI.
- **`update_history_tab(tab)`**: Refreshes the history tab with the list of all past questions and answers. It dynamically generates a list of frames containing each question-answer pair and a button to copy the answer to the clipboard.
- **`update_window_content(tab1, tab2, question, answer)`**: Updates the "Current QNA" tab with the latest question and answer. It also appends the data to the history and refreshes the history tab.
- **`monitor_clipboard(tab1, tab2)`**: Continuously monitors the clipboard for new text. When new text is detected, it calls `get_answer()` to fetch the answer and updates the window with the result. This runs in a separate thread to allow continuous clipboard monitoring while the UI remains responsive.
- **`main()`**: The entry point of the application, where the GUI window is created using `customtkinter`. It sets up the tabs for "Current QNA" and "History", starts the clipboard monitoring in a background thread, and manages the main event loop.


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

