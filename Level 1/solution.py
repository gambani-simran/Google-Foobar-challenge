# Level 1 is a cakewalk, the problem being of easy level. Keeping the Commander Lambda's story aside,
# basically I was given 2 lists and had to find the element which was not present in both list, 
# i.e. an additional uncommon element from given two lists(There was only 1 uncommon element)

x = [14,27,1,4,2,50,3,1]
y = [2,4,-4,3,1,1,14,27,50]

from collections import Counter

def solution(x,y):

	c1 = Counter(x)
	c2 = Counter(y)

	if len(x) > len(y):
		diff = c1-c2
	else:
		diff = c2-c1


	print ("Hello")
	print(c1)
	print(c2)
	print(diff)

	if len(list(diff.elements())) == 1:
		addlElem = list(diff.elements())[0]

	return addlElem

z = solution(x,y)
print(z)