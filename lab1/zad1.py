import shutil

src = str(input("Podaj sciezke: "))
dst = "lab1zad.txt"

shutil.copyfile(src, dst)