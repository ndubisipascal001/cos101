print("PHYSICS FORMULA CALCULATOR")
print("1. power")
print("2. speed")
print("3. workdone")
print("4. acceleration")
print("5. potential energy")

choice=int(input("choose a formula (1-5):"))

if choice== 1:
    work= float(input("enter workdone(J):"))
    time= float(input("enter time(s):"))
    power=work/time
    print("power=",power,"w")

elif choice ==2:
    distance=float(input(" enter distance(m):"))
    time= float(input("enter time(s):"))
    speed= distance/time
    print("speed=",speed,"m/s")

elif choice == 3:
    force=float(input("enter force(N):"))
    distance=float(input("enter distance(M)"))
    workdone =force* distance
    print("workdone =",workdone,"J")

elif choice == 4:
    u=float(input("enter inital velocity(m/s):"))
    v=float(input("enter final velocity(m/s):"))
    time=float(input("enter time(s):"))
    acceleration=(v-u)/time
    print("Acceleration=",acceleration,"m/s2")

elif choice==5:
    mass=float(input("enter mass(kg):")) 
    height=float(input("enter heigth(m):"))
    g=9.8
    potential_energy=mass*g*height
    print("potential energy=",potential_energy,"j")   

else:
    print("wrong option")



