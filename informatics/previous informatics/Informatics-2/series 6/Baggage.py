'''
Created on 2015. 11. 19.

@author: User
'''
def carousel(int, char) :
   carousel = []
   for x in range(int) :
      carousel.append(None)
   count = 0
   for y in char :
      count1 = 0
      while count1 != 3 :
         if carousel[count] == None :
            count1 += 1
         count += 1
         count %= int
         
      carousel[count-1] = y
   temp = carousel[count-1:]
   carousel[count-1:] = []
   carousel[0:0] = temp
   return carousel
print(carousel(8, 'ABCDE'))


def rotated(list1, list2) :
   count = 0
   while list1[count] == None :
      count += 1
      if count == len(list1) :
         if list1 == list2 :
            return True
         else :
            return False
   try :
      index = list2.index(list1[count])
   except:
      return False
   b = list2[index-count:]
   list2[index-count:] = []
   list2[0:0] = b 
   if list1 == list2 :
      return True
   else :
      return False