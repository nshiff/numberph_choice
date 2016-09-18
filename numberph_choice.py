


import random


toilets = []
n = 10

while len(toilets) < n:
	newToilet = random.randint(1,n*10)
	if newToilet not in toilets:
		toilets.append(newToilet)

print(toilets)
pivotSubscript = int(len(toilets) / 3)
print("ANALYSIS")
print("allowed to stop after element " + str(pivotSubscript) + " (" + str(toilets[pivotSubscript]) + ")") 
print("best: " + str(min(toilets)))
print("worst: " + str(max(toilets)))
print("")





bestSoFar = n*999
i=0
print("EXPERIMENT")
for t in toilets:

	if t < bestSoFar:
		bestSoFar = t
		print("new best: " + str(bestSoFar))
		if i > pivotSubscript:
			print('sticking with that')
			break
		else:
			print('but it\'s still early')

	if i == len(toilets) - 1:
		print('damn, last toilet')
		bestSoFar = t

	i += 1





print("chose " + str(bestSoFar))





