import time
import logging
import pyperclip
import threading
import customtkinter as ctk
import google.generativeai as genai

logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ] [ %(levelname)s ] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

API_KEY = "Enter Your Api Key"   # Replace with your actual Gemini API key
MODEL_NAME = "gemini-1.5-flash"
genai.configure(api_key=API_KEY)

history_data = []

def test_api_key():
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        model.generate_content("Hello There! How Are You?")
        logging.info("API Key Is Valid And Working")
        return True
    except Exception as e:
        logging.error(f"API Key Error : {str(e)}")
        return False

def get_answer(question):
    if not question:
        return "Please provide a question to get an answer."
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(question)
        return response.text.strip()
    except Exception as e:
        return f"Error while generating the answer: {str(e)}"

def copy_to_clipboard(text):
    pyperclip.copy(text)

def clear_history(tab):
    global history_data
    history_data.clear()
    update_history_tab(tab)

def update_history_tab(tab):
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

    ctk.CTkLabel(tab, text="History", font=("Arial", 16, "bold")).pack(pady=10)

    for idx, (question, answer) in enumerate(history_data):
        frame = ctk.CTkFrame(scrollable_frame, border_width=2, corner_radius=8, fg_color="#f5f5f5")
        frame.pack(pady=5, padx=10, fill="x", expand=True)

        question_label = ctk.CTkLabel(
            frame,
            text=f"Q{idx + 1}: {question}",
            font=("Arial", 12, "bold"),
            anchor="w",
            text_color="#2c3e50",
            fg_color="#f5f5f5",
            wraplength=500
        )
        question_label.pack(pady=(5, 0), fill="x")

        answer_label = ctk.CTkLabel(
            frame,
            text=f"A{idx + 1}: {answer}",
            font=("Arial", 12),
            anchor="w",
            text_color="#34495e",
            fg_color="#f5f5f5",
            wraplength=500
        )
        answer_label.pack(pady=(0, 5), fill="x")

        copy_button = ctk.CTkButton(
            frame, text="Copy Answer", command=lambda ans=answer: copy_to_clipboard(ans)
        )
        copy_button.pack(pady=5)

        timestamp_label = ctk.CTkLabel(
            frame,
            text=f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}",
            font=("Arial", 10),
            anchor="e",
            text_color="#7f8c8d",
            fg_color="#f5f5f5",
        )
        timestamp_label.pack(pady=(0, 5), anchor="e")

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

def update_window_content(tab1, tab2, question, answer):
    if question and answer:
        history_data.append((question, answer))
        update_history_tab(tab2)

    for widget in tab1.winfo_children():
        widget.destroy()

    ctk.CTkLabel(tab1, text="Question:", font=("Arial", 14, "bold")).pack(pady=5)
    question_text = ctk.CTkTextbox(tab1, height=150)
    question_text.insert("1.0", question)
    question_text.configure(state="disabled")
    question_text.pack(padx=10, pady=5, fill="both", expand=True)

    ctk.CTkLabel(tab1, text="Answer:", font=("Arial", 14, "bold")).pack(pady=5)
    answer_text = ctk.CTkTextbox(tab1, height=200)
    answer_text.insert("1.0", answer)
    answer_text.configure(state="disabled")
    answer_text.pack(padx=10, pady=5, fill="both", expand=True)

    ctk.CTkButton(
        tab1, text="Copy to Clipboard", command=lambda: copy_to_clipboard(answer)
    ).pack(pady=10)

def monitor_clipboard(tab1, tab2):
    last_text = pyperclip.paste().strip()
    while True:
        current_text = pyperclip.paste().strip()
        if current_text and current_text != last_text:
            last_text = current_text
            answer = get_answer(current_text)
            update_window_content(tab1, tab2, current_text, answer)
        time.sleep(1)

def main():
    logging.info("Starting the clipboard monitoring script...")

    if not test_api_key():
        logging.error("Exiting due to invalid API key.")
        return

    global root
    root = ctk.CTk()
    root.title("Clipboard QNA Tool")
    root.geometry("600x700")
    root.attributes("-topmost", True)
    root.resizable(False, False)

    tabview = ctk.CTkTabview(root)
    tab1 = tabview.add("Current QNA")
    tab2 = tabview.add("History")
    tabview.pack(expand=True, fill="both")

    ctk.CTkButton(tab2, text="Clear History", command=lambda: clear_history(tab2)).pack(
        pady=10
    )

    ctk.CTkButton(root, text="Close", command=root.destroy).pack(pady=10)

    threading.Thread(target=lambda: monitor_clipboard(tab1, tab2), daemon=True).start()

    root.mainloop()

if __name__ == "__main__":
    main()
