data = [1,3,2,4,7,3,2,2,1,4]
result = []
for item in data:
    if item not in result:
        result.append(item)
        print(result)