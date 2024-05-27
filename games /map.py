#map 
#applies a function to each item in an iterable 
store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
        ("sock",10.00)]
to_euros = lambda data: (data[0],data[1]*0.82)#lambda function
to_dollars = lambda data: (data[0],data[1]/0.82)
store_euros =list(map(to_dollars,store)) #map has a function and the iterable data as parameters 
for i in store_euros:
    print(i)