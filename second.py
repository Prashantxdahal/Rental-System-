import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Rent it.")

# Create the main frame
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Create the left frame for the image
left_frame = tk.Frame(main_frame)
left_frame.pack(side="left", padx=20, pady=20)

# Load and display the camera image
camera_image = Image.open("E:\ZZZZ Rental\camera.png")
camera_image = camera_image.resize((300, 200), resample=Image.BICUBIC)
camera_photo = ImageTk.PhotoImage(camera_image)
camera_label = tk.Label(left_frame, image=camera_photo)
camera_label.pack()

# Create the right frame for the information
right_frame = tk.Frame(main_frame)
right_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)

# Add the product name
product_label = tk.Label(right_frame, text="Sony a6400 On Rent", font=("Arial", 16, "bold"))
product_label.pack(pady=10)

# Add the price
price_label = tk.Label(right_frame, text="Rs.1000 Per Day", font=("Arial", 14))
price_label.pack(pady=5)

# Add the product description
description_label = tk.Label(right_frame, text="Camera Cage for Sony Alpha a6500/a6400/a6300/a6000 etc. License-a6400 (LC-A6400) for Sony Alpha 6400 Digital Mirrorless Camera Basic In-Case Shop. The cage features a variety of 1/4\"-20 and 3/8\"-16 threaded accessory mounting holes. It also has a cold shoe mount for attaching a mic or various other accessories. With the camera housed inside the cage, you can easily access the SD card, battery/compartment, and all camera buttons and ports.", wraplength=400, justify="left")
description_label.pack(pady=10)

# Add the "Rent Now" and "Add to Wishlist" buttons
button_frame = tk.Frame(right_frame)
button_frame.pack(pady=10)

rent_button = tk.Button(button_frame, text="Rent Now", bg="green", fg="white", padx=10, pady=5)
rent_button.pack(side="left", padx=10)

wishlist_button = tk.Button(button_frame, text="Add to Wishlist", bg="blue", fg="white", padx=10, pady=5)
wishlist_button.pack(side="left", padx=10)

root.mainloop()