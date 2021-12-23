from zipfile import ZipFile

if __name__ == '__main__':
    file_pw = open("path(dictionary)","r", errors="ignore")  # rockyou.txt
    zip_file = "path(zip-file)" #geschenk.zip

    pw_list = []
    for line in file_pw:
        if len(line.rstrip()) == 96 and len(str(line.rstrip().encode())) == 96 + 3:
            print(line.rstrip())
            pw_list.append(line.rstrip())

    for pw in pw_list:
        with ZipFile(zip_file) as zf:
            try:
                zf.extractall(pwd=pw.encode())
                print("\nPW:\n" + pw)
                break
            except RuntimeError:
                pass