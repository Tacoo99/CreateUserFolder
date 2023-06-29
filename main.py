import customtkinter
import os
from PIL import Image

import win32security


from ModalWindow import ModalWindow

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.toplevel_window = None

        self.title("CUF")
        self.geometry("620x450")
        self.resizable(False, False)
        self.iconbitmap("images/icon/icon2.ico")
        
        

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "banner-logo.png")), size=(110, 51))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(25, 25))
        self.info_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "info_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "info_light.png")), size=(25, 25))
        
        # self.eyeClosed = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "eyeClosed_dark.png")),
        #                                              dark_image=Image.open(os.path.join(image_path, "eyeClosed_light.png")), size=(25, 25))
        # self.eyeOpen = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "eyeOpen_dark.png")),
        #                                              dark_image=Image.open(os.path.join(image_path, "eyeOpen_dark.png")), size=(25, 25))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew" )
        self.navigation_frame.grid_rowconfigure(3, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="", image=self.logo_image)
        self.navigation_frame_label.grid(row=0, column=0, padx=0, pady=25, sticky="nsew")

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Add account",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.add_user_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Info/FAQ",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.info_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.navigation_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, sticky="s")
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["System", "Dark", "Light"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=10, sticky="s")
        


        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=2)

        self.banner_text = customtkinter.CTkLabel(self.home_frame, text="CUF - Create User Folder",
                                                  font=customtkinter.CTkFont(size=18, weight="bold"))
        self.banner_text.grid(row=0, column=0, padx=20, pady=0, sticky="nsew", ipady=10)
        self.description_text = customtkinter.CTkLabel(self.home_frame, text="Simple tool for creating user domain account entry on a computer",
                                                  font=customtkinter.CTkFont(size=14))
        self.description_text.grid(row=1, column=0, padx=20, sticky="n")

        #login form
        self.username_entry = customtkinter.CTkEntry(self.home_frame, width=200, placeholder_text="login")
        self.username_entry.grid(row=2, column=0, padx=30, pady=(15, 15), ipady=5)
        
        self.password_entry = customtkinter.CTkEntry(self.home_frame, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=3, column=0, padx=30, pady=(0, 15), ipady=5)
        
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Confirm", command=self.open_toplevel)
        self.home_frame_button_2.grid(row=4, column=0, padx=20, pady=10, ipadx=5, ipady=5)

        # create second frame
        self.help_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        self.banner_text2 = customtkinter.CTkLabel(self.help_frame, text="Frequently asked questions",
                                                  font=customtkinter.CTkFont(size=18, weight="bold"))
        self.banner_text2.grid(row=0, column=0, padx=20, pady=0, sticky="nsew", ipady=10)
        self.description_text2 = customtkinter.CTkLabel(self.help_frame, text="Find answers to commonsly asked questions about this program",
                                                  font=customtkinter.CTkFont(size=14))
        self.description_text2.grid(row=1, column=0, padx=20, sticky="n")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.help_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.help_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
        
            
    def open_toplevel(self):
        
        domain = "mpl.mee.com"
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if self.username_entry.get() != '':
            token = win32security.LogonUser(
            username,
            domain,
            password,
            win32security.LOGON32_LOGON_INTERACTIVE,
            win32security.LOGON32_PROVIDER_DEFAULT)
            
            # if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            #     self.toplevel_window = ModalWindow(self)  # create window if its None or destroyed
            # else:
            #     self.toplevel_window.focus()  # if window exists focus it
            
            if token:
                print("Uwierzytelnianie powiodło się. Użytkownik jest autoryzowany.")
            else:
                print("Uwierzytelnianie nie powiodło się. Użytkownik nie jest autoryzowany.")
        else:
            print('brak danych')

if __name__ == "__main__":
    app = App()
    app.mainloop()
