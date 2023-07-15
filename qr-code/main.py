import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

class App(ctk.CTk):
  def __init__(self):
    #window setup
    ctk.set_appearance_mode('light')
    super().__init__(fg_color = 'white')

    self.title('')
    self.iconbitmap('empty.ico')
    self.geometry('400x400')

    #Entry field
    EntryField(self)

    self.mainloop()

class EntryField(ctk.CTkFrame):
  def __init__(self, parent):
    super().__init__(master = parent, corner_radius = 20, fg_color = '#021FB3')
    self.place(relx = 0.5, rely = 1, relwidth = 1, relheight = 0.4, anchor = 'center')

    self.rowconfigure((0,1), weight = 1, uniform = 'a')
    self.columnconfigure(0, weight = 1, uniform = 'a')



App()
