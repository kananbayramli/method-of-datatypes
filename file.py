list_method = []
for method in dir(list):
  if method.startswith('__'):
    continue
  list_method.append(method)

tuple_method = []
for method in dir(tuple):
  if method.startswith('__'):
    continue
  tuple_method.append(method)

set_method = []
for method in dir(set):
  if method.startswith('__'):
    continue
  set_method.append(method)

string_method = []
for method in dir(str):
  if method.startswith('__'):
    continue
  string_method.append(method)

dict_method = []
for method in dir(dict):
  if method.startswith('__'):
    continue
  dict_method.append(method)


titles = ['List methods','Tuple method','Set method','String method','Dict method']
classes = [list_method,tuple_method,set_method,string_method,dict_method]

max_len = 0
for classs in classes:
  if max_len < len(classs):
    max_len = len(classs)

with open('Method.txt','w') as f:
  for title in titles:
    print(title, end='')
    print(' '*(30 - len(title)),end='')
    f.write(title)
    f.write(' '*(30 - len(title)))
  for i in range(max_len):
    print()
    f.write('\n')
    for classs in classes:
      if i >=len(classs):
        print('-------',end='')
        print(' '*23 , end='')
        f.write('-------')
        f.write(' '*23)
      else:
        print(classs[i],end='')
        print(' '*(30-len(classs[i])),end='')
        f.write(classs[i])
        f.write(" " * (30 - len(classs[i])))


