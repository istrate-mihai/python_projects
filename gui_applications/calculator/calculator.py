import tkinter as tk

# screen initialization
root = tk.Tk()

# Naming the window
root.title("Calculator")

scrollbar = tk.Scrollbar(root, orient='horizontal')

entry = tk.Entry(root, width=9, font=('Arial', 38, 'bold'), state='readonly', xscrollcommand=scrollbar.set)
entry.pack(pady=(30, 10))

scrollbar.config(command=entry.xview)
scrollbar.pack()

frame1 = tk.Frame(root)
frame1.pack(side='left', anchor='n')
frame2 = tk.Frame(root)
frame2.pack(side='left', anchor='n')
frame3 = tk.Frame(root)
frame3.pack(side='left', anchor='n')
frame4 = tk.Frame(root)
frame4.pack(side='left', anchor='n')

pixel = tk.PhotoImage(width=55, height=55)

def command(text):
    entry.config(state='normal')
    entry.insert(tk.END, text)
    entry.config(state='readonly')

def cmd_equal():
    entry.config(state='normal')
    txt = entry.get().replace('X', '*')

    try:
        result = eval(txt)
    except:
        result = 'Invalid'
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)
    entry.config(state='readonly')

def cmd_ac():
    entry.config(state='normal')
    entry.delete(0, tk.END)
    entry.config(state='readonly')

def buttons(text, frame):
    button = tk.Button(
        frame,
        text=text,
        font=('Arial', 20),
        image=pixel,
        bg="#333300",
        fg="white",
        compound="center",
        command=lambda :command(text)
    )
    return button

def buttons_ops(text, frame, bg, fg):
    button = tk.Button(
        frame,
        text=text,
        font=('Arial', 20),
        image=pixel,
        bg=bg,
        fg=fg,
        activebackground="black",
        compound="center",
        command=lambda :command(text)
    )
    return button

btn1 = buttons('1',frame1).pack()
btn4 = buttons('4', frame1).pack()
btn7 = buttons('7', frame1).pack()
ac   = tk.Button(
    frame1,
    text="AC",
    font=('Arial', 20),
    image=pixel,
    bg="#666699",
    fg="white",
    compound="center",
    command=lambda: cmd_ac()).pack()

btn2 = buttons('2', frame2).pack()
btn5 = buttons('5', frame2).pack()
btn8 = buttons('8', frame2).pack()
btn0 = buttons_ops('0', frame2, '#333300', 'white').pack()

plus = buttons_ops('+', frame4, 'black', 'white').pack()
minus= buttons_ops('-', frame4,  'black', 'white').pack()
mul = buttons_ops('x', frame4, 'black', 'white').pack()
div = buttons_ops('/', frame4, 'black', 'white').pack()

btn3 = buttons('3', frame3).pack()
btn6 = buttons('6', frame3).pack()
btn9 = buttons('9', frame3).pack()

equal = tk.Button(
    frame3,
    text='=',
    font=('Arial', 20),
    image=pixel,
    bg='white',
    fg='black',
    activebackground="black",
    compound='center',
    command=lambda: cmd_equal()).pack()

root.resizable(0, 0)

# This keeps the window active
root.mainloop()
