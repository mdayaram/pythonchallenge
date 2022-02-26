# http://www.pythonchallenge.com/pc/def/map.html
# K => M
# O => Q
# E => G
# They all shift by two.

def shift_by_two(encrypted):
  shifted = ""
  for c in encrypted:
    if c.isalpha():
      shifted_c = (ord(c) - ord("a") + 2) % 26 + ord("a")
      shifted += chr(shifted_c)
    else:
      shifted += c
  return shifted


text_on_page = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = "map"

decrypted_text_on_page = shift_by_two(text_on_page)
print(decrypted_text_on_page)
decrypted_url = "http://pythonchallenge.com/pc/def/" + shift_by_two(url) + ".html"
print("Decrypted URL: ", decrypted_url)