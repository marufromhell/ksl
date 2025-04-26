
def readfile(filename):
    with open(filename, "r", encoding="utf-8") as file:
        contents = file.read()
    return contents
def writefile(fnw, data):
    fw = open(fnw, "w", encoding="utf-8")
    fw.write(data)
    print(fw)
def amendfile(fnw, data):
    with open(fnw, "r", encoding="utf-8") as read:
        existing_data = read.read()  # Read the existing content of the file
    with open(fnw, "w", encoding="utf-8") as write:
        write.write(existing_data + data)  # Append the new data to the existing content
    print(f"Data appended to {fnw}")
def nreadfile():
    fnr = input("Filename to read(utf-8): ")
    with open(fnr, "r", encoding="utf-8") as file:
        fr = file.read()
    print(fr)
    input()
def nwritefile():
    fw = input("Filename to write to(utf-8): ")
    print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
    fr2 = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        fr2.append(line)
    with open(fw, "w") as outfile:
        outfile.write("\n".join(fr2))
    print(fr2)
def notepad():
    s1 = input("would you like to r/w?: ")
    if s1 == "r":
        nreadfile()
    elif s1 == "w":
        nwritefile()