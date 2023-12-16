# Must install BeautifulSoup4 package to handle html text

import re 
from urllib.request import urlopen
from bs4 import BeautifulSoup


# Functionality to replace non-readable characters utf-8 encoded, 
# to human readable characters with some variants not covered. 

def text_transformer(e): 
  value = e.group(0)
  first = False
  second = False 
  char_a = ''
  char_b = ''

  if value[0] != '\\': 
    char_a = value[0]
    value = value[1:]
    first = True

  if len(value) != 8: 
    char_b = value[len(value)-1]
    value = value[:-1]
    second = True

  repl = re.sub(r'\\', '', value)
  val = ''
  try: 
    val = dictionary[repl]['char']
    if(first): 
      val = char_a + val
    if (second):
      val = val + char_b
  except KeyError: 
    val = ""

  return val

# Returns a dictionary mapping from utf-8 encoding to human readable characters.
def create_dictionary():
  raw = urlopen('https://www.utf8-chartable.de/unicode-utf8-table.pl?start=128&number=128&names=-&utf8=string-literal')
  content = raw.read().decode(raw.headers.get_content_charset())
  
  bs = BeautifulSoup(str(content), 'html.parser')
  bs_mod = re.split(r'<table class="codetable">', str(bs))

  bs_full = bs_mod[1][3650:]
  bs_cpt = [line[16:22] for line in re.findall(r'<td class="cpt">U+.\w{,4}</td>', bs_full)]
  bs_char = [line[17:18] for line in re.findall(r'<td class="char">.{,1}</td>', bs_full)]
  bs_utf = [re.sub(r'\\', '', line)[17:23] for line in re.findall(r'<td class="utf8">.*</td>', bs_full)][1:]

  dict_obj = {}

  for i in range(len(bs_utf)): 
    dict_obj[bs_utf[i]] = {"char": bs_char[i], "codepoint": bs_cpt[i]}

  return dict_obj

dictionary = create_dictionary()