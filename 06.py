# http://pythonchallenge.com/pc/def/channel.html
# Comments in the page use the word zip.  Changing the
# current URL extension to .zip instead of .html lets
# us download a zip file containing many text files of
# the format 1234.txt and also a readme.txt.
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

def print_readme(archive):
  text = archive.read("readme.txt").decode("utf-8")
  print(text)

def linked_list(archive):
  num = "90052"
  while True:
    filename = num + ".txt"
    text = archive.read(filename).decode("utf-8")
    num = next_num(text)
    if not num.isnumeric():
      print(text)
      return text

def zip_comments_inorder(archive):
  num = "90052"
  while True:
    filename = num + ".txt"
    comment = archive.getinfo(filename).comment.decode("utf-8")
    print(comment, end='')
    text = archive.read(filename).decode("utf-8")
    num = next_num(text)
    if not num.isnumeric():
      return

archive = open_zipfile()
print_readme(archive)
linked_list(archive)
zip_comments_inorder(archive)

# Answer is printed in ascii art: hockey