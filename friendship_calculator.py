#funny friendship calculator
alphabet="bcghjklmpqrtvxxyz"
score=0
names=input("enter first name and give space and then enter 2nd name.:")
for character in names:
    if character in "aeiou":
        score+=5
    elif character in "friends":
        score+=10
    elif character in alphabet:
        score+=alphabet.find(character)
    else:
        score+=0
if score >100:
    print("your friendship score is: ",score)
    print("congratulatons! , you both are good friends. ")
else:
    print("your friendship score is: ",score)
