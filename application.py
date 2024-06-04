import cv2
import os
import customtkinter as ctk
import tkinter.messagebox as tkmb
from PIL import Image, ImageTk
from model_predict import irish_detection
new_window = None  # Define new_window as a global variable

def capture_image():
    global new_window  # Use the global new_window variable

    # Open camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        tkmb.showerror(title="Error", message="Failed to open camera")
        return

    # Capture frame
    ret, frame = cap.read()
    if not ret:
        tkmb.showerror(title="Error", message="Failed to capture image")
        return

    # Save captured image
    image_path = "captured_image.png"


    cv2.imwrite(image_path, frame)


    rslt=irish_detection("captured_image.png")

    # Release camera
    cap.release()

    # Display image path
    tkmb.showinfo(title="Captured Succesfull", message=f"The Detected Image is.\n: {rslt}")

    # Display captured image
    image = Image.open(image_path)
    image = image.resize((300, 200), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    ctk.CTkLabel(new_window, image=photo).pack()
    ctk.CTkLabel(new_window, text="Iris Based Human Identification").pack()

    # Delete captured image after displaying
    os.remove(image_path)

# Rest of the code remains the same


# Setting up GUI
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.geometry("800x800")
app.title("Iris Based Human Identification")

# Function to handle login button click
def login():

    capture_button = ctk.CTkButton(new_window, text="Capture Image", command=capture_image)
    capture_button.pack(pady=10)

# Main UI
label = ctk.CTkLabel(app, text="This is the USER INTERFACE")
label.pack(pady=20)

frame = ctk.CTkFrame(app)
frame.pack(pady=40, padx=40, fill='both', expand=True)

label = ctk.CTkLabel(frame, text='Iris Scanner')
label.pack(pady=12, padx=10)

button = ctk.CTkButton(frame, text='START', command=login)
button.pack(pady=12, padx=10)

app.mainloop()
