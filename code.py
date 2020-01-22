# --------------
import yaml

# Read the data of the format .yaml type
with open(path) as f :
    data = yaml.load(f)
f.close()

# Find data type of the file
print (type(data))

# In which city, and at which venue the match was played and where was it played ?
print ("city and venue are : ",data['info']['city'],data['info']['venue'])

# Which are all the teams that played in the tournament ? How many teams participated in total?
print("teams are - ",data['info']['teams']," no of teams - ",len(data['info']['teams']))

# Which team won the toss and what was the decision of toss winner ?
print("toss winner - ",data['info']['toss']['winner']," and decision is ",data['info']['toss']['decision'])
print ("---"*20)
# Find the first bowler and first batsman who played the first ball of the first inning
print ("batsman : ", data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman'],"\n bowler is - ",data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler'])

print ("*****"*20)
# How many deliveries were delivered in first inning ?
print ("deliveries in 1st inning is -", len(data['innings'][0]['1st innings']['deliveries']))

# How many deliveries were delivered in second inning ?
print ("$$$"*20)

print("deliveries - ",len(data['innings'][1]['2nd innings']['deliveries']))
# Which team won and how ?

print ("match won by ", data['info']['outcome']['winner']," by ",data['info']['outcome']['by']['runs'], "runs")




