import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('Calculator')
window.geometry("250x500")

bg_color = "#292f36"
button_bg_color = "#4ecdc4"
button_text_color = "black"

window.configure(bg=bg_color)

frame = tk.Frame(master=window, bg=bg_color)
frame.pack(expand=True, fill="both")

entry = tk.Entry(master=frame, relief=tk.SUNKEN, borderwidth=3,
                 width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, ipady=10, pady=10)

icon_image = tk.PhotoImage(file="icon.png")
window.iconphoto(True, icon_image)

def myclick(number):
    entry.insert(tk.END, number)

def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

def clear():
    entry.delete(0, tk.END)

button_frame = tk.Frame(master=frame, bg=bg_color)
button_frame.grid(row=1, column=0, columnspan=4)

button_width = 7
button_height = 2

button_1 = tk.Button(master=button_frame, text='1', font=('Arial', 12), width=button_width, height=button_height, command=lambda: myclick(1), borderwidth=2, relief="ridge", bg=button_bg_color, fg=button_text_color)
button_1.grid(row=0, column=0, padx=5, pady=5)

button_2 = tk.Button(master=button_frame, text='2', font=('Arial', 12), width=button_width, height=button_height, command=lambda: myclick(2), borderwidth=2, relief="ridge", bg=button_bg_color, fg=button_text_color)
button_2.grid(row=0, column=1, padx=5, pady=5)

button_3 = tk.Button(master=button_frame, text='3',font=('Arial',12), width=button_width, height=button_height, command=lambda: myclick(3),borderwidth=2, relief="ridge", bg=button_bg_color, fg=button_text_color)
button_3.grid(row=0, column=2, padx=5, pady=5)

button_4 = tk.Button(master=button_frame, text='4',font=('Arial',12), width=button_width, height=button_height, command=lambda: myclick(4),borderwidth=2, relief="ridge", bg=button_bg_color, fg=button_text_color)
button_4.grid(row=1, column=0, padx=5, pady=5)

button_5 = tk.Button(master=button_frame, text='5',font=('Arial',12), width=button_width, height=button_height, command=lambda: myclick(5),borderwidth=2, relief="ridge", bg=button_bg_color, fg=button_text_color)
button_5.grid(row=1, column=1, padx=5, pady=5)

button_6 = tk.Button(master=button_frame, text='6',font=('Arial',12), width=button_width, height=button_height, command=lambda: myclick(6),borderwidth=2, relief="ridge", bg=button_bg_color, fg=button_text_color)
button_6.grid(row=1, column=2, padx=5, pady=5)

button_7 = tk.Button(master=button_frame, text='7',font=('Arial',12), width=button_width, height=button_height, command=lambda: myclick(7),borderwidth=2, relief="ridge", bg=button_bg_color, fg=button_text_color)
button_7.grid(row=2, column=0, padx=5, pady=5)

button_8 = tk.Button(master=button_frame, text='8',font=('Arial',12), width=button_width, height=button_height, command=lambda: myclick(8),borderwidth=2, relief="ridge", bg=button_bg_color, fg=button_text_color)
button_8.grid(row=2, column=1, padx=5, pady=5)

button_9 = tk.Button(master=button_frame, text='9',font=('Arial',12), width=button_width, height=button_height, command=lambda: myclick(9),borderwidth=2, relief="ridge", bg=button_bg_color, fg=button_text_color)
button_9.grid(row=2, column=2, padx=5, pady=5)

button_0 = tk.Button(master=button_frame, text='0',font=('Arial',12), width=button_width, height=button_height, command=lambda: myclick(0),borderwidth=2, relief="ridge", bg=button_bg_color, fg=button_text_color)
button_0.grid(row=3, column=1, padx=5, pady=5)

button_add = tk.Button(master=button_frame, text="+",font=('Arial',12), width=button_width, height=button_height, command=lambda: myclick('+'),borderwidth=2, relief="ridge", bg=button_bg_color, fg=button_text_color)
button_add.grid(row=4, column=0, padx=5, pady=5)

button_subtract = tk.Button(master=button_frame, text="-",font=('Arial',12), width=button_width, height=button_height, command=lambda: myclick('-'),borderwidth=2, relief="ridge", bg=button_bg_color, fg=button_text_color)
button_subtract.grid(row=4, column=1, padx=5, pady=5)

button_multiply = tk.Button(master=button_frame, text="x", font=('Arial',12),width=button_width, height=button_height, command=lambda: myclick('*'),borderwidth=2, relief="ridge", bg=button_bg_color, fg=button_text_color)
button_multiply.grid(row=4, column=2, padx=5, pady=5)

button_div = tk.Button(master=button_frame, text="/",font=('Arial',12), width=button_width, height=button_height, command=lambda: myclick('/'),borderwidth=2, relief="ridge", bg=button_bg_color, fg=button_text_color)
button_div.grid(row=5, column=0, padx=5, pady=5)

button_modulus = tk.Button(master=button_frame, text="%", font=('Arial',12), width=button_width, height=button_height, command=lambda: myclick('%'),borderwidth=2, relief="ridge", bg=button_bg_color, fg=button_text_color)
button_modulus.grid(row=5, column=1, padx=5, pady=5)

button_clear = tk.Button(master=button_frame, text="Clear",font=('Arial',12), width=button_width, height=button_height, command=clear,borderwidth=2, relief="ridge", bg=button_bg_color, fg=button_text_color)
button_clear.grid(row=5, column=2, padx=5, pady=5)

button_equal = tk.Button(master=button_frame, text="=", font=('Arial', 12), width=20, height=button_height, command=equal, borderwidth=2, relief="ridge", bg=button_bg_color, fg=button_text_color)
button_equal.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

window.mainloop()
