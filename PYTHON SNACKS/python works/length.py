

#user enter velocity,V in m/s
# user enter acceleration,a in m/s^2
#minimum runway length is calculated 



speed = float(input("enter speed:"))

acceleration= float(input("enter acceleration:"))


length = speed**2/(2*acceleration)



        print(f"The runway length for the airplane is: {length:.2f}")


