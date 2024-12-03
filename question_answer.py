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

API_KEY = (
    "Your Gemini API Key"  # Replace with your actual Gemini API key
)
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
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()


def clear_history(tab):
    global history_data
    history_data.clear()
    update_history_tab(tab)


def update_history_tab(tab):
    for widget in tab.winfo_children():
        widget.destroy()

    frame = ctk.CTkFrame(tab, fg_color="transparent")
    frame.pack(fill="both", expand=True)

    canvas = ctk.CTkCanvas(frame, highlightthickness=0, bg="#2A2A2A")
    scrollbar = ctk.CTkScrollbar(
        frame, orientation="vertical", command=canvas.yview, fg_color="#1C1C1C"
    )
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    scrollable_frame = ctk.CTkFrame(canvas, fg_color="transparent")
    scrollable_frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    for idx, (question, answer) in enumerate(history_data):
        frame_item = ctk.CTkFrame(
            scrollable_frame,
            border_width=0,
            corner_radius=10,
            fg_color="#3A3A3A",
        )
        frame_item.pack(pady=10, padx=10, fill="x")

        question_label = ctk.CTkLabel(
            frame_item,
            text=f"Q{idx + 1}: {question}",
            font=("Arial", 13, "bold"),
            text_color="#F1F1F1",
            anchor="w",
        )
        question_label.pack(padx=10, pady=(8, 5), fill="x")

        answer_label = ctk.CTkLabel(
            frame_item,
            text=f"A{idx + 1}: {answer}",
            font=("Arial", 12),
            text_color="#D1D1D1",
            wraplength=500,
            anchor="w",
        )
        answer_label.pack(padx=10, pady=(0, 10), fill="x")

        copy_button = ctk.CTkButton(
            frame_item,
            text="Copy Answer",
            command=lambda ans=answer: copy_to_clipboard(ans),
            corner_radius=5,
            fg_color="#1C8D73",
            hover_color="#147A63",
            text_color="white",
            font=("Arial", 12, "bold"),
        )
        copy_button.pack(pady=(5, 10))

    def resize_canvas(event):
        canvas_width = event.width
        canvas_height = event.height
        canvas.config(width=canvas_width, height=canvas_height)

    frame.bind("<Configure>", resize_canvas)


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

    def check_clipboard():
        nonlocal last_text
        current_text = pyperclip.paste().strip()
        if current_text and current_text != last_text:
            last_text = current_text
            answer = get_answer(current_text)
            root.after(
                0, lambda: update_window_content(tab1, tab2, current_text, answer)
            )
        root.after(1000, check_clipboard)

    check_clipboard()


def main():
    logging.info("Starting The Clipboard Monitoring Script ...")

    if not test_api_key():
        logging.error("Exiting Due To Invalid API Key.")
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
