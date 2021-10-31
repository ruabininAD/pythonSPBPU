#1


def nested_sum(t):
	f=0
	for i in t:
		f+=sum(i)
	return f
#print(_sum([[1,2,3,4,5],[2,3,4,5,6]]))

#2

def cumsort(t):
	s=[]
	for i in range(len(t)): 
		Sum=0
		for j in range(i+1):
			Sum+=int(t[j])
		s.append(Sum)
	return s
#print(cumsort([1,2,3,4,5]))
	
#сделать вторую задачу 

#3



def middel(t):
	t.pop(0)
	t.pop(len(t)-1)
	return t
#print(middel([1,2,3,4,5,6,7,8]  ))


#4


def chop(t): 
	t.pop(0)
	t.pop(len(t)-1)
#t=[1,2,3,4,5,6,7,8]
#chop(t)
#print(t)


#5

#t = [1,2,3,4,7,6]
def Is_sorted(t):
	if t == sorted(t):
		return True
	else:
		return False
#print(Is_sorted(t))


#6
def is_anagram(w1,w2): 
	print(w1,w2)
	w1.replace(" ", "")
	w2.replace(" ", "")
	w1=list(w1)
	w2=list(w2)
	print(w1,w2)
	w1=sorted(w1)
	w2=sorted(w2)
	if w1 == w2: 
		return True
	else:
		return False
#print(is_anagram("лепс спел","спел лепс"))

#7 

def has_duplicates(s):
	if type(s)==type(" sdsd"): 
		s=list(s)
	for i in s: 
		if s.count(i)>1: 
			return True
		else: 
			return False
#(has_duplicates("sdsfghjkl"))
			
	
	
			
		
