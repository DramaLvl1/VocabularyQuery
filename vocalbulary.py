import random

r = random.randint(1, 3)

def vocabulary(question, answer):
  i = input(question)
  if i == answer:
    print("correct!\n\nyour input: " + i)
  else:
    print("incorrect!\n\nYour input: " + i + "\n\The correct answer: " + answer)
  
########## examples ##########

# check if random numbers are 1, 2 or 3
if r == 1:
  vocabulary("cool down (in german)", "abkühlen")
  
elif r == 2:
  vocabulary("shade (in german)", "Schatten")

elif r == 3:
  vocabulary("circle (in german)", "Kreis")

# and if you want you can add more vocabularies
# but then you should change the maximum at the r variable at the second line
# for anyone who dont know: random.randint(minimum, maximum)
