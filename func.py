def isTheSameLast(first, last):
  first_index = first.find(" ")
  last_index  = last.find(" ")
  
  first_word = first[ 0:first_index]
  last_word = last[last_index:]
  
  first_word == last_word
