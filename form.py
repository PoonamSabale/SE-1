from Tkinter import *

def save_info():
    name_info = name.get()
    gender_info = gender.get()
    dob_info = dob.get()
    age_info = age.get()
    mobile_info = mobile.get()
    address_info = address.get()
    date_info = date.get()
    
    file = open("details.txt","a")
    
    file.write("Name :- " + name_info)
    file.write("\n")
    
    file.write("Gender :- " + gender_info)
    file.write("\n")
    
    file.write("DOB :- " + dob_info)
    file.write("\n")
    
    file.write("Age :- " + str(age_info))
    file.write("\n")
    
    file.write("Mobile no :- " + mobile_info)
    file.write("\n")
    
    file.write("Address :- " + address_info)
    file.write("\n")
    
    file.write("Date :- " + date_info)
    file.write("\n")
    file.write(" ")
    
    file.close()
    
    print("Record saved successfully.\n")

    name_entry.delete(0, END)
    gender_entry.delete(0, END)
    dob_entry.delete(0, END)
    age_entry.delete(0, END)
    mobile_entry.delete(0, END)
    address_entry.delete(0, END)
    date_entry.delete(0, END)
    

form = Tk()

form.geometry("700x700")

form.title("Vaccination Form")

heading = Label(text="Vaccination Form",fg="black",bg="yellow",width="500",height="3",font="10")

heading.pack()

name_text = Label(text="Name :")
gender_text = Label(text="Gender :")
dob_text = Label(text="DOB :")
age_text = Label(text="Age :")
mobile_text = Label(text="Mobile no :")
address_text = Label(text="Address :")
date_text = Label(text="Date :")

name_text.place(x=15,y=70)
gender_text.place(x=15,y=140)
dob_text.place(x=15,y=210)
age_text.place(x=15,y=280)
mobile_text.place(x=15,y=350)
address_text.place(x=15,y=420)
date_text.place(x=15,y=490)

name = StringVar()
gender = StringVar()
dob = StringVar()
age = IntVar()
mobile = StringVar()
address = StringVar()
date = StringVar()

name_entry = Entry(textvariable=name,width="30")
gender_entry = Entry(textvariable=gender,width="30")
age_entry = Entry(textvariable=age,width="30")
dob_entry = Entry(textvariable=dob,width="30")
mobile_entry = Entry(textvariable=mobile,width="30")
address_entry = Entry(textvariable=address,width="30")
date_entry = Entry(textvariable=date,width="30")

name_entry.place(x=15,y=100)
gender_entry.place(x=15,y=170)
dob_entry.place(x=15,y=240)
age_entry.place(x=15,y=310)
mobile_entry.place(x=15,y=380)
address_entry.place(x=15,y=450)
date_entry.place(x=15,y=520)


button = Button(form,text="Submit Data",command=save_info,width="30",height="2",bg="grey")

button.place(x=15,y=560)


mainloop()
