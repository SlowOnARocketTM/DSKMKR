import os
import tkinter
import customtkinter
import shutil

main = customtkinter.CTk()
main.geometry("600x500")
main.title("DSKMKR")
icon = tkinter.PhotoImage(file="DSKMKR.png")  # Make sure this is 48x48 or smaller
main.iconphoto(True, icon)
customtkinter.set_default_color_theme("white.json")
main.resizable(False, False)

# Version
TVersion = customtkinter.CTkLabel(main, text="Set The Version Of the Software(leave 1.0.0 if unsure)")
TVersion.pack(pady = 5)
Version = tkinter.StringVar()
CVersion = customtkinter.CTkEntry(main, width=550, height=40, corner_radius=15, textvariable=Version)
CVersion.pack(pady = 20)
# Executable
TExeclocation = customtkinter.CTkLabel(main, text="Set the location of the .Appimage")
TExeclocation.pack(pady = 5)
Execlocation = tkinter.StringVar()
CExeclocation = customtkinter.CTkEntry(main, width=550, height=40, corner_radius=15, textvariable=Execlocation)
CExeclocation.pack(pady = 10)
# App Name
TName = customtkinter.CTkLabel(main, text="Set the name of the software")
TName.pack(pady = 5)
Name = tkinter.StringVar()
CName = customtkinter.CTkEntry(main, width=550, height=40, corner_radius=15, textvariable=Name)
CName.pack(pady = 10)
# Icon
TIcon = customtkinter.CTkLabel(main, text="Set the location of the apps icon file")
TIcon.pack(pady = 5)
Icon = tkinter.StringVar()
CIcon = customtkinter.CTkEntry(main, width=550, height=40, corner_radius=15, textvariable=Icon)
CIcon.pack(pady = 10)
# Create and move the file
def MKDSK() :
    print("The version that was set is", Version.get())
    print("The executable location that was set is", Execlocation.get())
    print("The Name Of The Software is ", Name.get())
    print("The icon's location that was set is", Icon.get())

    file = open(f"{Name.get()}.desktop", "w")
    file.write(f"""
[Desktop Entry]
Encoding=UTF-8
Version={Version.get()}
Type=Application
Terminal=false
Exec={Execlocation.get()}
Name={Name.get()}
Icon={Icon.get()}
    """)
    # Move The File
    src_path= f"{Name.get()}.desktop"
    dst_path = os.path.expanduser(f"~/.local/share/applications/{src_path}")
    shutil.move(src_path, dst_path)
    print(".desktop file was created and moved succesfully")    # toast thingy
    confirmv.configure(state="disabled")
    toast = customtkinter.CTkToplevel(main)
    toast.geometry("500x100+100+100")  
    toast.overrideredirect(True)  
    customtkinter.CTkLabel(toast, text=".desktop file was created and moved succesfully").pack(expand=True)
    toast.after(5000, toast.destroy)  # auto-close in 1.5 sec

# Confirm button
confirmv = customtkinter.CTkButton(main, text="Create .desktop file", command=MKDSK)
confirmv.pack(pady = 10)
# TK loop
main.mainloop()
