import hashlib
import os
import wget
from zipfile import ZipFile

def update():
    url = "https://bazaar.abuse.ch/export/txt/sha256/full/"
    output = "..\\antivirus\\update\\full.zip"
    try:
        os.remove(output)
        os.remove('..\\antivirus\\update\\full_sha256.txt')
    except FileNotFoundError:
        print("Adding the deleted file")
    file_name = wget.download(url, out=output)
    print('')
    with ZipFile(output, 'r') as zip:
        zip.extractall("..\\antivirus\\update")


def hash_sha256(file):
    try:
        hr = hashlib.sha256()
        with open(file, 'rb') as data:
            # here d will give the data of a given size in this case it is 5mb or 5120 in the form of byte
            for d in iter(lambda: data.read(5120), b""):
                hr.update(d)
                return (hr.hexdigest())
    except:
        pass


def search(drive):
    l1 = []
    d = {}
    with open('..\\antivirus\\update\\full_sha256.txt') as f:
        for i in f:
            d[i.strip()] = "Virus"
    try:
        for i in drive:
            print("Scanning")
            for root, folder, files in os.walk(i):
                for file in files:
                    path = root+'\\'+file
                    hash = hash_sha256(path)
                    if d.get(hash, "Not Found") == "Virus":
                        l1.append((file, path))
        print("Done Scanning")
        return l1
    except:
        pass

