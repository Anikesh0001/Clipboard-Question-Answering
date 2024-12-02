import time
import logging

import pyperclip
import threading

import customtkinter as ctk
import google.generativeai as genai

# Configuring Logging
logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ] [ %(levelname)s ] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Gemini API Configuration
API_KEY = "Enter Your Api Key"   # Replace with your actual Gemini API key
MODEL_NAME = "gemini-1.5-flash"
genai.configure(api_key=API_KEY)

history_data = []  # List To Store History Data


def test_api_key():
    """Test If The Key Is Valid By Making A Sample Request"""
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        model.generate_content("Hello There! How Are You?")
        logging.info("API Key Is Valid And Working")
        return True

    except Exception as e:
        logging.error(f"API Key Error : {str(e)}")
        return False


def get_answer(question):
    """Get The Answer For The Given Question Using The Gemini API"""
    if not question:
        return "Please provide a question to get an answer."

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(question)
        return response.text.strip()

    except Exception as e:
        return f"Error while generating the answer: {str(e)}"


def copy_to_clipboard(text):
    """Copy Text To Clipboard"""
    pyperclip.copy(text)


def clear_history(tab):
    """Clear The History Tab Data"""
    global history_data
    history_data.clear()
    update_history_tab(tab)


def update_history_tab(tab):
    """Update The Content Of The History Tab"""
    for widget in tab.winfo_children():
        widget.destroy()

    canvas = ctk.CTkCanvas(tab)
    scrollbar = ctk.CTkScrollbar(tab, command=canvas.yview)
    scrollable_frame = ctk.CTkFrame(canvas)

    scrollable_frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    for idx, (question, answer) in enumerate(history_data):
        frame = ctk.CTkFrame(scrollable_frame, border_width=1, corner_radius=8)
        frame.pack(pady=10, padx=10, fill="x", expand=True)

        # Display Question
        ctk.CTkLabel(
            frame,
            text=f"Q{idx + 1}: {question}",
            font=("Arial", 12, "bold"),
            anchor="w",
        ).pack(pady=5, fill="x")

        # Display Answer
        ctk.CTkLabel(
            frame, text=f"A{idx + 1}: {answer}", font=("Arial", 12), anchor="w"
        ).pack(pady=5, fill="x")

        # Button To Copy Answer
        ctk.CTkButton(
            frame, text="Copy Answer", command=lambda ans=answer: copy_to_clipboard(ans)
        ).pack(pady=5)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")


def update_window_content(tab1, tab2, question, answer):
    """Update The Content Of The Main Window"""
    # Add New Data To History
    if question and answer:
        history_data.append((question, answer))
        update_history_tab(tab2)

    # Update The Current QNA Tab
    for widget in tab1.winfo_children():
        widget.destroy()

    # Display The Question
    ctk.CTkLabel(tab1, text="Question:", font=("Arial", 14, "bold")).pack(pady=5)
    question_text = ctk.CTkTextbox(tab1, height=150)
    question_text.insert("1.0", question)
    question_text.configure(state="disabled")
    question_text.pack(padx=10, pady=5, fill="both", expand=True)

    # Display The Answer
    ctk.CTkLabel(tab1, text="Answer:", font=("Arial", 14, "bold")).pack(pady=5)
    answer_text = ctk.CTkTextbox(tab1, height=200)
    answer_text.insert("1.0", answer)
    answer_text.configure(state="disabled")
    answer_text.pack(padx=10, pady=5, fill="both", expand=True)

    # Button To Copy Answer
    ctk.CTkButton(
        tab1, text="Copy to Clipboard", command=lambda: copy_to_clipboard(answer)
    ).pack(pady=10)


def monitor_clipboard(tab1, tab2):
    last_text = pyperclip.paste().strip()  # Initial Clipboard Text
    while True:
        current_text = pyperclip.paste().strip()
        if current_text and current_text != last_text:
            last_text = current_text
            answer = get_answer(current_text)
            update_window_content(tab1, tab2, current_text, answer)
        time.sleep(1)


def main():
    logging.info("Starting the clipboard monitoring script...")

    # Test If The API Key Is Valid
    if not test_api_key():
        logging.error("Exiting due to invalid API key.")
        return

    # Main Window Configuration
    global root
    root = ctk.CTk()
    root.title("Clipboard QNA Tool")
    root.geometry("600x700")
    root.attributes("-topmost", True)  # Always On Top
    root.resizable(False, False)

    # Create Tabs
    tabview = ctk.CTkTabview(root)
    tab1 = tabview.add("Current QNA")
    tab2 = tabview.add("History")
    tabview.pack(expand=True, fill="both")

    # Add Clear History Button
    ctk.CTkButton(tab2, text="Clear History", command=lambda: clear_history(tab2)).pack(
        pady=10
    )

    # Add Close Button
    ctk.CTkButton(root, text="Close", command=root.destroy).pack(pady=10)

    # Start Monitoring Clipboard In A Separate Thread
    threading.Thread(target=lambda: monitor_clipboard(tab1, tab2), daemon=True).start()

    root.mainloop()


if __name__ == "__main__":
    main()
