def most_frequent(str):
    str=str.lower()
    d={}
    for i in str:
        if i not in d:
            d[i]=1
        else:
            d[i] += 1
    for w in sorted(d, key=d.get, reverse=True):
        print(w,':',d[w])

str=input("Please enter a string: ")
most_frequent(str)