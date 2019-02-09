import re
import csv


def emails(string):
    matches = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', string)
    if matches:
        return matches
    else:
        return False

def emailnames(mail):
    enames = re.findall(r'[a-zA-Z0-9_.+-]+@', mail)

    if enames:
        for i in enames:
            i = i[:-1]
           ## print(i)
            return i
    else:
        return False

def domins(org):
    dominName = re.findall(r'@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', org)

    if dominName:
        for i in dominName:
            i = i[1:]
            return i

    else:
        return False

def asterisks(aster):
    atches = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', aster)
    if atches:
        for i in atches:
            i = re.sub(r'\S', '*', i, 6)
        return i
    else:
        return False





### change leads txt to your leads txt file name
openleads = open("leads.txt", "r+")


openedleads = openleads.read()
finalopen = emails(openedleads)


with open('email_file.csv', mode='w') as email_file:
        email_writer = csv.writer(email_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in finalopen:
            email_writer.writerow([str(emailnames(i)), i, str(domins(i)), str(asterisks(i))])
