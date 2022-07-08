import time

expressions = input()
s = []

for i in range (len(expressions)):
    if expressions[i] == "(":
        s.append(i)
    elif expressions[i] == ")":
        start_index = s.pop()
        end_index = i+1
        print(expressions[start_index:end_index])




