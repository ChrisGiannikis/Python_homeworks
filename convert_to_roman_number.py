
print "Give me a number"
number = input()

from collections import OrderedDict
def write_latin(number):

     latin = OrderedDict()
     latin[1000000] = "M_"
     latin[900000] = "C_M_"
     latin[500000] = "D_"
     latin[400000] = "C_D_"
     latin[100000] = "C_"
     latin[90000] = "X_C_"
     latin[50000] = "L_"
     latin[40000] = "X_L_"
     latin[10000] = "X_"
     latin[9000] = "I_X_"
     latin[5000] = "V_"
     latin[4000] = "I_V_"
     latin[1000] = "M"
     latin[900] = "CM"
     latin[500] = "D"
     latin[400] = "CD"
     latin[100] = "C"
     latin[90] = "XC"
     latin[50] = "L"
     latin[40] = "XL"
     latin[10] = "X"
     latin[9] = "IX"
     latin[5] = "V"
     latin[4] = "IV"
     latin[1] = "I"

     def latin_number(number):
         for j in latin.keys():
             m , y = divmod(number, j)
             yield latin[j] * m
             number -= (j * m)
             if number > 0:
                 latin_number(number)
             else:
                 break

     return "".join([a for a in latin_number(number)])

     print "This number in latin is: "

print write_latin(number)
