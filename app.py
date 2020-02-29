import tkinter as tk


def change_text(btn):
    display['text'] = str(display['text'])
    display['text'] += str(btn)
    # print(type(btn))


def get_displyed_value():
    display['text'] = eval(display['text'])


def clear():
    display['text'] = ''

def delete():
    display['text'] = str(display['text'][0: len(display['text']) - 1])





gui = tk.Tk()

gui.title("Calculator")

# Make a canvas.
canvas = tk.Canvas(width=400, height=600, bg="white")
canvas.pack()

# Frame for our Screen.
frame = tk.Frame(canvas, bg="#d4d6d5", bd=3)
frame.place(relx=.01, rely=.03, relwidth=.98, relheight=.13)

# Cal Screen.
display = tk.Label(frame, bg="#fff", font=40, anchor="e", justify="right")
display.place(relwidth=1, relheight=1)

# Frame for Delete
frame = tk.Frame(canvas, bg='#c5c5c5', bd=3)
frame.place(relx=.01, rely=.17, relwidth=.98, relheight=.055)

button = tk.Button(frame, text='Del', font=15, bg='#4f4a3c', fg='#cca952', command=delete)
button.place(relx=0, rely=0, relwidth=1, relheight=1)

# Frame for our Cancel.
frame = tk.Frame(canvas, bg="#c5c5c5", bd=3)
frame.place(relx=.01, rely=.23, relwidth=.98, relheight=.06)

button = tk.Button(frame, text='C', font=15, fg="#cca952", bg= '#4f4a3c', command=clear)
button.place(relx=0, rely=0, relwidth=1, relheight=1)

frame = tk.Frame(canvas, bg="#d4d6d5", bd=3)
frame.place(relx=.01, rely=.30, relwidth=.98, relheight=.65)

# First roll
button = tk.Button(frame, text="7", font=40, command=lambda: change_text(7))
button.place(relx=0, rely=0, relwidth=.25, relheight=.25)

button = tk.Button(frame, text="8", font=40, command=lambda: change_text(8))
button.place(relx=.25, rely=0, relwidth=.25, relheight=.25)

button = tk.Button(frame, text="9", font=40, command=lambda: change_text(9))
button.place(relx=.50, rely=0, relwidth=.25, relheight=.25)

button = tk.Button(frame, text="/", font=40, command=lambda: change_text('/'))
button.place(relx=.75, rely=0, relwidth=.25, relheight=.25)

# 2 roll
button = tk.Button(frame, text="4", font=40, command=lambda: change_text(4))
button.place(relx=0, rely=.25, relwidth=.25, relheight=.25)

button = tk.Button(frame, text="5", font=40, command=lambda: change_text(5))
button.place(relx=.25, rely=.25, relwidth=.25, relheight=.25)

button = tk.Button(frame, text="6", font=40, command=lambda: change_text(6))
button.place(relx=.50, rely=.25, relwidth=.25, relheight=.25)

button = tk.Button(frame, text="*", font=40, command=lambda: change_text('*'))
button.place(relx=.75, rely=.25, relwidth=.25, relheight=.25)

# 3 roll
button = tk.Button(frame, text="1", font=40, command=lambda: change_text(1))
button.place(relx=0, rely=.50, relwidth=.25, relheight=.25)

button = tk.Button(frame, text="2", font=40, command=lambda: change_text(2))
button.place(relx=.25, rely=.50, relwidth=.25, relheight=.25)

button = tk.Button(frame, text="3", font=40, command=lambda: change_text(3))
button.place(relx=.50, rely=.50, relwidth=.25, relheight=.25)

button = tk.Button(frame, text="-", font=40, command=lambda: change_text('-'))
button.place(relx=.75, rely=.50, relwidth=.25, relheight=.25)

# 4 roll
button = tk.Button(frame, text=".", font=40, command=lambda: change_text('.'))
button.place(relx=0, rely=.75, relwidth=.25, relheight=.25)

button = tk.Button(frame, text="0", font=40, command=lambda: change_text(0))
button.place(relx=.25, rely=.75, relwidth=.25, relheight=.25)

button = tk.Button(frame, text="=", font=40, command=lambda: get_displyed_value())
button.place(relx=.50, rely=.75, relwidth=.25, relheight=.25)

button = tk.Button(frame, text="+", font=40, command=lambda: change_text('+'))
button.place(relx=.75, rely=.75, relwidth=.25, relheight=.25)

# button = tk.Button(frame, text="2", command=lambda: change_text(display))
# button.place(relx=0.06, rely=0)
#
# button = tk.Button(frame, text="Click", command=lambda: change_text(display))
# # button.grid(row=0, column=1)

gui.mainloop()