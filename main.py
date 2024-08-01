import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Rent it.")

# Define the main frame
main_frame = tk.Frame(root, bg="white")
main_frame.pack(fill="both", expand=True)

# Add the top menu
top_menu = tk.Frame(main_frame, bg="#2B4064")
top_menu.pack(side="top", fill="x")

# Add the logo
logo_image = Image.open("E:\ZZZZ Rental/logo2.png")
logo_image = logo_image.resize((110, 40), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(top_menu, image=logo_photo, bg="#2B4064")
logo_label.pack(side="left", padx=20, pady=20)

home_button = tk.Button(top_menu, text="Home", fg="white", bg="#2B4064", borderwidth=0, font=("Helvetica", 14))
home_button.pack(side="left", padx=30, pady=40)

about_button = tk.Button(top_menu, text="About", fg="white", bg="#2B4064", borderwidth=0, font=("Helvetica", 14))
about_button.pack(side="left", padx=30, pady=20)

categories_button = tk.Button(top_menu, text="Categories", fg="white", bg="#2B4064", borderwidth=0, font=("Helvetica", 14))
categories_button.pack(side="left", padx=30, pady=20)

more_button = tk.Button(top_menu, text="More", fg="white", bg="#2B4064", borderwidth=0, font=("Helvetica", 14))
more_button.pack(side="left", padx=10, pady=10)

# Create the rectangle background for the sign-in button
sign_in_button_frame = tk.Frame(top_menu, bg="#2B4064", padx=10, pady=5, relief="groove", borderwidth=2)
sign_in_button_frame.pack(side="right", padx=30, pady=10)

sign_in_button = tk.Button(sign_in_button_frame, text="Sign in", fg="white", bg="#2B4064", borderwidth=0, font=("Helvetica", 14))
sign_in_button.pack(padx=10, pady=5)

# Create the left frame and right frame
left_frame = tk.Frame(main_frame, bg="white")
right_frame = tk.Frame(main_frame, bg="white")

# Pack the left and right frames side-by-side
left_frame.pack(side="left", fill="both", expand=True, padx=50, pady=100,anchor="center")
right_frame.pack(side="left", fill="both", expand=True, padx=50, pady=100,anchor="center")

# Add the "Rent Almost Anything" image to the left frame
left_image = Image.open("E:\ZZZZ Rental/left.png")
left_image = left_image.resize((500, 400), Image.LANCZOS)
left_photo = ImageTk.PhotoImage(left_image)
left_label = tk.Label(left_frame, image=left_photo, bg="white")
left_label.pack(pady=10)

# Create the rectangle box and center it in the right frame
rectangle_box = tk.Frame(right_frame, bg="#2B4064", padx=300, pady=300, relief="groove", borderwidth=2)
rectangle_box.place(in_=right_frame, relx=0.5, rely=0.5, anchor="center")

# Add the "Welcome" label and login fields to the rectangle box
welcome_label = tk.Label(rectangle_box, text="Welcome", fg="white", bg="#2B4064", font=("Helvetica", 24, "bold"))
welcome_label.pack(pady=20)

login1_label = tk.Label(rectangle_box, text="Login to your account to continue", fg="white", bg="#2B4064", font=("Helvetica", 12))
login1_label.pack(pady=0)

username_entry = tk.Entry(rectangle_box, width=30, font=("Helvetica", 14), relief="groove", borderwidth=1)
username_entry.pack(pady=10)
username_entry.insert(0, "Username")

password_entry = tk.Entry(rectangle_box, width=30, show="*", font=("Helvetica", 14), relief="groove", borderwidth=1)
password_entry.pack(pady=10)
password_entry.insert(0, "Password")

forgot_password_button = tk.Button(rectangle_box, text="forgot password?", fg="white", bg="#2B4064", borderwidth=0, font=("Helvetica", 12))
forgot_password_button.pack(pady=5)

def login():
    username = username_entry.get()
    password = password_entry.get()
    # Add your login logic here
    print(f"Username: {username}, Password: {password}")

login_button = tk.Button(rectangle_box, text="Login", fg="white", bg="#2B4064", borderwidth=0, font=("Helvetica", 14), command=login)
login_button.pack(pady=10)

create_account_button = tk.Button(rectangle_box, text="New to Rent it ? Create Account", fg="white", bg="#2B4064", borderwidth=0, font=("Helvetica", 12))
create_account_button.pack(pady=30)

# Apply shadow effect to the rectangle box
shadow_color = "#888888"
shadow_offset = 500
shadow_frame = tk.Frame(main_frame, bg=shadow_color, padx=shadow_offset, pady=shadow_offset)
shadow_frame.place(in_=rectangle_box, relx=0, rely=0, relwidth=1, relheight=1, anchor="nw")
shadow_frame.lower()

# Run the main loop
root.mainloop()