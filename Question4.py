it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#length of the set it_companies
print("The length of set it_companies is:", len(it_companies))

#Adding 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

#Inserting multiple IT companies at once to the set it_companies
multiple_it_companies= ["Accenture","DXC"]
it_companies.update(multiple_it_companies)
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove("DXC")
print(it_companies)

#What is the difference between remove and discard
#Remove: If the item to remove does not exist, remove() will raise an error
#Discard: If the item to remove does not exist, discard() will NOT raise an error

#Joining A and B
set1 = A.union(B)
print(set1)

#Finding A intersection B
set2 = A.intersection(B)
print(set2)

#Is A subset of B
set3 = A.issubset(B)
print(set3)

#Are A and B disjoint sets
set4 = A.isdisjoint(B)
print(set4)

#Join A with B and B with A
set5 = B.union(A)
print(set3,set5)

#What is the symmetric difference between A and B
set6 = A.symmetric_difference(B)
print(set6)

#Delete the sets completely
del A,B
#print(B)

#Convert the ages to a set and compare the length of the list and the set
set7= set(age)
print(len(set7))