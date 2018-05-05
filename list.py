'''
Created on May 5, 2018

@author: o_olasub
'''
 #list
name =  ['p','r','o','g','r','a','m','m','e','r']
print(name[5],"\n")
#iterate 
for x in name:
    print(x)
    
#merege all the list
print("****join****")
names="".join(name)
print (names)
print (", ".join(name))

#swap
print("****swap****")
name[0],name[5]=name[5],name [0]

#slice  [beginning,end,step]
print("****slice****")
n=name[2:];print(n)
ne=name[:2];print(ne)
nex=name[::5];print(nex)
nexts=name[1:9:2];print(nexts)


#index- prints out position of the first value it  meets name.index(value,where to start from)
print("****index****")
print ("the first m is at position ",name.index('m'))
#print (name.index('z'))  #ValueError: 'z' is not in list   
print ("the next m is at position ",name.index('m',name.index('m')+1)) #looks for the next "m" on the list 

#reverse
print("****reverse****")
nexts.reverse() #doesn't return only reverses
print(nexts)

#count-gets the number of times a value occurs
print("****count****")
print("the number of z's in the list is ",name.count('z'))
print("the number of r's in the list is ",name.count('r'))

#sort-sorts alphabetically
print("****sort****")
name.sort()
print(name)

#len-length of list
print("****length****")
print(len(name))

#append- add to the end of list
print("****append****")
name.append('z')
print(name)

#insert- insert at any position (positon,value)
print("****insert****")
name.insert(5,"b")
print (name)
#extend - merge another list
print("****extend****")
name.extend(['n','e','w'])
print(name)

#pop  - removes based on positon
print("****pop****")
print ("the letter removed is ",name.pop(2)) #removes the last one. it returns the roved word
print(name)
print ("the letter removed is ",name.pop(2)) #removes the last one. it returns the roved word
print(name)

#remove  - removes based on value(removes first value it sees)
print("****remove****")
name.remove('m')
print(name)

#clear-remove all
print("****clear****")
name.clear()
print(name)
