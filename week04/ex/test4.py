import json

arr = []
file = open("JSON.tsv", 'r')
a = file.readline()

titles = [t.strip() for t in a.split('\t')]

# for line in file:
#     d = {}
#     #print(d)
#     for t, f in zip(titles, line.split('\t')):
#         d[t] = f.strip
#         print(d[t])
#     arr.append(d)


for line in file:
    d = {}
    #print(line)
    #print(d)
    for t, f in zip(titles, line.split('\t')):
        d[t] = f.strip()
        #print(titles)
        #print(f.strip)
        #print(t)
        #print(f)
        #print(d[t])
        #print(d)
    arr.append(d)
    #print(d)




    #print(d)
    #print(a.strip())


jsonfile = open("JSONtest.json","w")
jsonfile.write(json.dumps(arr,indent=3))



# for i in range (len(aInString)):
#     print([i])