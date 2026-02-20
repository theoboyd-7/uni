from tkinter import Tk, Frame, Label, Button, messagebox, filedialog, StringVar
from backend import wc

class FileStatsApp:
    def __init__(self):
        self.win = Tk()
        self.win.title("File Analyzer")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        self.result = StringVar(value="Results will show once file added")

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        analyze_button = Button(
            self.main_frame, 
            text="Select File", 
            command=self.process_file,
        )
        analyze_button.grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        result_label = Label(
            self.main_frame, 
            textvariable=self.result
        )
        result_label.grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        close_button = Button(
            self.main_frame, 
            text="Close", 
            command=self.win.destroy
        )
        close_button.grid(
            row=2,
            column=0,
            padx=5,
            pady=5
        )

    def process_file(self):
        filename = filedialog.askopenfilename(
            title="Select a file",
            filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
        )
        
        if not filename:
            return None
            
        try:
            chars, words, lines = wc(filename)
            self.result.set(f"File Stats: {filename.split('/')[-1]}\n\nCharacters: {chars}\nWords: {words}\nLines: {lines}")
            
        except FileNotFoundError:
            messagebox.showerror("Error", f"Could not find the file:\n{filename}")


def main():
    app = FileStatsApp()
    app.run()


main()