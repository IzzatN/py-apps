import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

class App(ctk.CTk):
  def __init__(self):
    #window setup
    ctk.set_appearance_mode('light')
    super().__init__(fg_color = 'white')

    #customize
    self.title('')
    self.iconbitmap('empty.ico')
    self.geometry('400x400')

    #run app
    self.mainloop()

App()
