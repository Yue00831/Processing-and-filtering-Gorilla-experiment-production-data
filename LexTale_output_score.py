import pandas as pd
import tkinter as tk
from tkinter import filedialog

def calculate_lextale_score():
    root = tk.Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename(
        title="Select LexTALE Excel file",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )
    
    if not file_path:
        print("No file selected.")
        return

    df = pd.read_excel(file_path)

    # check the necessary columns, make sure they exist
    if 'Correct' not in df.columns or 'type' not in df.columns:
        print("Required columns ('Correct' and 'type') not found in the file.")
        return

    # calculate scores
    words_correct = df[(df['type'] == 'word') & (df['Correct'] == 1)].shape[0]
    nonwords_correct = df[(df['type'] == 'non') & (df['Correct'] == 1)].shape[0]
    score = ((words_correct / 40 * 100) + (nonwords_correct / 20 * 100)) / 2

    # print results
    print(f"Words correct: {words_correct} / 40")
    print(f"Nonwords correct: {nonwords_correct} / 20")
    print(f"LexTALE Score: {round(score, 2)}")

# run the function
calculate_lextale_score()
