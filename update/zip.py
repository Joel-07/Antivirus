from zipfile import ZipFile
import wget

url = "https://bazaar.abuse.ch/export/txt/sha256/full/"
output = "..\\antivirus\\update\\full.zip"
with ZipFile('..\\antivirus\\update\\full.zip', 'r') as zip:
    zip.extractall("..\\antivirus\\update")
