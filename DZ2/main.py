result = []
def divider(a, b):
 if a < b:
   raise ValueError
 if b > 100:
   raise IndexError
 return a/b
data = {10: 2, 2: 5, 23: 4, 18: 0, 0: 15, 8 : 4}
for key in data:
   try:
      res = divider(key, data[key])
      result.append(res)
   except Exception as error:
       print(type(error), "Неработает в общем то, переделавай давай")
print(result)