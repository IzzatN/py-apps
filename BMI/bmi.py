import customtkinter as ctk
from settings import *

try:
  from ctypes import windll, byref, sizeof, c_int
except:
  pass

class App(ctk.CTk):
  def __init__(self):
    super().__init__(fg_color = GREEN)
    self.title('')
    self.iconbitmap('empty.ico')
    self.geometry('400x400')
    self.resizable(False, False)
    self.change_title_bar_color() # works only on Windows

    self.columnconfigure(0, weight = 1)
    self.rowconfigure((0,1,2,3), weight = 1, uniform = 'a')

    ResultText(self)

    self.mainloop()

  def change_title_bar_color(self):
    try:
      HWND = windll.user32.GetParent(self.winfo_id())
      DWMWA_ATTRIBUTE = 35
      COLOR = TITLE_HEX_COLOR
      windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
    except:
      pass

class ResultText(ctk.CTkLabel):
  def __init__(self, parent):
    font = ctk.CTkFont(family = FONT, size = MAIN_TEXT_SIZE, weight = 'bold')
    super().__init__(master = parent, text = 22.5, font = font, text_color = WHITE)
    self.grid(column = 0, row = 0, rowspan = 2, sticky = 'nsew')

if __name__ == '__main__':
  App()
