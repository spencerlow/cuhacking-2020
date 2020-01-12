import tkinter as tk


# window = TK()
# window.title("test")

window = tk.Tk()
window.geometry("600x600")
window.title("Murder mystery")
window.resizable(False, False)
window.configure(background="blue")

def first_function():
    text = "test text here"
    textoutput = tk.Label(window, text = text, fg="red", font=("Helvetica",16))
    textoutput.grid(row=0,column=1)

testButton = tk.Button(text = "door", command = first_function)
testButton.grid(row=0, column=0)

# new comment additional line



if __name__ == "__main__":
    window.mainloop()
