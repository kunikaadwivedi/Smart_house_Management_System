from tkinter import *
import time
import ttkthemes
from tkinter import ttk

count = 0
text = ''


def slider():
    global text, count
    if count == len(s):
        count = 0
        text = ''
    text = text + s[count]
    sliderLabel.config(text=text)
    count += 1
    sliderLabel.after(300, slider)


def clock():
    date = time.strftime('%d/%m/%Y')
    current_time = time.strftime("%H:%M:%S")
    datetimelabel.config(text=f'  Date: {date}    Time: {current_time}')
    datetimelabel.after(1000, clock)


def clock():
    date = time.strftime('%d/%m/%Y')
    current_time = time.strftime("%H:%M:%S")
    datetimelabel.config(text=f'  Date: {date}\nTime: {current_time}')
    datetimelabel.after(1000, clock)  # Updates every 1000 ms (1 second)


root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')  # Keep or change theme here
root.geometry('1420x740+10+10')
root.resizable(False, False)
root.title("Smart Home Device Management")

# Date and Time label
datetimelabel = Label(root, font=("times new roman", 18, "bold"), fg="black", bg="white")
datetimelabel.place(x=0, y=0)

clock()

# Slider for text animation
s = "Smart Home Device Management"
sliderLabel = Label(root, text=s, font=("Helvetica", 32, "italic bold"), bg="#F0F0F0", fg="blue")
sliderLabel.place(x=450, y=20)
slider()

# Set the background of the entire window
root.configure(bg="#F0F0F0")

# Left frame for buttons and logo
leftFrame = Frame(root, bg="white", relief=FLAT, bd=0)
leftFrame.place(x=50, y=80, width=400, height=630)

# Adding a logo or image
logo_image = PhotoImage(file="smart-house.png")
logoLabel = Label(leftFrame, image=logo_image, bg="white")
logoLabel.place(x=0, y=20)

# Buttons with more modern rounded styling
buttons = ["Add Device", "Search Device", "Delete Device", "Update Device", "Show Device", "Export Data", "Exit"]
y_position = 150

for button_text in buttons:
    button = Button(leftFrame, text=button_text, font=("Helvetica", 16, "bold"), bg="#87CEEB", fg="black",
                    bd=0, relief=FLAT, activebackground="#4682B4", activeforeground="white",
                    highlightthickness=0, padx=10, pady=10)
    button.place(x=50, y=y_position, width=300, height=50)
    y_position += 70

# Connect to Database Button (styled)
connectButton = ttk.Button(root, text="Connect to Database", style="TButton")
connectButton.place(x=1200, y=20)


# Right frame for device details and database operations
rightFrame = Frame(root, bg="Lavender", relief=FLAT, bd=0)
rightFrame.place(x=500, y=80, width=850, height=620)

# Adding labels and entry fields for device management
Label(rightFrame, text="Device ID", font=("Helvetica", 14), bg="white", fg="black").place(x=50, y=20)
id_entry = Entry(rightFrame, font=("Helvetica", 14), width=30, bd=2, relief=RIDGE)
id_entry.place(x=200, y=20)

Label(rightFrame, text="Device Name", font=("Helvetica", 14), bg="white", fg="black").place(x=50, y=80)
name_entry = Entry(rightFrame, font=("Helvetica", 14), width=30, bd=2, relief=RIDGE)
name_entry.place(x=200, y=80)

Label(rightFrame, text="Device Type", font=("Helvetica", 14), bg="white", fg="black").place(x=50, y=140)
type_entry = Entry(rightFrame, font=("Helvetica", 14), width=30, bd=2, relief=RIDGE)
type_entry.place(x=200, y=140)

Label(rightFrame, text="IP Address", font=("Helvetica", 14), bg="white", fg="black").place(x=50, y=200)
ip_entry = Entry(rightFrame, font=("Helvetica", 14), width=30, bd=2, relief=RIDGE)
ip_entry.place(x=200, y=200)

# Buttons for database actions with modern colors and proper spacing
add_button = Button(rightFrame, text="Add Device", font=("Helvetica", 14, "bold"), bg="#1E90FF", fg="black", bd=0, relief=FLAT,
                    activebackground="#4682B4", activeforeground="white")
add_button.place(x=100, y=300, width=220, height=50)

update_button = Button(rightFrame, text="Update Device", font=("Helvetica", 14,"bold"), bg="#32CD32", fg="black", bd=0, relief=FLAT,
                       activebackground="#4ED64E", activeforeground="white")
update_button.place(x=350, y=300, width=220, height=50)

delete_button = Button(rightFrame, text="Delete Device", font=("Helvetica", 14, "bold"), bg="#FF4500", fg="black", bd=0, relief=FLAT,
                       activebackground="#FF6347", activeforeground="white")
delete_button.place(x=600, y=300, width=220, height=50)

root.mainloop()
