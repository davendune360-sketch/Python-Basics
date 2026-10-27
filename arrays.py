#store lots of data
import numbers

# data structures
# list, set, dictionary

people = ["Jack", "Jane", "Ahmed", "Hussein", "Marion"]
scores = [87, 45, 52, 91, 67, 29, 66, 71, 81]

# print(people[0])
# print(scores[0])
# print(people[-1])# last value
# people.append("Willis")
# print(people)
# scores.append(44)
# print(scores)
# print.clear()
# people.sort()
# scores.sort(reverse=True)
# print(people)
# print(scores)

# print(scores[0],scores[-1])
# print( sum(scores) / len(scores) )
# print(scores.count(88))

scores.sort()
# slicing
# print(scores)
# print(scores[-3:])
# print(scores[:3])
# print(scores[3:5]) #

# set -- remove duplicates
numbers = {87, 89, 87, 67, 54}
print(numbers)

# tuple --immutable duplicates
days = ("Mon", "Tue", "Fri", "Sat", "Sun")

# dictionary Key + value
person = {"name": "Zillow", "city": "Marsbit", "age":19}
print(person["name"])

# data structures + algorithms
print(sum(numbers))

watu = [{"name": "Sila", "age":22},
        {"name": "Sila", "age":22},
        {"name": "Sila", "age":22}]
print(watu[1]["name"])