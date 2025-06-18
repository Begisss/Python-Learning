fruits = ['apple', 'banana', 'cherry', 'mango','peach']
print("The third fruit is: ", fruits[3])

l1 = [1,3,4,6,7]
l2 = [2,5,8,9,10]
l1 + l2 

numbers = [45, 7, 8, 11, 12, 13, 7]
numbers2 = []
numbers2.append(numbers[0])
a = len(numbers)//2
numbers2.append(numbers[a])
numbers2.append(numbers[-1])
print(numbers2)

movies = ['batman', 'superman', 'interstellar', 'avatar', 'joker']
tuple_movies = tuple(movies)
print(tuple_movies)

cities = ['London', 'Tokyo', 'Paris', 'Los Angeles', 'Barcelona', 'Milan']
if 'Paris' in cities:
    print('Paris')

numbers = [1, 2, 3, 4, 5, 6, 7]
duplicated_numbers = numbers * 2
print(duplicated_numbers)

numbers = [7, 8, 9, 10, 11, 12]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)

numbers = tuple(range(1, 11))
slice_result = numbers[3:7]
print(slice_result)

colors = ['red', 'blue', 'green', 'blue', 'yellow', 'blue']
blue_count = colors.count('blue')
print(blue_count)

animals = ('cat', 'dog', 'lion', 'tiger', 'elephant')
lion_index = animals.index('lion')
print(lion_index)

numbers1 = (1, 2, 3, 4, 5)
numbers2 = (6, 7, 8, 9, 10)
numbers1 + numbers2 

car_brands = ['BMW','Audi','Bentley','Jaguar', 'Cadillac']
car_models = ('M590', 'RSQ8', 'Continental', 'FType')
print(len(car_brands))
print(len(car_models))

numbers = (2,3,4,5,6)
numbers_list = list(numbers)
print(numbers_list)

numbers = (2,3,4,5,6)
print(min(numbers), max(numbers))

words = ("apple", "banana", "cherry", "date", "strawberry")
reversed_words = words[::-1]
print(reversed_words)
