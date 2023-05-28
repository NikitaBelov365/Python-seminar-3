dict = {"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}

result = []
for i in dict:
    result.append(list(i.values())[0])
x = set(result)
print(x)