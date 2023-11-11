import tkinter as tk 
import random
import string

root = tk.Tk()
root.title("PASSWORD GENERATOR")
root.geometry("600x600")

frame = tk.Frame(root)
frame.pack(pady=20)

c1_var = tk.IntVar() # holds the state 
c2_var = tk.IntVar()
c3_var = tk.IntVar()
c4_var = tk.IntVar()

def generate_password():
    length = int(length_entry.get())
    selected_checkboxes = ""

    if  c1_var.get() == 1:
        selected_checkboxes += string.ascii_lowercase
    if c2_var.get() == 1:
        selected_checkboxes += string.ascii_uppercase
    if c3_var.get() == 1:
        selected_checkboxes += string.digits
    if c4_var.get() == 1:
        selected_checkboxes += string.punctuation

    password = "".join(random.choice(selected_checkboxes) for _ in range(length))
    passwordoutput.delete(0, tk.END)
    passwordoutput.insert(0, password)

def reset_password():
    length_entry.delete(0, tk.END)
    passwordoutput.delete(0, tk.END)
    c1_var.set(0)
    c2_var.set(0)
    c3_var.set(0)
    c4_var.set(0)

passwordgenerator_label = tk.Label(frame, text="PASSWORD GENERATOR", font = ("arial 28 bold"), fg="green", background="alice blue" )
passwordgenerator_label.grid(row=0, column=0, columnspan = 2)

length_label = tk.Label(frame, text="PASSWORD LENGTH:", font=("arial 15 bold"), justify="center")
length_label.grid(row=3, column=0, padx=10, pady=10)
length_entry = tk.Entry(frame, width=20, font=("arial 15"), justify="center")
length_entry.grid(row=3, column=1, padx=10, pady=10)

c1 = tk.Checkbutton(frame, text="Lowercase", variable = c1_var, width=20, font=("arial 15"))
c1.grid(row=4, column=0, columnspan=2)
c2 = tk.Checkbutton(frame, text="Uppercase", variable = c2_var, width=20, font=("arial 15"))
c2.grid(row=5, column=0, columnspan=2)
c3 = tk.Checkbutton(frame, text="Digits", variable = c3_var, width=20, font=("arial 15"))
c3.grid(row=6, column=0, columnspan=2)
c4 = tk.Checkbutton(frame, text="Special characters", variable = c4_var, width=20, font=("arial 15"))
c4.grid(row=7, column=0, columnspan=2)

def show_selected_checkboxes():
    selected_checkboxes=[] # empty list
    if c1_var.get() == 1:
        selected_checkboxes.append(c1)
    if c2_var.get() == 1:
        selected_checkboxes.append(c2)
    if c3_var.get() == 1:
        selected_checkboxes.append(c3)
    if c4_var.get() == 1:
        selected_checkboxes.append(c4)

def random_password_generator():
    generate_password()
    show_selected_checkboxes()

passwordgenerate_label = tk.Label(frame, text="GENRATED PASSWORD", font=("arial 15 bold"), justify="center")
passwordgenerate_label.grid(row=8, column=0, padx=20, pady=20)

generatepassword_button = tk.Button(frame, text="GENERATE", font=("arial 15 bold"), command=random_password_generator)
generatepassword_button.grid(row=9, column=0, columnspan=2)

passwordoutput = tk.Entry(frame, width=20, font=("arial 15"), justify="center")
passwordoutput.grid(row=8, column=1, padx=20, pady=20)

reset_button = tk.Button(frame, text ="RESET", font="arial 15 bold", command=reset_password)
reset_button.grid(row=10, column=0, columnspan=2)

root.mainloop()