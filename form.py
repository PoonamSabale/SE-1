from tkinter import *
import re
from datetime import datetime


def error1():
    screen1 = Toplevel(form)
    screen1.geometry("300x90")
    screen1.title("Warning!")
    Label(screen1, text = "All fields are required", fg = "red", font = "5").pack()

def error2():
    screen1 = Toplevel(form)
    screen1.geometry("300x90")
    screen1.title("Warning!")
    Label(screen1, text = "Enter valid mobile number", fg = "red", font = "5").pack()


def error3():
    screen1 = Toplevel(form)
    screen1.geometry("400x90")
    screen1.title("Warning!")
    Label(screen1, text = "Fill the vaccination form if your are above 18", fg = "red", font = "5").pack()

def error4():
    screen1 = Toplevel(form)
    screen1.geometry("600x90")
    screen1.title("Warning!")
    Label(screen1, text = "Enter valid name in the form Mr/Mrs/Ms FirstName MiddleName LastName", fg = "red", font = "5").pack()

def error5():
    screen1 = Toplevel(form)
    screen1.geometry("600x90")
    screen1.title("Warning!")
    Label(screen1, text = "Enter date in dd-mm-yyyy format", fg = "red", font = "5").pack()

def validating_name(name):
    regex_name = re.compile(r'^(Mr\.|Mrs\.|Ms\.) ([a-z]+)( [a-z]+)*( [a-z]+)*$', re.IGNORECASE)
    res = regex_name.search(name)
    return res

def isValid_mobile(s):  
    # Begins with 0 or 91
    # Then contains 7 or 8 or 9.
    # Then contains 9 digits
    Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
    return Pattern.match(s)
   
def isvalid_date(date):
    format = "%d-%m-%Y"
    res = True
    try:
      res = bool(datetime.strptime(date, format))
    except ValueError:
      res = False
    return res
    

def save_info():
    name_info = name.get()
    gender_info = gender.get()
    dob_info = dob.get()
    age_info = age.get()
    mobile_info = mobile.get()
    address_info = address.get()

    
    
    
    if name_info == "" or gender_info == "" or dob_info == "" or age_info == "" or mobile_info == "" or address_info == "" : 
      error1()

    elif not isValid_mobile(mobile_info) :
      error2()

    elif age_info < 18 :
      error3()

    elif not validating_name(name_info):
      error4()
        
    elif not isvalid_date(dob_info):
      error5() 
    
    
    else:
      file = open("details.txt","a")
      file.write("\n")
    
      file.write("Name :-" + name_info)
      file.write("\n")
    
      file.write("Gender:- " + gender_info)
      file.write("\n")
    
      file.write("DOB:- " +  dob_info)
      file.write("\n")
    
      file.write("Age:- " + str(age_info))
      file.write("\n")
    
      file.write("Mobile:- " + mobile_info)
      file.write("\n")
    
      file.write("Address:- " + address_info)
      file.write("\n")
    
      file.close()
    
      print("Record saved successfully.\n")

      name_entry.delete(0, END)
      gender_entry.delete(0, END)
      dob_entry.delete(0, END)
      age_entry.delete(0, END)
      mobile_entry.delete(0, END)
      address_entry.delete(0, END)
     

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


name_text.place(x=15,y=70)
gender_text.place(x=15,y=140)
dob_text.place(x=15,y=210)
age_text.place(x=15,y=280)
mobile_text.place(x=15,y=350)
address_text.place(x=15,y=420)


name = StringVar()
gender = StringVar()
dob = StringVar()
age = IntVar()
mobile = StringVar()
address = StringVar()


name_entry = Entry(textvariable=name,width="30")
gender_entry = Entry(textvariable=gender,width="30")
age_entry = Entry(textvariable=age,width="30")
dob_entry = Entry(textvariable=dob,width="30")
mobile_entry = Entry(textvariable=mobile,width="30")
address_entry = Entry(textvariable=address,width="30")

name_entry.place(x=15,y=100)
gender_entry.place(x=15,y=170)
dob_entry.place(x=15,y=240)
age_entry.place(x=15,y=310)
mobile_entry.place(x=15,y=380)
address_entry.place(x=15,y=450)



button = Button(form,text="Submit Data",command=save_info,width="30",height="2",bg="grey")

button.place(x=15,y=560)


mainloop()
