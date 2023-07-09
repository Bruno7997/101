import random


def Dice(n):
 D=[0,0,0,0,0,0,0,0,0]
 if(n%2!=0):D[1]=D[3]=D[7]=D[5]=" "
 else:D[1]=D[4]=D[7]=" "
 if(n==3 or n==1):
  D[6]=D[2]=" "
  if(n==1):D[0]=D[8]=" "
   
 if(n==4 or n==2):
  D[3]=D[5]=" "
  if(n==2):D[0]=D[8]=" "
 
 return print(" _________\n",
              "|",D[0],D[1],D[2],"|\n",
              "|",D[3],D[4],D[5],"|\n",
              "|",D[6],D[7],D[8],"|\n",
              "‾‾‾‾‾‾‾‾‾")


R=input("Quer rolar um dado? Digite Y/N\n")
while(R=="Y"):
 N=random.randint(1,6)
 Dice(N)
 print("\n",N)
 R=input("\nQuer rolar novamente? Digite Y/N\n")


 