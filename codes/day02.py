#day01_name_analyzer.py
#Function 1: get_word_count(text)     → returns number of words

def get_word_count(str_in):
  return len(str_in.split(' '))


#Function 2: get_char_count(text)     → returns number of characters (no spaces)

def get_char_count(str_in):
  return len(str_in.replace(" ",""))

#Function 3: get_uppercase(str_in)      → returns text in uppercase
def make_upper(str_in):
  return str_in.upper()

#Function 4: analyse_text(text)       → calls all 3 above and returns combined result
def analyse_text(str_in):
  words = get_word_count(str_in)
  chars = get_char_count(str_in)
  case_up = make_upper(str_in)
  return f"total word count is {words} and char count is {chars}. so all the things are upper case {case_up}"

print(analyse_text("Hello World"))
