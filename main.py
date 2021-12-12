
# num1 = int(input('enter a number :'))
# num2 = int(input('enter a another :'))
#
# result = num1 - num2
# print('the result is' + str(result))
#
# print(eval('result + 3'))
#
# result = input('Enter your expression')
# print(eval(result))
#
# money = 1000
# print(money > 1000 == False)
#
# thelist = ["orange","apple","lemon",'orange', 'orange']
# # print(len(thelist))
# # print(thelist.count('orange'))
# thelist.append(['add','test'])
# thelist.insert(4, 'first')
#
# print(thelist.pop())

# name = 0
# if name > 3:
#     print('right')
# elif name < 1:
#     print('nice')
# else:
#     print('none')

# for index in range(10):
#     print('hello world')

# array = ['cat','dog','cow','bird','fish']

# for i in range(len(array)):
#     if array[i] >= 'cow':
#         break
#     array[i] = 'love ' + array[i]
#     print(array[i])

# for element in array:
#     element = 'love ' + element
#     print(element)
# index = 0
# while index < len(array):
#     if index == 2:
#         index += 1
#         break
#     print(array[index])
#     index +=1

# arr = ['one','two','three','four','five'] # list
# print(type(arr))
#
# my_tuple = ('one','two','three','four','five') #tuple
# print(type(my_tuple))

# x = ('one','two','three','four')
# y = list(x)
# y[1] = 'change'
#
# z = tuple(y)
# print(z)


# the_set = {'one','two','three','four','five'} #set
# print(type(the_set))
# print(the_set)



dictionary = {
    'name' : 'khine lin tun',
    'father_name' : 'U Ba',
    'age' : 26,
    'address' : 'No(46), Thadipadan Street, Tamwe Township, Yangon',
    'single' : True
}
# x = dictionary.keys()
# print(type(list(x)))

# print(dictionary.keys())
# print(dictionary.values())
# print(list(dictionary.items()))
# dictionary.update({'name' : 'Harry'})
# dictionary.update({'phone': '0911111111'})
# dictionary.pop('phone')
# dictionary.popitem() #last item remove (version 3.7 above support)
# del dictionary['name'] # we can radom remove.
# print(dictionary)

# for key in dictionary:  method_one
#     print(dictionary[key])
#
# for ele in dictionary.values(): #method_two
#     print(ele)

# for key in dictionary.keys(): #method_three
#     print(key)

# for tuple in dictionary.items(): #method_four
#     print(tuple)
for (key, value) in dictionary.items(): #method_five
    print(key,value)




