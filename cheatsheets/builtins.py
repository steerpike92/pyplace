'''naked functions'''

'''basic types'''

int(130.4)
int('41')
#int('344.10') raises error
float(10)
float('32.43')
bool(23)

bin(21)

str(10234.102)
str(120)
chr(54) # grab ascii character
ord('a') # unicode code point of character


'''basic math'''

abs(-2)
max(range(0,10))
min(range(0,10))
sum(range(1,10))
pow(10,10)
#print round(103.10462, ndigits=3) #103.105


#bytearray([source[, encoding[, errors]]])

'''basic boolean shit'''

all([True, True, False])
any([True, True, False])



#print "here's a number {}".format(10)
type(102)



'''sequence things'''

list(range(0,10))
tuple(range(1,10))
set(range(1,6))

range(0,10)
xrange(20,2,-2)
enumerate(range(5,10))
len(range(0,10))

zip(range(0,10), range(20,0,-2))
sorted([13,50,10,502,1,-32],
        key = lambda x: x**2, reverse=True)

reduce(lambda x,y: x*y, range(1,6)) #factorial(5)
map(lambda x: x**2, range(0,10))
filter(lambda x: x>4, range(0,10))

hash (('5','1','a'))


'''basic files'''

#file(name[,mode[,buffering]])
#open(name[, mode[, buffering]])

#raw_input
#input('prompt')


'''list methods'''
L=[]
L.append(10)
L.extend([1,0,60,10])
L.insert(3,-14) #injects -14 between index 2 and 3
L.remove(60)
#print L
#print L.pop()
#print L.pop(1)
L.append(132)
L.index(132)
L.count(132)
132 in L
L.sort(key = lambda x: x**2)
L.reverse()

'''set methods'''


import copy


S = set(L)
len(S)
42 in S
S2=copy.deepcopy(S)
S2.add(-29292)
S.isdisjoint(S2)
S.issubset(S)
S <= S2 #check if subset
S < S2 #check if proper subset
S.issuperset(S2)
S >= S2
S > S2
S.union(S2)
S3 = S | S2 | set([404]) #other union
S4=S3.intersection(set([404]))
S5 = S & S2
print S
print S3
print S4
print S5
#.remove(elem) #raises error if not found
#.discard(elem) #doesn't raise error
#.pop() #remove an arbitrary element, error if empty
#.clear()


'''string methods'''

s= 'Abcdefg'
s=''.join([s,'h','i'])
#print s
#print s.upper()
#print s.lower()
s2=s.capitalize()
i=s.count('bcd')
#str.decode([encoding[, errors]])
#str.encode([encoding[, errors]])
i=s.find('f') #return index or -1 if not found
i=s.index('f') #return index or error if not found
b=s.isalnum() #is all alphanumeric
b=s.isalpha()
b=s.isdigit()
b=s.islower()
b=s.isspace()
b=s.isupper()
s2=s.split('e')
s2=s.splitlines(True) #keyword for keep ends

s2=s.lstrip('ABC')
s2=s.rstrip('xyz') #any permutation of arg

import string
'''string constants'''
string.ascii_letters
string.ascii_lowercase
string.ascii_uppercase
string.digits
string.hexdigits
string.letters #location dependent
string.uppercase #location dependent
string.lowercase
string.printable
string.whitespace
string.punctuation



'''file I/O'''
f = open("example.txt")
for line in f:
    #do something
    pass
f.close()

#f.read() reads all at once, not a good idea (huge files)
#f.readlines returns a list of strings, also bad

with open("example.txt") as f:
    #do stuff with file
    #this is preferred way as it always closes the file
    pass
    




#buffer
