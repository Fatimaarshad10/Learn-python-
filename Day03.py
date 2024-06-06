# """Enumerate is use when i need the iteration or the key value"""
x = ('Apple', 'Orange', 'WaterMelon')
y = enumerate(x)
print(y)
listData = list(y)
print(listData)
# [(0, 'Apple'), (1, 'Orange'), (2, 'WaterMelon')]
for index , data in listData:
    print(f"index===> {index} , data ===> {data}")
file = open('write.txt' , 'w')
try:
    file.write('fatima is learning the code')
finally:
    file.close()
with open('write.txt', 'w') as file:
    file.write('hello here is the code ')

