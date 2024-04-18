import customtkinter
import os
from PIL import Image
 
customtkinter.set_default_color_theme
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_default_color_theme("green")
        self.title("COOKIES LOADER")
        self.geometry("610x300")
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.iconbitmap("test_images/logo_app.ico")
        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo_app.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo_possible.png")), size=(388, 46))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "information_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "information_light.png")), size=(20, 20))
         
 
        self.netflix_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "netflix.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "netflix.png")), size=(20, 20))
        self.envato_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "envato.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "envato.png")), size=(20, 20))
        self.freepik_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "freepik.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "freepik.png")), size=(20, 20))
        self.service_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "service.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "service.png")), size=(20, 20))
 
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)
 
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  C. L.", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)
 
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="INICIO",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")
 
        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="service",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.service_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")
 
        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Sobre el programa",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")
 
 
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Dark", "Light", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")
 
        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
 
        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
        ### INSERTAR BOTONES A LA NAVEGACION
 
        self.netflix = customtkinter.CTkButton(self.home_frame, text="Abrir Netflix", image=self.netflix_image, compound="left", command=self.opennetflix)
        self.netflix.grid(row=1, column=0, padx=20, pady=10)
        self.envato = customtkinter.CTkButton(self.home_frame, text="Abrir Envato", image=self.envato_image, compound="left", command=self.openenvato)
        self.envato.grid(row=2, column=0, padx=20, pady=10)
        self.freepik = customtkinter.CTkButton(self.home_frame, text="Abrir Freepik", image=self.freepik_image, compound="left", command=self.openfreepik)
        self.freepik.grid(row=3, column=0, padx=20, pady=10)
 
        # create second frame
 
        # Frame contenedor
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
 
        # TÃ­tulo o encabezado
        self.credents_text = "INFORMACIÃ“N DE LA CUENTA"
        self.label_text = customtkinter.CTkLabel(self.second_frame, text=self.credents_text, anchor="center")
        self.label_text.grid(row=0, column=2, sticky="w", padx=1, pady = 10 )
 
        # Label y Entry para Email
        self.label_email = customtkinter.CTkLabel(self.second_frame, text="Email:", image=self.service_image, compound="left")
        self.label_email.grid(row=1, column=1, padx=10, pady=10, sticky="e")
 
 
        self.entry_email = customtkinter.CTkEntry(self.second_frame, width=200)
        self.entry_email.grid(row=1, column=2, padx=10, pady=10)
        self.entry_email.insert(0, "mail-admin@gmail.com")
 
        # Label y Entry para ContraseÃ±a
        self.label_password = customtkinter.CTkLabel(self.second_frame, text="ContraseÃ±a:", image=self.service_image, compound="left")
        self.label_password.grid(row=2, column=1, padx=10, pady=10, sticky="e")
 
 
        self.entry_password = customtkinter.CTkEntry(self.second_frame, width=200)
        self.entry_password.grid(row=2, column=2, padx=10, pady=10)
        self.entry_password.insert(0, "123456789")
 
         
 
 
        # create third frame
 
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
 
        self.aboutprogram  = """Respecto al funcionamiento de las cuentas:
Es esencial no cambiar ningÃºn detalle o informaciÃ³n de las cuentas.
Si lo hacemos, la cuenta se perderÃ¡ para ambos, tÃº y yo.
La instalaciÃ³n del Firefox portable para que todo arranque correctamente,
funciona descargandose desde una nube de google drive
(LINK DEL DRIVE para que lo revise: Link)
(Descargado de https://portableapps.com/apps/internet/firefox_portable).
Totalmente limpio, no se preocupe, y disfrutÃ© de sus servicios."""
        self.label3 = customtkinter.CTkLabel(self.third_frame, text=self.aboutprogram,justify="left")
        self.label3.grid(row=2, column=1, padx=10, pady=10)
        # select default frame
        self.select_frame_by_name("home")
 
        self.update()  # Actualiza la ventana para obtener las dimensiones actuales
        self.center_window()  # Centra la ventana
 
 
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
 
        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
 
 
 
 
    def opennetflix(self):
        print("Abriendo netflix...")
    def openenvato(self):
        print("Abriendo envato...")
    def openfreepik(self):
        print("Abriendo freepik...")
 
    def home_button_event(self):
        self.select_frame_by_name("home")
 
    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")
 
    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")
 
    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
 
 
 
    def center_window(self, width=None, height=None):
        # Obtiene las dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
 
        # Si no se especifica el ancho y el alto, obtiene las dimensiones actuales de la ventana
        if not width:
            width = self.winfo_width()
        if not height:
            height = self.winfo_height()
 
        # Calcula las coordenadas x e y para centrar la ventana
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
 
        self.geometry(f'{int(width)}x{int(height)}+{int(x)}+{int(y)}')
 
 
 
 
if __name__ == "__main__":
    app = App()
    app.mainloop()