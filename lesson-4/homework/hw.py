my_dict = {'apple': 10, 'banana': 5, 'cherry': 20, 'date': 15}
asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", asc_sorted)
desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", desc_sorted)  

dict = {'club': 'Barcelona', 'country' : 'Spain'}
dict['continent'] = 'Europe'

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = dic1.copy() 
result.update(dic2)
result.update(dic3)

n = int(input("Enter a number: "))
squares = {}
for x in range(1, n + 1):
    squares[x] = x * x
print(squares)

n = int(input("Enter a number: "))
result = {}
for i in range (1, n + 1 ):
    result[i] = i * i
print(result)

my_set = {1, 2, 3, 4}
print(my_set)

my_set = {'a', 's', 'd', 'r'}
for i in  my_set:
    print(i)

yangi_set = {'barca','real','sevilla'}
yangi_set.add('atletico')
yangi_set

yangi_set.update(['valencia', 'villareal', 'betis'])
yangi_set

yangi_set.remove('barca')
yangi_set

yangi_set.discard('real')
yangi_set
