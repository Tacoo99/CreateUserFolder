import tkinter
import customtkinter
import os
from PIL import Image
import ctypes

class ModalWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Success")
        self.geometry("360x300")
        self.resizable(False, False)
        self.iconbitmap("images/icon/icon.ico")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        
         #center the window
        self.transient(self.master)
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.winfo_width()) // 2
        y = (screen_height - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")
        self.lift()
        self.focus_force()
        
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logout_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "logout_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "logout_light.png")), size=(20, 20))
        self.close_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "close_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "close_light.png")), size=(20, 20))


        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid(row=0, column=0, sticky="nsew")

        self.banner_text = customtkinter.CTkLabel(self.home_frame, text="The user account has been successfully created.",
                                                  font=customtkinter.CTkFont(size=14, weight="bold"))
        self.banner_text.grid(row=0, column=0, sticky="nsew", ipady=10, padx=5, pady=6)
        
        self.description_text = customtkinter.CTkLabel(self.home_frame, text="You can log out and log in with yours.",
                                                  font=customtkinter.CTkFont(size=14))
        self.description_text.grid(row=1, column=0, sticky="sew")
        
        self.logout_button= customtkinter.CTkButton(self.home_frame, text="Logout", command=self.confirm_logout, image=self.logout_image, compound="right")
        self.logout_button.grid(row=2, column=0, pady=(15, 15), ipady=4)
        
        self.close_button= customtkinter.CTkButton(self.home_frame, text="Close window", command=self.close_window, image=self.close_image, compound="right")
        self.close_button.grid(row=3, column=0, pady=(15, 15), ipady=4)
        
        
    def confirm_logout(self):
        # Displaying a messagebox asking for logout confirmation
        result = tkinter.messagebox.askyesno("Confirmation", "Are you sure you want to log out?")

        if result:
            # Log the user off the computer
            ctypes.windll.user32.ExitWindowsEx(0, 0)
            
    def close_window(self):
        self.destroy()