# VocabularyQuery
If you want to learn vocabularies for any languages you could use this

# How to use?

### Step 1:
Copy the [Python Code](https://raw.githubusercontent.com/DramaLvl1/VocabularyQuery/main/vocalbulary.py) and paste it into your editor (you can use [PyCharm](https://www.jetbrains.com/de-de/pycharm/download/#section=windows) for pc or [extendsclass](https://extendsclass.com/python.html) for all devices
### Step 2: 
Change the maximum of the second line. 

**example**

```py
import random

r = random.randint(1, 4) # increase the second number if you add vocabularies
```
### Step 3: 
Add more vocabularies by adding more elif statement

**example**
```py 
if r == 1:
  vocabulary("cool down (in german)", "abkühlen")
  
elif r == 2:
  vocabulary("shade (in german)", "Schatten")

elif r == 3:
  vocabulary("circle (in german)", "Kreis")

# elif r == 4:
#   vocabulary("forth vocabulary", "answer")
```
But of course without those hashtags. I just wanted to show you how to add vocabularies
