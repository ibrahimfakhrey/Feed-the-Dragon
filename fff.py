import random
names=["هادي ","معاذ","عمر","زين"]
yassin_is_here=True

while yassin_is_here:
    x=input("هو ياسين هنا يا حج ؟ \n")
    if x=="اه":
        y=random.choice(names)
        print( f"انا هضرب { y}")
    if x=="لا":
        print(" باي باي انا هنام خلاص انا هقفل بقي عايز حاجة  ")
        yassin_is_here=False
