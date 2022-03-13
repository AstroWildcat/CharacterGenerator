#Elena Flood
#Museumverse Original Character Generator
#Trust me, this took me WAY longer to figure out than I would have liked.
#I spent two weeks working on this program instead of actually focusing on my schoolwork.

import random
import names
import pycountry
import pyhobbies
import pyoccupation
import pymentalhealth
import scgraphics
from datetime import date
random.seed()

#This code generates the character's gender variable, which is used to generate the pronouns.
global gender
gender = (random.choice(['male','female']))

#This generates the character's name and stores it for later use.
def getFirstname():
    return (names.get_first_name(gender))
firstName = getFirstname()
def getLastname():
    return (names.get_last_name())
lastName = getLastname()

#This generates the character's pronouns that will be used throughout the paragraph.
if gender == 'male':
      uc="He"
      lc="he"
      pp="his"
      Pp="His"
if gender == 'female':
      uc="She"
      lc="she"
      pp="her"
      Pp="Her"

#This contains their sex, race, and sexuality.
sex = (random.choice(['cis']*2 + ['intersex']*1 + ['trans']*2))
race = (random.choice(['white']*2 + ['black']*2 + ['Asian'] + ['Indigenous'] + ['biracial']*2 + ['mixed-race']*3))
attract = (random.choice(['straight'] + ['gay']*2 + ['bisexual']*2 + ['pansexual']*2 + ['asexual']))

#This calculates the country they are from. This does not neccesarily indicate their birth country.
def origin():
    place=(random.choice(list(pycountry.countries)))
    return place.name
country = origin()

#This calculates the character's ethnicity.
def heritage():
    place=(random.choice(list(pycountry.countries)))
    return place.demonym
ethnicity = heritage()

#This calculates the year of birth, which will factor into their birthday and age.
yob = int(random.randrange(1938,2006))

#This calculates their birthday.
def birthday(yob):
    day = int(random.randrange(1,31))
    month = random.choice(['January','February','March','April','May','June','July','August','September','October','November','December'])
    if month == 'February':
        day != 30,31
    if day == 31:
        month == (random.choice(['January','March','May','July','August','October','December']))
    return str(month)+" "+str(day)+","+" "+str(yob)
birthday = birthday(yob)

#This calculates their age.
def age(yob):
    now = date.today()
    return int(now.year)-int(yob)
age = age(yob)

#This calculates the amount of siblings they have.
sib = (random.randrange(0,5,))
if sib == 1:
    num = 'sibling'
else:
    num = 'siblings'
    
##This generates names for the siblings, if there are any.
def siblings():
    sibName = str(names.get_first_name())
    if sib == 2:
        sibName = str(names.get_first_name())+" and "+str(names.get_first_name())
    if sib == 3:
        sibName = str(names.get_first_name())+", "+str(names.get_first_name())+", and "+str(names.get_first_name())
    if sib == 4:
        sibName = str(names.get_first_name())+", "+str(names.get_first_name())+", "+str(names.get_first_name())+", and "+str(names.get_first_name())
    return str(sibName)
siblingNames = siblings()

#This determines how many children they have.
child = random.randrange(0,4)
if (attract == 'asexual' or attract == 'gay') or (age == range(16,17)):
    child = random.randrange(0,2)
elif age <= 15:
    child = 0
if child == 1:
    num2 = 'child'
    num3 = 'is'
else:
    num2 = 'children'
    num3 = 'are'
    
##This generates names for the children, if there are any.
def children():
    childName = str(names.get_first_name())
    if child == 2:
        childName = (str(names.get_first_name())+" and "+str(names.get_first_name()))
    if child == 3:
        childName = str(names.get_first_name())+", "+str(names.get_first_name())+", and "+str(names.get_first_name())
    if child == 4:
        childName = str(names.get_first_name())+", "+str(names.get_first_name())+", "+str(names.get_first_name())+", and "+str(names.get_first_name())
    return str(childName)
childNames = children()

#This choses a job.
job = random.choice(list(pyoccupation.job))

#This choses a multitude of hobbies.
def hobbies ():
    times = random.randrange(1,3)
    if times == 1:
        num2 = 'hobby is'
        load = str(random.choice(list(pyhobbies.hobbies)))
    if times == 2:
        num2 = 'hobbies are'
        load = str(random.choice(list(pyhobbies.hobbies))+" and "+random.choice(list(pyhobbies.hobbies)))
    if times == 3:
        num2 = 'hobbies are'
        load = str(random.choice(list(pyhobbies.hobbies))+", "+random.choice(list(pyhobbies.hobbies))+", and "+random.choice(list(pyhobbies.hobbies)))
    return str(num2+" "+load)
hobby = hobbies()

#This part contains how many mental health conditions they have.
mental = random.randrange(0,5)
if mental == 1:
    num4 = 'mental health condition, which is'
else:
    num4 = 'mental health conditions, which are'

#This part generates the names of the mental conditions.
def mentalhealth ():
    MHName = str(random.choice(list(pymentalhealth.mental_health)))
    if mental == 2:
        MHName = str(random.choice(list(pymentalhealth.mental_health)))+" and "+str(random.choice(list(pymentalhealth.mental_health)))
    if mental == 3:
        MHName = str(random.choice(list(pymentalhealth.mental_health)))+", "+str(random.choice(list(pymentalhealth.mental_health)))+", and "+str(random.choice(list(pymentalhealth.mental_health)))
    if mental == 4:
        MHName = str(random.choice(list(pymentalhealth.mental_health)))+", "+str(random.choice(list(pymentalhealth.mental_health)))+", "+str(random.choice(list(pymentalhealth.mental_health)))+", and "+str(random.choice(list(pymentalhealth.mental_health)))
    if mental == 5:
        MHName = str(random.choice(list(pymentalhealth.mental_health)))+", "+str(random.choice(list(pymentalhealth.mental_health)))+", "+str(random.choice(list(pymentalhealth.mental_health)))+", "+str(random.choice(list(pymentalhealth.mental_health)))+", and "+str(random.choice(list(pymentalhealth.mental_health)))
    return str(MHName)
mentalList = mentalhealth()


#This stores the strings in the paragraph that contains their information.
line1 = ("Your character's name is"+" "+firstName+" "+lastName+".")
line2 = (firstName+" is a "+sex+" "+gender+" who is "+attract+". "+uc+" is a "+race+" "+ethnicity+" who lives in "+country+".")
line3 = (uc+" is "+str(age)+", and was born in "+birthday+".")
line4 = (firstName+" is a "+job+", and "+pp+" main "+hobby+".")
line5 = (uc+" grew up with "+str(sib)+" "+num+", named "+siblingNames+'.')
line6 = (uc+" has "+str(child)+" "+num2+", who "+num3+" named "+childNames+".")
line7 = (uc+" has "+str(mental)+" "+num4+" "+mentalList+".")

#This makes a window that displays the information.    
##create the graphics window (w x h)
win = scgraphics.GraphicsWindow(1000, 500)
##get a reference to the canvas
canvas = win.canvas()
##This displays the text in the window.
if sib == 0:
    line5 = ("")
else:
    pass
if child == 0:
    line6 = ("")  
else:
    pass
if mental == 0:
    line7 = ("")  
else:
    pass
canvas.drawText(25,25,str(line1))
canvas.drawText(25,50,str(line2))
canvas.drawText(25,75,str(line3))
canvas.drawText(25,100,str(line4))
canvas.drawText(25,125,str(line5))
canvas.drawText(25,150,str(line6))
canvas.drawText(25,175,str(line7))

#This prints out the text into the python shell so it can be copied and pasted.
print(line1)
print(line2)
print(line3)
print(line4)
if sib == 0:
    pass
else:
    print(line5)
if child == 0:
    pass  
else:
    print(line6)
if mental == 0:
    pass 
else:
    print(line7)

#wait for user to close the window
win.wait()
