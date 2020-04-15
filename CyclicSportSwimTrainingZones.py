

#This script serves to cyclic sport, it aims the limits of energy production
#we know that these limits can be trained. Use a professional of this area 
#when training, be carefull with the amount at each speed... Be wise... 
#You can use this piece a code for the best purposes

import time

name = input ("What's your name? ")
print('Hi', name)
distance = input ("What's your swim distance (in meters)? ")
print('Only? You are getting old... Only', distance, '!')
b = int (distance)
ti = input ("How long did you take to swim it at full speed (in seconds)?")
print('Are you sure? Have you done the conversion??')
time.sleep (2)
c = int (ti)
d = b/c
print(d, 'm/s','is your full speed') 

#Speed training zones, speed for each metabolic zone
RecA0 = d*0.5
print (RecA0, 'm/s','is the speed for recovering purposes')
FatA1 = d*0.6
print (FatA1, 'm/s','is the speed for burning fat')
GlycogenA2 = d*0.6 and d*0.8
print (GlycogenA2,'and', FatA1, 'm/s','are the limits of speed for increase glycolic metabolism and lactate threshold')
AllA3 = d*0.95
print (AllA3, 'm/s','is the speed for increase lactate tolerance and VO2Max')

#Time lap training zones, time for the swwimer's (athlete) distance
T0 = b/RecA0
print ('You need to complete that distance in',(round (T0)),'seconds','for recovering purposes') 
T1 = b/FatA1
print ('You need to complete that distance in',(round (T1)),'seconds','for burning fat')
T2 = b/GlycogenA2
print ('You need to complete that distance between',(round (T1)),'and',(round (T2)),'seconds', 'for increase glycolic metabolism and lactate threshold')
T3 = b/AllA3
print ('You need to complete that distance in',(round (T3)),'seconds','for increase lactate tolerance and VO2Max')

time.sleep(3)

print ('Well, VO2Max only at maximum speeds. At what speed you finish a race?')

time.sleep(3)

print('oVer and Over... Again ')

time.sleep(2)
print('Again...')

time.sleep(3)
print('Do not miss the next chapter.... We dont')
 
# BiBle - Workload and perception of effort in swimming training - Luís Rama, Ana M Teixeira
# Among others
