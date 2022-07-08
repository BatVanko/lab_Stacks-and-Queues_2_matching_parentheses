numbers_of_queries = int(input())
stacked_queries = []
for _ in range (numbers_of_queries):
    current_command = input().split()
    if int(current_command[0]) == 1:
        stacked_queries.append(current_command[1])
    elif int(current_command[0]) == 2:
        stacked_queries.pop()
    elif int(current_command[0]) == 3:
        print(max(stacked_queries))
    elif int(current_command[0]) == 4:
        print(min(stacked_queries))
print(", ".join(stacked_queries[::-1]))





