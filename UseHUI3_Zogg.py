#Cheryl Zogg HW2

import HUI3_Zogg as eq #calling in the scoring file

#code testing
print("Score for perfect health: [1,1,1,1,1,1,1,1]")
print(eq.utility(vision=1,hearing=1,speech=1,ambulation=1,dexterity=1,emotion=1,cognition=1,pain=1))

print("Score for arbitrary but plausible: [1,2,3,4,5,4,3,2]") #a state apparently worse than death
print(eq.utility(vision=1,hearing=2,speech=3,ambulation=4,dexterity=5,emotion=4,cognition=3,pain=2))
print((1.371*1.00*0.95*0.89*0.73*0.65*0.64*0.95*0.96)-0.371) #'hand' checked comparison

#print("Score for this should not work: [1,1,6,1,1,1,1,1]") #ValueError: Speech level must be 1-5
#print(eq.utility(vision=1,hearing=1,speech=6,ambulation=1,dexterity=1,emotion=1,cognition=1,pain=1))

#print("Score for this should not work: [1,1,1,1,1,1,1,6]") #ValueError: Pain level must be 1-5
#print(eq.utility(vision=1,hearing=1,speech=1,ambulation=1,dexterity=1,emotion=1,cognition=1,pain=6))

#print("Score for this should not work: [1,1,1,1,1,1,7,1]") #ValueError: Cognition level must be 1-6
#print(eq.utility(vision=1,hearing=1,speech=1,ambulation=1,dexterity=1,emotion=1,cognition=7,pain=1))