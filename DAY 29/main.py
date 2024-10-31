from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []


    letter_list = [random.choice(letters) for x in range(nr_letters)]
    symbol_list = [random.choice(symbols) for x in range(nr_symbols)]
    number_list = [random.choice(numbers) for x in range(nr_numbers)]

    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)

    password = "".join(password_list)

    input_password.insert(0,password )
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    if len(input_password.get()) == 0 or len(input_website.get()) == 0:
        is_empty = messagebox.showinfo(title="missing info", message= "Please dont leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title="website",
                                       message=f"These are the details entered: \n Email:{input_email.get()} "
                                               f"\n Password:{input_password.get()} \n Is it ok to save ?")
        if is_ok:
            with open('data.txt', 'a+') as file:
                file.write(f" {input_website.get()}| {input_email.get()}|{input_password.get()} \n")

            #remove all the data from the fields
            input_website.delete(0, END)
            input_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 20, pady= 20)



#canvas
canvas = Canvas(width = 200, height = 200, highlightthickness = 0)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100, image = logo_img)
canvas.grid(column = 1, row = 0)

#Label- Website
my_label_website = Label(text = "Website:")
my_label_website.grid(column= 0, row = 1)


#Label- Email/Username
my_label_website = Label(text = "Email/Username")
my_label_website.grid(column= 0, row = 2)

#Label- Password
my_label_website = Label(text = "Password")
my_label_website.grid(column= 0, row = 3)

#Button - Generate Password
button_generate = Button(text = "Generate", command = generate_password)
button_generate .grid(column= 2, row = 3)

#Button - ADD
button_add = Button(text = "ADD", width=36, command = save)
button_add.grid(column= 1, row = 4 , columnspan = 2)


#Entry - Website
input_website = Entry(width = 35)
input_website.grid(column= 1, row = 1 , columnspan = 2)
input_website.focus()

#Entry - Email/Username
input_email = Entry(width = 35)
input_email.grid(column= 1, row = 2 , columnspan = 2)
input_email.insert(0, "maxmuster@gmail.com")

#Entry - password
input_password = Entry(width = 21 )
input_password.grid(column= 1, row = 3 )


window.mainloop()