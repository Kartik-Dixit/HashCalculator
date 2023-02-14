import tkinter
import tkinter.messagebox
import customtkinter
import hashlib
from tkinter import messagebox

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

alg = ""
hash = ""
# text1 = "abcd"
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Hash Calculator")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="HashCalculator", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.algo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Algorithm:", anchor="w")
        self.algo_label.grid(row=1, column=0, padx=20, pady=(10, 0))
        
        self.algo_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["md5", "sha1", "sha224", "sha256", "sha384", "sha512"],
                                                               command=self.change_algo_event)
        self.algo_optionemenu.grid(row=2, column=0, padx=20, pady=(10, 20))
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.main_button_1 = customtkinter.CTkButton(master=self,text="Exit", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.main_button_event)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")


        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        #self.textbox.insert("0.0","Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    
    def change_algo_event(self, new_algo: str):
        alg = new_algo
        text = self.textbox.get('0.0', "end")
        text1 = text.rstrip('\n')
        if(text1 == ""):
            messagebox.showwarning('Warning', 'No message!')
        if(alg == "md5"):
            md5_hash = hashlib.md5(text1.encode())
            hash = md5_hash.hexdigest()
            print(hash)
        elif(alg == "sha1"):
            sha1_hash = hashlib.sha1(text1.encode())
            hash = sha1_hash.hexdigest()
        elif(alg == "sha224"):
            sha224_hash = hashlib.sha224(text1.encode())
            hash = sha224_hash.hexdigest()
        elif(alg == "sha256"):
            sha256_hash = hashlib.sha256(text1.encode())
            hash = sha256_hash.hexdigest()
        elif(alg == "sha384"):
            sha384_hash = hashlib.sha384(text1.encode())
            hash = sha384_hash.hexdigest()
        elif(alg == "sha512"):
            sha512_hash = hashlib.sha512(text1.encode())
            hash = sha512_hash.hexdigest()
        self.textbox1 = customtkinter.CTkTextbox(self, width=250)
        self.textbox1.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox1.insert("0.0",hash)


    def main_button_event(self):
        msg_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?', icon='warning')
        if msg_box == 'yes':
            self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()