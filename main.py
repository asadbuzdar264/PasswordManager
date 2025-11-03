from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def genrate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letter + password_symbol + password_number
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

#**********---------------DATA HANDLING WITH JSON ------------*********
    user_input= {
        website:{
            "Email":username,
            "Password":password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please Don't leave any field Empty.")
    else:
        try:
            with open("new_f.json","r") as user_file:
                data = json.load(user_file)
        except (FileNotFoundError, json.JSONDecodeError):
            with open("new_f.json", "w") as user_file:
                json.dump(user_input, user_file, indent=4)

        else:
            data.update(user_input)
            with open("new_f.json", "w") as user_file:
                json.dump(data, user_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


#-----------------------------GUESS PASSWORD-------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("new_f.json", "r") as data_file:
            user_info = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found", message="No Data File Found")

    else:
        if website in user_info:
            email = user_info[website]["Email"]
            password = user_info[website]["Password"]
            messagebox.showinfo(title=website, message=f"E-mail: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title=website, message=f"No Details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200, height=200 )
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100,100, image = lock_image)
canvas.grid(row=0,column=1)

#Labels:
website_lable = Label(text="Website:")
website_lable.grid(row=1,column=0)
username_lable = Label(text="Username/Email:")
username_lable.grid(row=2,column=0)
password_lable = Label(text="Password:")
password_lable.grid(row=3,column=0)

#Entries:
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1)
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(row=2,column=1)
username_entry.insert(0,"AsadBuzdar264")
password_entry = Entry(width=35)
password_entry.grid(row=3,column=1)

#Buttons:
genrate_password = Button(text="Generate Password", command=genrate_pass)
genrate_password.grid(row=3,column=2)
add_button = Button(text="Add",width=26, command= save)
add_button.grid(row=4,column=1)
search_button = Button(text="Search",width=14, command=find_password)
search_button.grid(row=1,column=2)


window.mainloop()