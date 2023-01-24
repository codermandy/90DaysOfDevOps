courses=['History','Geography','Maths','Science']
# Lists : prints index 0, 1
print(courses[0:2])
# Lists : prints index 2,3 ,4 ... n
print(courses[2:])
# Lists : Append courses in the end of list
courses.append('Arts')
print(courses)
#lists : Insert courses in the desired index
courses.insert(0,'Civics')
print(courses)
# lists : insert add another list[]  to existing list[[]]
courses2=['Maths','Computer']
courses.insert(0,courses2)
print(courses)
# lists: extends adds elements to original list []
courses.extend(courses2)
print(courses)
#lists : remove
removed=courses.remove('Maths'); #removest the particualr element
popped=courses.pop(); #removes the last element
print(removed)
print(popped)

courses=['History','Geography','Maths','Science']
# Lists : prints index 0, 1
# lists sort
nums=[2,6,1,9,5,-3,0]
nums.sort(reverse=True)
courses.sort(reverse=True)
s_courses=sorted(courses) #sorted list without altering original
print(nums)
print(courses)
print(s_courses)

#functions
print(sum(nums))

print(courses.index('Maths'))
print('Computer' in courses)

for item in courses:
    print(item)
for index,course in enumerate(courses,start=1):
    print(index,course)

course_str=' - '.join(courses)
print(course_str)

new_list=course_str.split(' - ')
print(new_list)

#list of cloud service providers
cloud_providers = ["AWS","GCP","Azure"]
cloud_providers.append("Digital Ocean")
print(sorted(cloud_providers))