def second_largest(array):
    array.sort()
    return array[-2]
def diffrence(array):
 maks = max(array)
 mini = min(array)
 diffrence = maks - mini
 return diffrence
def med(array):
   array.sort()
   srodek = len(array) // 2
   return array[srodek]
def smallest_largest(array):
   small = min(array)
   larg = max(array)
   list1 = []
   list1.append (small)
   list1.append (larg)
   return list1
def string(array):
  wynik = "-".join(map(str, array))
  return wynik
      
      
     
