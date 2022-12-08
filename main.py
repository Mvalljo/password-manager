from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()

    if website == "" or password == "":
        messagebox.askokcancel(title="Oops", message="Don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email}"
                                       f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry
website_input = Entry(width=52)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_username_input = Entry(width=52)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "maria@email.com")

password_input = Entry(width=33)
password_input.grid(column=1, row=3)

# Buttons
generate_pwd_button = Button(text="Generate Password")
generate_pwd_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()