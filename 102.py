import os, shutil, time

to="C:/Users/SUZANA/Desktop/Projeto101"
fromD="c:/Users/SUZANA/Desktop/Python 1"
response = str(input("Deseja mover para(Y) ou mover de volta(N)?\t"))
if(response=="Y"):list=os.listdir(fromD)
else: list=os.listdir(to)

print(list)

for F in list:
 R, E = os.path.splitext(F)
 print(R+" / "+E+"\n")

 if E == "": continue
 if E not in [".py"]:
 
  if(response=="Y"):path1=fromD+"/"+F; path2=to; path3=to+"/"+F
  else: path1=to+"/"+F; path2=fromD; path3=fromD+"/"+F
  

  if(os.path.exists(path2)):
   print("Movendo "+F)
   shutil.move(path1, path3)
  else:
   os.makedirs(path2)
   shutil.move(path1, path3)
 
