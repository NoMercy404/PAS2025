import re

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"


def check(Ip):
    # pass the regular expression
    # and the string in search() method
    if (re.search(regex, Ip)):
        print("Prawidlowy Ip address")

    else:
        print("Nieprawidlowy Ip address")

IP = str(input("Podaj IP: "))

check(IP)