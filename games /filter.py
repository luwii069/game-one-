#filter ...inshort inachunga tu 

friends = [("Rachel", 19),
           ("Monica", 18),
           ("Phoebe", 17),
           ("Joey", 16),
           ("Chandler", 21),
           ("Rose", 20)]

# Define a lambda function to filter friends aged 18 or above
is_old_enough = lambda data: data[1] >= 18

# Use filter() to apply the lambda function to the list of friends
drinking_friends = list(filter(is_old_enough, friends))

# Print the list of friends who are old enough to drink
for friend in drinking_friends:
    print(friend)

    #e= lambda data:data[i]>=18
#drinking=list(filter(age,friends))
#for i in drinking:
 #   return i
 #additional n shorter
 #reduce function basically recycles

 #import functools
 #letters = ["H","E","L","L","O"]
 #word = functools.reduce(lambda x,y:x+y,letter)
 #print(word)
