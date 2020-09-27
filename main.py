import sys
import os
import shutil
from tpp import parse
from tkinter import messagebox, filedialog

if sys.version_info[0] == 2:
    from Tkinter import *
else:
    from tkinter import *
from TkinterDnD2 import *

count = 0
start = 0
digit = 3
dir = ''

def reset_counter():
    global count, start, digit
    count = int(start_string.get())
    start = int(start_string.get())
    digit = int(digit_string.get())
    reset_button.config(text='Count: %d' % count)

def select_folder():
    global dir
    dir = filedialog.askdirectory()
    if dir == '':
        return
    folder_button.config(text='OK')

def drop(event):
    global count
    
    if dir == '':
        messagebox.showerror("Error", "No output directory selected")
        return
    
    filelist = parse(event.data)
    for file in filelist:
        s_ind = file.rfind('/') + 1
        e_ind = file.rfind('.')
        file_name = file[s_ind:e_ind]
        file_ext = file[e_ind:]
        new_path = dir + '/%03d' % count + file_ext
        
        try:
            if os.path.isfile(new_path):
                warning_string = '(From file %s)\nThe destination file "%s" already exists.\nOverwrite the file?' % (file_name + file_ext, ('%0*d' % (digit, count)) + file_ext)
                ans = messagebox.askyesno("Info", warning_string)
                if ans == False:
                    return
            shutil.copy2(file, new_path)
        except:
            messagebox.showerror("Error", "Copy to destination folder error")
        count += 1
        reset_button.config(text='Count: %d' % count)

root = TkinterDnD.Tk()
root.geometry('210x170')
root.resizable(0,0) # disable maximize button
root.title('File Numbering Utility v1.0')
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)


config_frame = Frame(root)
config_frame.grid(row=1, column=0)

folder_label = Label(config_frame, text='Dest. folder:')
folder_label.grid(row=0, column=0)
folder_button = Button(config_frame, text='Select', command=select_folder, width=5)
folder_button.grid(row=0, column=1, padx=5, pady=1)

start_string = StringVar()
start_string.set('%d' % start)
start_label = Label(config_frame, text='Start num:')
start_entry = Entry(config_frame, textvariable=start_string, width=4)
start_label.grid(row=1, column=0, sticky='e')
start_entry.grid(row=1, column=1, padx=3, pady=5)

digit_string = StringVar()
digit_string.set('%d' % digit)
digit_label = Label(config_frame, text='Digits:')
digit_entry = Entry(config_frame, textvariable=digit_string, width=4)
digit_label.grid(row=2, column=0, sticky='e')
digit_entry.grid(row=2, column=1, padx=3, pady=5)

reset_button = Button(root, text='Drop files here\n(click to reset)', command=reset_counter, width=15, height=3)
reset_button.grid(row=2, column=0, columnspan=1, padx=10, pady=10)

root.mainloop()