import csv

with open('datasets/mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

# print(mpg[:3])  # The first three dictionaries in our list.
print(len(mpg))
print(mpg[0].keys())
cty = sum(float(d['cty']) for d in mpg) / len(mpg)
hwy = sum(float(d['hwy']) for d in mpg) / len(mpg)
cylinders = set(d['cyl'] for d in mpg)
print(cty, hwy, cylinders)
testSet = set(('cty', 'hwy', 'cylinders'))
print(testSet)

CtyMpgByCyl = []

for c in cylinders:  # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for d in mpg:  # iterate over all dictionaries
        if d['cyl'] == c:  # if the cylinder level type matches,
            summpg += float(d['cty'])  # add the cty mpg
            cyltypecount += 1  # increment the count
    CtyMpgByCyl.append((c, summpg / cyltypecount))  # append the tuple ('cylinder', 'avg mpg')

CtyMpgByCyl.sort(key=lambda x: x[0])
CtyMpgByCyl

