import subprocess
import time
import google.generativeai as genai
import pyperclip

# Constants
API_KEY = "Enter your API Key"  # Replace with your actual Gemini API key
MODEL_NAME = "gemini-1.5-flash"

# Configure your API key
genai.configure(api_key=API_KEY)

def get_answer(question):
    """Get the answer from the Gemini API."""
    if not question:
        return "Please provide a valid question."

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(question)
        return response.text.strip()
    except Exception as e:
        return f"Error while getting answer: {str(e)}"

def escape_quotes(text):
    """Escape quotes for AppleScript."""
    return text.replace('"', '\\"')

def show_answer(answer):
    """Display the answer in a dialog box."""
    if answer:
        escaped_answer = escape_quotes(answer)
        subprocess.run(['osascript', '-e', f'display dialog "{escaped_answer}"'])

def main():
    last_text = ""
    
    # Start monitoring clipboard for questions
    while True:
        # Get the current text from the clipboard
        current_text = pyperclip.paste().strip()
        
        # Check if the clipboard text has changed
        if current_text and current_text != last_text:
            last_text = current_text
            
            # Get the answer from the API
            answer = get_answer(current_text)
            
            # Show the answer in a dialog box
            show_answer(answer)
        
        # Sleep for a short time to avoid excessive CPU usage
        time.sleep(1)

if __name__ == "__main__":
    main()
