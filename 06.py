# http://pythonchallenge.com/pc/def/channel.html
# Change the URL to have an extension of zip and download
# and unzip that file.  The contents are in the 06 directory.
import zipfile
import requests
import io

def next_num(text):
  return text.split()[-1]

def open_zipfile():
  url = "http://www.pythonchallenge.com/pc/def/channel.zip"
  r = requests.get(url)
  bytes = io.BytesIO(r.content)
  return zipfile.ZipFile(bytes)

def linked_list():
  archive = open_zipfile()
  num = "90052"
  while True:
    filename = num + ".txt"
    text = archive.read(filename).decode("utf-8")
    num = next_num(text)
    if not num.isnumeric():
      print(text)
      return text

def zip_comments_inorder():
  archive = open_zipfile()
  num = "90052"
  while True:
    filename = num + ".txt"
    comment = archive.getinfo(filename).comment.decode("utf-8")
    print(comment, end='')
    text = archive.read(filename).decode("utf-8")
    num = next_num(text)
    if not num.isnumeric():
      return

linked_list()
zip_comments_inorder()

# Answer is printed in ascii art: hockey