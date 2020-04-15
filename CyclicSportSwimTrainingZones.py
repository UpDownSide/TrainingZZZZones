
# This script serves to cyclic sport, it aims the limits of energy production,
# limits could be trained. Use a professional of this area when training, be carefull... 
# You can always try your best!!!! Hoping to help!


name = input ("What's your name? ")
distance = input ("What's your swim distance (in meters)? ")
b = int (distance)
time = input ("How long did you take to swim it at full speed (in seconds)?")
c = int (time)
d = b/c
print(d, 'm/s', 'is your full speed') 

#Speed training zones, speed for each metabolic zone
RecA0 = d*0.5
print (RecA0, 'm/s','is for recovering purposes')
FatA1 = d*0.6
print (FatA1, 'm/s','is for burning fat')
GlycogenA2 = d*0.6 and d*0.8
print (GlycogenA2, 'm/s','is for increase glycolic metabolism and increase glycogen storage')
AllA3 = d*0.95
print (AllA3, 'm/s','is for lactate production and for increase VO2Max')

#Time lap training zones, time for the swwimer's (athlete) distance
T0 = b/RecA0
print ('You need to complete that distance in',(round (T0)),'seconds','for recovering purposes') 
T1 = b/FatA1
print ('You need to complete that distance in',(round (T1)),'seconds','for burning fat')
T2 = b/GlycogenA2
print ('You need to complete that distance in',(round (T2)),'seconds', 'for increase glycolic metabolism and increase glycogen storage')
T3 = b/AllA3
print ('You need to complete that distance in',(round (T3)),'seconds','is for lactate production and for increase VO2Max')

print('oVer and Over... Again ')


# BiBle - Workload and perception of effort in swimming training - Luís Rama, Ana M Teixeira
# Among others
