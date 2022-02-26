# http://www.pythonchallenge.com/pc/def/linkedlist.php

from urllib.request import urlopen

def get_page_body(url):
  page = urlopen(url)
  binary_data = page.read()
  string_data = binary_data.decode("utf-8")
  return string_data

def make_url(num):
  return "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(num)


new_num = 12345
keep_going = True
counter = 0
while keep_going:
  counter += 1
  url = make_url(new_num)
  body = get_page_body(url)
  print("Count: ", counter, ": ", body)
  if 'and the next nothing is' in body:
    new_num = body.split()[-1]
  elif 'Yes. Divide by two and keep going.' in body:
    new_num = str(int(int(new_num) / 2))
  else:
    keep_going = False
  
