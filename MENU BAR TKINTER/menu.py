# creating menu bar:
# ====================


import tkinter as tk       
from tkinter import ttk 
from tkinter import filedialog 
from tkinter.filedialog import asksaveasfile
win = tk.Tk() 
win.title('MENU_BAR')


def func():
    print('func called')
def openfile():
    return filedialog.askopenfilename()
def save():
    files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = files)
  

# Menu --> this Menu class present in tkinter
# **************************SIMPLE MENUBAR*****************************
# menubar = tk.Menu(win)
# menubar.add_command(label='Save', command=func)
# menubar.add_command(label='Save As', command=func)
# menubar.add_command(label='Copy', command=func)
# menubar.add_command(label='Paste', command=func)

main_menu = tk.Menu(win)
# file menu
file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label='New File', command=openfile)

file_menu.add_command(label='New Window', command=func)
file_menu.add_command(label='Open', command=func)
file_menu.add_command(label='Save', command=func)
file_menu.add_command(label='Save As', command=lambda:save())
file_menu.add_separator()
file_menu.add_command(label='Page Setup', command=func)
file_menu.add_command(label='Print', command=func)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=func)
# edit menu
edit_menu = tk.Menu(main_menu, tearoff=0)
edit_menu.add_command(label='Undo', command=func)
edit_menu.add_separator()
edit_menu.add_command(label='Cut', command=func)
edit_menu.add_command(label='Copy', command=func)
edit_menu.add_command(label='Paste', command=func)
edit_menu.add_command(label='Delete', command=func)
edit_menu.add_separator()
edit_menu.add_command(label='Find', command=func)
edit_menu.add_command(label='Find Next', command=func)
edit_menu.add_command(label='Find Previous', command=func)
edit_menu.add_command(label='Replace', command=func)
edit_menu.add_command(label='Go To', command=func)
edit_menu.add_separator()
edit_menu.add_command(label='Select All', command=func)
edit_menu.add_command(label='Time/Date', command=func)
edit_menu.add_separator()
edit_menu.add_command(label='Font', command=func)
#view menu
view_menu = tk.Menu(main_menu, tearoff=0)
edit_menu.add_command(label='Zoom', command=func)
edit_menu.add_command(label='Status', command=func)
edit_menu.add_command(label='Word Wrap', command=func)

main_menu.add_cascade(label='File',menu=file_menu)
main_menu.add_cascade(label='Edit',menu=edit_menu)
main_menu.add_cascade(label='View',menu=view_menu)


win.config(menu=main_menu)

win.mainloop()