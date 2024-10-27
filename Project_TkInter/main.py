from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import mysql.connector as m

mydatabase = m.connect(host="localhost", user="root", password="aryan", database="complain")
insert_query = "INSERT INTO cms(name, comp, dept_name, feedback) VALUES (%s, %s, %s, %s)"
status_query = "SELECT DISTINCT status FROM cms WHERE name = %s"
status_by_id_query = "SELECT status FROM cms WHERE id = %s"


def savePerson():
    name_1 = nameEntry.get()
    comp_1 = compEntry.get()
    dept_name_1 = departmentVar.get()  # Retrieve the selected department name
    feedback_1 = feedbackEntry.get()  # Retrieve the feedback
    cursor = mydatabase.cursor()
    cursor.execute(insert_query, (name_1, comp_1, dept_name_1, feedback_1))
    mydatabase.commit()
    messagebox.showinfo("Success", "User Registered")  # Show success message

def getStatus():
    try:
        name_1 = nameEntry.get()
        cursor = mydatabase.cursor()
        cursor.execute(status_query, (name_1,))
        status = cursor.fetchone()[0]
        messagebox.showinfo("Status", f"Status for {name_1}: {status}")
    except Exception as e:
        messagebox.showerror("Error", "Invalid Name")

tkWindow = Tk()
tkWindow.geometry('400x280')  # Increased height to accommodate status entry
tkWindow.title('Tkinter Form')

# Define custom colors
bg_color = "#FFFACD"  # Lemon Chiffon
fg_color = "#000000"  # Dark Black
entry_bg_color = "#FAF0E6"  # Linen

# Set background color for the main window
tkWindow.configure(bg=bg_color)

# Set font
custom_font = font.Font(family="Helvetica", size=12)
nameLabel = Label(tkWindow, text="Name", bg=bg_color, fg=fg_color, font=custom_font)
nameLabel.grid(row=0, column=0)
nameEntry = Entry(tkWindow, bg=entry_bg_color, fg=fg_color, font=custom_font)
nameEntry.grid(row=0, column=1)

compLabel = Label(tkWindow, text="Complain", bg=bg_color, fg=fg_color, font=custom_font)
compLabel.grid(row=1, column=0)
compEntry = Entry(tkWindow, bg=entry_bg_color, fg=fg_color, font=custom_font)
compEntry.grid(row=1, column=1)

departmentLabel = Label(tkWindow, text="Department", bg=bg_color, fg=fg_color, font=custom_font)
departmentLabel.grid(row=2, column=0)
departmentVar = StringVar(tkWindow)
departmentVar.set("Roti")  # Default value
departmentMenu = OptionMenu(tkWindow, departmentVar, "Roti", "Chawal", "Dal", "Bhaji")
departmentMenu.grid(row=2, column=1)

feedbackLabel = Label(tkWindow, text="Feedback", bg=bg_color, fg=fg_color, font=custom_font)
feedbackLabel.grid(row=3, column=0)
feedbackEntry = Entry(tkWindow, bg=entry_bg_color, fg=fg_color, font=custom_font)
feedbackEntry.grid(row=3, column=1)

saveButton = Button(tkWindow, text="Save", command=savePerson, bg="#FFFACD", fg="#8B0000", font=custom_font)  # lemon chiffon button
saveButton.grid(row=4, column=0, columnspan=2)

getStatusButton = Button(tkWindow, text="Get Status", command=getStatus, bg="#FFFACD", fg="#8B0000", font=custom_font)  # lemon chiffon button
getStatusButton.grid(row=5, column=0, columnspan=2)

tkWindow.mainloop()
