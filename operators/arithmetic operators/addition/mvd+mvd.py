#string+string

print("lucky"+"lucky")

#string+list()
print("a"+['a'])#type error

#string+tuple
print("a"+('a'))#type error

#string+set
print("a"+{'a'})#type error

#string+dict
print("a"+{'a':1})#type error


#list

#list+list
print([10,20,30]+[40,50,60])#10,20,30,40,50,60

#list+string
print([10]+"lucky")#type error

#list+tuple
print([10]+(1))#type error

#list+set
print([1]+{1})#type error

#list+dict
print([1]+{1:'lucky'})



#tuple

# tuple+tuple
print((1,2,3)+(2,3,4))#1,2,3,2,3,4

#tuple+string
print((1)+"lucky")#type error

#tuple+set
print((1)+{1})#type error

# tuple+dict
print((1)+{1:'w'})#type error


#set

#set+set
print({1}+{2})#type error

#set+string,set+tuple,set+dict,set+list = type error


#dict

# dict+dict

print({1:'s'}+{2:'d'})#type error

#dict+list,dict+string,dict+set,dict+tuple = type error

