import tkinter as tk
import files 
def contact():
    print(files.read("docs/contact.txt"))
def docmain():
    print(files.read("docs/doc1.txt"))
def docex():
    print(files.read("docs/doc2.txt"))

def mainnoin(fn, fn2):
    print(fn)
    with open(fn, "r", encoding="utf-8") as file:
        ksfile = file.read()
    replacements = {
        ">": "age:            ",
        "~": "name:           ",
        "#": "phone:          ",
        "&": "family:         ",
        "^": "associates:     ",
        "_@": "emails:         ",
        "!": "address:        ",
        "*": "state/province: ",
        "$": "city/town:      ",
        "-": "apt/suite:      ",
        r"//": "comments:       ",
        "`": "file/image:     ",
        ";": "ip address:     ",
        "_tt": "tiktok          ",
        "_yt": "youtube         ",
        "_sc": "snapchat        ",
        "_dc": "discord         ",
        "_ds": "discord server  ",
        "_ex": "extra social    ",
        r"\\": "end comment     ",
        ",": ", ",
        "?": "unknown "
    }
    for old, new in replacements.items():
        ksfile = ksfile.replace(old, new)
    files.write(fn2,ksfile)

def exnoin(fn, fn2):
    with open(fn, "r", encoding="utf-8") as file:
        ksfile = file.read()
    replacements = {
        "_ag": "age:            ",
        "_n": "name:           ",
        "_p": "phone:          ",
        "_f": "family:         ",
        "_w": "work:           ",
        "_e": "emails:         ",
        "_ad": "address:        ",
        "_sp": "state/province: ",
        "_ct": "city/town:      ",
        "_as": "apt/suite:      ",
        "//": "comments:       ",
        "_h": "file/image:     ",
        "_ip": "ip address:     ",
        "_tt": "tiktok          ",
        "_yt": "youtube         ",
        "_sc": "snapchat        ",
        "_dc": "discord         ",
        "_ds": "discord server  ",
        "_ex": "extra social    ",
        r"\\": "end comment     ",
        ",": ", ",
        "?": "unknown "
    }
    for old, new in replacements.items():
        ksfile = ksfile.replace(old, new)
    
    
    files.write(fn2, ksfile)
def cmdline():
    while True:
        function_name = input("Ksl.py@User:~$ ")
        if function_name == "exit":
            print("Exiting...")
            break
        else:
            exec(function_name)
def kslselector():
    MAIN_MENU = """
1. Contact Info
2. View Docs 
3. Run Interpreter
4. Command Line
q. Quit
"""
    DOC_MENU = """
1. Main Docs
2. Extra Docs
3. Import my GPG key
q. Go Back
"""
    INTERPRETER_MENU = """
1. Main Interpreter
2. Extra Interpreter
n. Open Notepad
m. Read Notes
q. Go Back
"""
    
    option = ""
    while option != "q":
        print(MAIN_MENU)
        option = input("Select an option: ").lower()
        
        if option == "1":
            print("Contact info selected")
            contact()
            
        elif option == "2":
            suboption = ""
            while suboption != "q":
                print(DOC_MENU)
                suboption = input("Select a suboption: ").lower()
                
                if suboption == "1":
                    print("Main docs selected")
                    docmain()
                elif suboption == "2":
                    print("Extra docs selected")
                    docex()
                elif suboption == "3":
                    import os
                    print("Importing GPG key")
                    os.system("gpg --import docs/gpgkey.txt")
                elif suboption == "q":
                    print("Going back to main menu")
                else:
                    print("Invalid suboption")
                    
        elif option == "3":
            suboption = ""
            while suboption != "q":
                print(INTERPRETER_MENU)
                suboption = input("Select a suboption: ").lower()
                
                if suboption == "1":
                    print("Main interpreter selected")
                    fn = input("Enter the file name to read: ")
                    fn2 = input("Enter the file name to write to: ")
                    mainnoin(fn, fn2)
                elif suboption == "2":
                    print("Extra interpreter selected")
                    fn = input("Enter the file name to read: ")
                    fn2 = input("Enter the file name to write to: ")
                    exnoin(fn, fn2)
                elif suboption == "n":
                    files.notepad()
                elif suboption == "m":
                    files.nread()
                elif suboption == "q":
                    print("Going back to main menu")
                else:
                    print("Invalid suboption")
                    
        elif option == "4":
            cmdline()
            
        elif option == "q":
            print("Exiting the program")
            
        else:
            print("Invalid option")