import tkinter
from tkinter import messagebox
import string
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, ''.join(random.choice(string.ascii_uppercase) for i in range(10)))

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_information():

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Alert", message="Please fill up the data...")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f" Is it ok to save? ")

        if is_ok:
            with open("password_data.txt", "a") as file:
                file.write(f" {website_entry.get()} | {username_entry.get()} | {password_entry.get()} \n")
                website_entry.delete(0, tkinter.END)
                username_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)





# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label
website_label = tkinter.Label(text="Website")
website_label.grid(column=0, row=1)

username_label = tkinter.Label(text="Email/Username")
username_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password")
password_label.grid(column=0, row=3)

# Entry
website_entry = tkinter.Entry(width=35)

website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = tkinter.Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(tkinter.END, "ugalrube@gmail.com")

password_entry = tkinter.Entry(width=18)
password_entry.grid(column=1, row=3)

# Button
generate_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=33, command=add_information)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
