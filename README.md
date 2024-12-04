# Clipboard Question Answering

This project is a clipboard monitoring bot that automatically generates answers to questions copied to the clipboard using the Gemini API. It displays the generated answers in a dialog box.

## Features

- **Clipboard Monitoring**: Continuously monitors the clipboard for new text (questions).
- **AI-Powered Answers**: Uses the Gemini API to generate answers for the copied questions.
- **Background Operation**: Runs in the background, checking the clipboard for changes and updating in real-time.

## Demo Video

![Demo](Demo.gif)

## Prerequisites

Before you start, make sure you have the following installed:

- **Python 3.x**: Required to run the bot.
- **Gemini API Key**: You need a valid Gemini API key to interact with the Gemini API.
- **Required Python Packages**:
  - `google-generativeai`
  - `customtkinter`
  - `CTkMessagebox`
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
   - Run the script and enter the Gemini API key when asked for. ( Only required for the first run )

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
- **`update_history_tab(tab)`**: Dynamically updates the History tab with the list of all previously asked questions and their corresponding answers. Each question-answer pair includes a "Copy Answer" button.
- **`update_window_content(tab1, tab2, question, answer)`**: Updates the content of the "Current QNA" tab with the latest question and answer.
- **`update_chat_tab(chat_tab)`**: Updates the Chat with AI tab to display a list of all interactions (questions and answers) in a scrollable format, with options to submit new questions.
- **`monitor_clipboard(tab1, tab2)`**: Continuously monitors the clipboard for new text, checks if it's a new question, and fetches the answer using the Gemini API.
- **`main()`**: Initializes the application, creates the CustomTkinter GUI, and starts the clipboard monitoring thread.

## GUI Overview

- **Tab 1: Current QNA**  
  Displays the current question and its answer with a button to copy the answer to the clipboard.

- **Tab 2: History**  
  Displays a scrollable list of previously asked questions and their answers with a "Clear History" button.

- **Tab 3: Chat with AI**  
  Allows users to interact with the AI by entering a question and receiving an instant answer.

- **Close Button**  
  Gracefully exits the application.

## Future Enhancements

- [ ] **Dark Mode Customization**: The UI is already dark-themed but can be made customizable.
- [ ] **Answer Summarization**: Add the option to summarize lengthy answers.
- [x] **API Key Management**: A GUI-based form to manage the Gemini API key directly from the app.
- [ ] **Offline Storage**: Store Q&A history in a local file or database to maintain a persistent history across sessions.

### How to Contribute

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new pull request.

## License

This project is open source and available under the [MIT License](LICENSE).
