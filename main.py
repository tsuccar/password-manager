import json
import random
# this imports all class and contants
from tkinter import *
#this imports messagebox which is itself another module
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    letter_list = [random.choice(letters) for _ in range(random.randint(8,10))]
    symbol_list = [random.choice(symbols) for _ in range(random.randint(2,4))]
    number_list = [random.choice(numbers) for _ in range(random.randint(2,4))]
    
    password_list = letter_list + symbol_list + number_list
    random.shuffle(password_list)
    password = "".join(password_list)
    print(f"Your password is: {password}")
    password_entry.delete(0,END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():

    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()
    
    new_data = {
        website_input: {
            "email": email_input,
            "password": password_input
        }
    }
    
    if len(website_input)==0 or len(password_input) ==0:
        messagebox.showinfo(title="Incomplete Entry", message= "website or passowrd not provided.")
        
    else:
        try:
            with open ("data.json","r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except json.decoder.JSONDecodeError:
            with open ("data.json", "w") as data_file:
                #Saving updated data
                json.dump(new_data, data_file, indent=4)
        except FileNotFoundError:
            with open ("data.json", "w") as data_file:
                #Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            with open ("data.json", "w") as data_file:
                #udpating old data with new data
                data.update(new_data)
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            email_entry.delete(0,END)
            email_entry.insert(0,"username@email.com")
            password_entry.delete(0,END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error, message=",message=" No Data File Found")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f" Email: {email} \n Passowrd: {password}")
            
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50,pady=50)
window.title("Password Manager")

canvas = Canvas(width=200,height=200)
lock_logo_img=PhotoImage(file="logo.png")
canvas.create_image(120,110,image=lock_logo_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = Button(text="Search",width=13,command=find_password)
search_button.grid(column=2,row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

email_entry = Entry(width=38)
email_entry.insert(0, "myemail@email.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(column=2,row=3)

add_button = Button(text="Add",width=36,command=save_data)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()

## I changed this file