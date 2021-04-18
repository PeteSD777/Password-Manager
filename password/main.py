from tkinter import *
from tkinter import messagebox
import random
import json
# Search function


def find_password():
    website = entry.get()
    with open('data.json', 'r') as data:
        data = json.load(data)

        if website in data:
            print("exists")

            messagebox.askokcancel(
                title=f"{website}", message=f"email: {data[website]['email']}\npassword: {data[website]['password']}")
        else:
            try:
                data[website]
            except KeyError:
                messagebox.askokcancel(
                    title="Doesnt exist", message=f" credentials for {website} non existent")
# Generate random string password


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for i in range(nr_letters)]
    password_list += [random.choice(symbols) for i in range(nr_symbols)]
    password_list += [random.choice(numbers) for i in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    up = entrypass.insert(0, password)
    entrypass.config(text=up)
    print(f"Your password is: {password}")


# Save credentials


def add():
    website = entry.get()
    mail = entrymail.get()
    password = entrypass.get()
    new_data = {
        website: {
            "email": mail,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.askokcancel(
            title="Empty", message=f"Entered email or password is empty")

    else:
        try:
            with open('data.json', 'r')as data_file:
                data = json.load(data_file)

                data.update(new_data)
        except:
            with open('data.json', 'w')as data_file:
                json.dump(new_data, data_file)
            with open('data.json', 'r') as data1:
                data = json.load(data1)

        finally:
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)

                entry.delete(0, END)

                entrypass.delete(0, END)

# UI


window = Tk()
window.config(padx=20, pady=20, bg="white")
window.title("Password Manager")
logo = PhotoImage(file='logo.png')
canvas = Canvas(width=350, height=300, bg="white", highlightthickness=0)
canvas.create_image(175, 90, image=logo)
canvas.pack()
canvas.create_text(50, 200, text="Website: ", font=("Arial", 11))
entry = Entry(width=17)
entry.focus()
entry.place(x=80, y=190)
entrymail = Entry(width=35)

entrymail.place(x=80, y=215)
entrypass = Entry(width=17)

button = Button(width=30, text="Add", command=add)
button.place(x=80, y=260)
button2 = Button(width=17, text="Generate", command=generate)
button2.place(x=180, y=235)
button3 = Button(width=17, text="Search", command=find_password)
button3.place(x=180, y=190)
entrypass.place(x=80, y=240)
canvas.create_text(50, 225, text="Email/:", font=("Arial", 11))
canvas.create_text(40, 245, text="Password", font=("Arial", 11))


window.mainloop()
