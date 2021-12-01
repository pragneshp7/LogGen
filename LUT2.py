import numpy as np
import math
import sys
import getopt

argv = sys.argv[1:]

try:
	opts,args = getopt.getopt(argv,"e:m:a:o:b:")
except:
	f.write("ERROR!!");

for opt,arg in opts:
	if opt in ['-e']:
		exponen = arg
	if opt in ['-m']:
		mantiss = arg
	if opt in ['-a']:
		accurac = arg
	if opt in ['-b']:
		bas = arg
	if opt in ['-o']:
		file_name = arg

EXPONENT = int(exponen)
MANTISSA = int(mantiss)
ACCURACY = int(accurac)
BASE = str(bas)

print("Got exponent and mantissa as "+exponen+" and "+mantiss +" and "+accurac +" file name is "+file_name);
f = open(file_name,"w")


if EXPONENT <= 0:
	print("ERROR!!!\n")
	quit()
else:
	print("LUT2: EXPONENT>0\n")

if MANTISSA <= 0:
	print("ERROR!!!\n")
	quit()
else:
	print("LUT2: MANTISSA>0\n")

if ACCURACY <= 0 or ACCURACY>MANTISSA:
	print("ERROR!!!\n")
	quit()
else:
	print("LUT2:ACCURACY>0 and less equal to than MANTISSA\n")

#if int(BASE) <= 0:# or str(BASE)!='e':
#if str(BASE)!='e':
if str(BASE)!='e' and int(BASE)!=10:
	print("ERROR!!!\n")
	quit()
else:
	print("LUT2: BASE>0\n")


# Python program to convert a real value 
# to IEEE 754 Floating Point Representation. 

# Function to convert a 
# fraction to binary form. 
def binaryOfFraction(fraction): 

    # Declaring an empty string 
    # to store binary bits. 
    binary = str() 

    # Iterating through 
    # fraction until it 
    # becomes Zero. 
    while (fraction): 
        
        # Multiplying fraction by 2. 
        fraction *= 2

        # Storing Integer Part of 
        # Fraction in int_part. 
        if (fraction >= 1): 
            int_part = 1
            fraction -= 1
        else: 
            int_part = 0
    
        # Adding int_part to binary 
        # after every iteration. 
        binary += str(int_part) 

    # Returning the binary string. 
    return binary 

# Function to get sign bit, 
# exp bits and mantissa bits, 
# from given real no. 
def floatingPoint(real_no): 

    # Setting Sign bit 
    # default to zero. 
    sign_bit = 0

    # Sign bit will set to 
    # 1 for negative no. 
    if(real_no < 0): 
        sign_bit = 1

    # converting given no. to 
    # absolute value as we have 
    # already set the sign bit. 
    real_no = abs(real_no) 

    # Converting Integer Part 
    # of Real no to Binary 
    int_str = bin(int(real_no))[2 : ] 
    #f.write ("int_str= {0}".format(int_str))

    # Function call to convert 
    # Fraction part of real no 
    # to Binary. 
    fraction_str = binaryOfFraction(real_no - int(real_no)) 
    #f.write ("fraction_str= {0}".format(fraction_str))
    # Getting the index where 
    # Bit was high for the first 
    # Time in binary repres 
    # of Integer part of real no. 
    ind = int_str.find('1')
    if ind == -1:
        ind2 = fraction_str.find('1')
    else:
        ind2 = -1;
    #f.write ("ind= {0}".format(ind))
    #f.write ("ind2= {0}".format(ind2))
    # The Exponent is the no. 
    # By which we have right 
    # Shifted the decimal and 
    # it is given below. 
    # Also converting it to bias 
    # exp by adding 127. 
    if ind == -1:
        exp_str = bin(127-ind2-1)[2 : ] 
        #f.write ("exp_str= {0}".format(exp_str))
        #f.write ("ind= {0}".format(ind))    
        exp_str = ('0' * (8 - len(exp_str))) + exp_str
        #f.write ("len(exp_str)= {0}".format(len(exp_str)))
        #f.write ("bin(len(exp_str)= {0}".format(bin(15-ind2-1)))
    else:
        exp_str = bin((len(int_str) - ind - 1) + 127)[2 : ] 
        exp_str = ('0' * (8 - len(exp_str))) + exp_str
        #f.write ("len(int_str)= {0}".format(len(int_str)))
        #f.write ("bin(len(int_str)= {0}".format(bin((len(int_str) - ind - 1) + 15)))
    # getting mantissa string 
    # By adding int_str and fraction_str. 
    # the zeroes in MSB of int_str 
    # have no significance so they 
    # are ignored by slicing.
    if ind == -1: 
        mant_str = fraction_str[ind2 + 1 : ] 
    else:
        mant_str = int_str[ind + 1 : ] + fraction_str 
    # Adding Zeroes in LSB of 
    # mantissa string so as to make 
    # it's length of 23 bits. 
    mant_str = mant_str + ('0' * (MANTISSA - len(mant_str))) #to-do

    if real_no == 0:
        sign_bit = '0'
        exp_str = '00000000'
        for i in range (1, MANTISSA): #to-do
            mant_str += '0'
        #mant_str = '0000000000'
    # Returning the sign, Exp 
    # and Mantissa Bit strings. 
    return sign_bit, exp_str, mant_str 

# Driver Code 
if __name__ == "__main__": 

    # Function call to get 
    # Sign, Exponent and 
    # Mantissa Bit Strings. 
    #sign_bit, exp_str, mant_str = floatingPoint(-87.336544) 

    # Final Floating point Representation. 
    #ieee_32 = str(sign_bit) + '|' + exp_str + '|' + mant_str[0:7] 

    # Printing the ieee 32 represenation. 
    #f.write("IEEE 754 representation of -9.70000 is :") 
    #f.write(ieee_32) 

    a = np.float64(1)
    f.write("module LUT2(addr, log);\n")
    f.write("    input [" + str(ACCURACY-1) + ":0] addr;\n") #6 for LUT-MANT7
    SIZE = EXPONENT + MANTISSA
    f.write("    output reg [" + str(SIZE) + ":0] log;\n")
    f.write("\n")
    f.write("    always @(addr) begin\n")
    f.write("        case (addr)\n")
    #f.write("			7'b0"),
    #f.write("		: log = 16'b1111111110000000;")
    #f.write(ACCURACY)
    #f.write(pow(2,ACCURACY))
    for i in range (pow(2,ACCURACY)): #128 for LUT-MANT7
        if BASE == 'e':
            temp = np.log(a)/np.log(np.e)
        else:
            temp = np.log(a)/np.log(int(BASE))
        num = bin(np.float16(temp).view('H'))[2:].zfill(16)
        #f.write("			10'b{0:b}".format(i).zfill(7)),
        #f.write("		: log = 18'b{0};".format(num))
        sign_bit, exp_str, mant_str = floatingPoint(temp)    
        ieee_32 = str(sign_bit) + exp_str + mant_str[0:MANTISSA] 

        f.write("			" + str(ACCURACY) + "'b{0:b}".format(i)), #7 for LUT-MANT7 #to-do
        f.write("		: log = " + str(SIZE+1) + "'b{0};".format(ieee_32)+"\n")
        #f.write("  {0}".format(temp))
        a += np.exp2(-ACCURACY) #-7 for LUT-MANT7
    #f.write("			8'b11111111"),
    #f.write("		: log = 16'b0111111110000000;")
    f.write("        endcase\n")
    f.write("    end\n")
    f.write("endmodule\n")
