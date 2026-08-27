print("Hello World")
a = 2
b = 3.3
c = "Shayan"

# name = input("What is your name?")
print( )
print(a)
print(b)
print(c)
# print(name)
print( )

complex_data = 14 + 5j
print('Data : ',complex_data, ' Type ' , type(complex_data))
print( )

string_paragraph = 'Machine learning is a subfield of artificial intelligence.'
print('Data : ',string_paragraph, ' Type ' , type(string_paragraph))
print( )

t = 'Hello World!'
print(t)
print(t[0])
print(t[2:5])
print(t[2:])
print(t + " Test")
print( )

list_data = [1,2,3,4,5.1 ,"Shayan" ]
print(list_data)
print( )

tuple_data = (1,2,3,4,5.2 , "Shayan" )
print(tuple_data)
print( )

set_data = {1,2,3,4,5.1 ,"Shayan" }
print(set_data)
print( )

list1  = ["Physics" , "Chemistry" , "Engineering" , 1947 , 2001]
list2 =  [1,2,3,4,5,6,7,8,9]
print(list1)
print(list2)
print( )

list1[0] = 10
del list1[3]
print(list1)
print( )

my_tuple = (1,2,3,4,5,6,7,8,9)
print(my_tuple)
print( )

age = 20

if age >= 18:
    print("You are eligible for admission")
else:
    print("You are not eligible for admission")

print( )

for i in range(10):
    print(i+1,": " , "Hello World")

print( )

for alphabet in "John Cenassss":
    print(alphabet)
print( )

count = 0
while count < 10:
    print("The count is: ", count)
    count += 1

print( )
def non_para_func():
    print("Non Para Func Called")

non_para_func()

print( )

def details_func(name , age):
    print("Name : ", name)
    print("Age : ", age)
details_func(28,"Huzaifa")
print( )


def details(*Numbers):
    print("Numbers : ", Numbers)
details(1,2,3,4,5,6,7,8,9)