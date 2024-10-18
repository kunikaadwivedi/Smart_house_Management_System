from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def login_action():
    username = usernameEntry.get()
    password = passwordEntry.get()

    # Perform input validation
    if not username or not password:
        messagebox.showwarning("Input Error", "Both username and password are required!")
    else:
        # Simulate a simple login check (this is where real validation logic would go)
        if username == "Sakshi_Punia" or username == "Kunikaa_Dwivedi" and password == "dbms1234":
            messagebox.showinfo("Login Success", "Welcome!")
            window.destroy()
            import shms
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

# Initialize window
window = Tk()
window.geometry('1250x720+0+0')
window.resizable(False, False)
window.title("Login System of Smart Home Device Management")

# Keep references to images to prevent garbage collection
window.images = []

# Set the background image
backgroundImage = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0, y=0)
window.images.append(backgroundImage)  # Keep reference

# Create the login frame with a custom background color
loginFrame = Frame(window, bg='#B0BEC5', bd=5, relief=RIDGE)
loginFrame.place(x=770, y=350, width=350, height=300)

# Load and display the logo image
logoImage = Image.open('logo.png')
resizedLogoImage = logoImage.resize((75, 75))  # Resize to 75x75 pixels
logoImageTk = ImageTk.PhotoImage(resizedLogoImage)
logoLabel = Label(loginFrame, image=logoImageTk, bg='#B0BEC5')
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)
window.images.append(logoImageTk)  # Keep reference

# Load and display the username icon
usernameImage = Image.open('users.png')
resizedUsernameImage = usernameImage.resize((30, 30))  # Resize to 30x30 pixels
usernameImageTk = ImageTk.PhotoImage(resizedUsernameImage)

# Use the resized username image in the label with custom colors
usernameLabel = Label(loginFrame, image=usernameImageTk, text=' Username:', compound=LEFT,
                      font=('Times Roman', 15), bg='#CFD8DC', fg='#37474F')
usernameLabel.grid(row=1, column=0, padx=10, pady=10)
usernameEntry = Entry(loginFrame, font=('Times Roman', 15), bg='#263238', fg='white', insertbackground='white', bd=3)
usernameEntry.grid(row=1, column=1, padx=10, pady=10, ipadx=5, ipady=5)
window.images.append(usernameImageTk)  # Keep reference

# Load and display the password icon
passwordImage = Image.open('password.png')  # Assuming you have a password icon
resizedPasswordImage = passwordImage.resize((30, 30))  # Resize to 30x30 pixels
passwordImageTk = ImageTk.PhotoImage(resizedPasswordImage)

passwordLabel = Label(loginFrame, image=passwordImageTk, text=' Password:', compound=LEFT,
                      font=('Times Roman', 15), bg='#CFD8DC', fg='#37474F')
passwordLabel.grid(row=2, column=0, padx=10, pady=10)
passwordEntry = Entry(loginFrame, show='*', font=('Times Roman', 15), bg='#263238', fg='white', insertbackground='white', bd=3)
passwordEntry.grid(row=2, column=1, padx=10, pady=10, ipadx=5, ipady=5)
window.images.append(passwordImageTk)  # Keep reference

# Add a login button with custom colors and login logic
loginButton = Button(loginFrame, text="Login", font=('Times Roman', 15, 'bold'), bg='cornflowerblue', fg='white',
                     activebackground='cornflowerblue', activeforeground='white', cursor='hand', command=login_action)
loginButton.grid(row=3, column=0, columnspan=2, pady=20)

logo_image = Image.open('logo.png')
# Start the GUI event loop
window.mainloop()
