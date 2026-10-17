
#1
activity = int(input ("enter activity lvl"))

punctuality= int (input("enter punchuality lvl"))

if activity<0 or punctuality<0 and punctuality>100:
    print("Invalid")
elif activity>=8 and punctuality>=80:
    print("highly engaged")
elif activity< 4 or punctuality < 60:
    print("need improvement")
else :
    print("moderately engage")
