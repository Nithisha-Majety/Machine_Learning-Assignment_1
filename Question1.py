import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sorting the list
ages.sort()
print("Sorted list: ", ages)

#Finding min and nax age from list
min_age = ages[0]
max_age = ages[-1]

print("Min value in list : " , min_age ,"\n"  "Max value in list : " , max_age)
ages.append(min_age) #Appending min and max values to list
ages.append(max_age)
#Appended list
print("Appended list:", ages)

#median of ages (one middle item or two middle items divided by two)
median_of_ages = statistics.median(ages)
print("Median of the list:", median_of_ages)

#average of age (sum of all items divided by their number)
avg_of_ages = sum(ages)/len(ages)
print("Average of the list : ", avg_of_ages)

#Range of ages
ran = max_age - min_age
print("Range of the list :", ran)







