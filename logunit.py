import sys
import getopt

argv = sys.argv[1:]

try:
	opts,args = getopt.getopt(argv,"e:m:a:o:")
except:
	print("ERROR!!");

for opt,arg in opts:
	if opt in ['-e']:
		exponent = arg
	if opt in ['-m']:
		mantissa = arg
	if opt in ['-a']:
		accuracy = arg
	if opt in ['-o']:
		file_name = arg
print("Got exponent and mantissa as "+exponent+" and "+mantissa +" and "+accuracy +" file name is "+file_name);

##net = int(exponent) + int(mantissa) + 2
net = int(exponent) + int(mantissa) 
#print("Net is "+ str(net))

f = open(file_name,"w")
f.write("`timescale 1ns / 1ps\n")
f.write("\n")
##f.write("`define MANT10 // can take values from MANT10-5\n")
f.write("\n")
f.write("module logunit (clk, fpin, fpout, rst);\n")
f.write("\n")
f.write("\n")
f.write("	input ["+str(net)+":0] fpin;\n")
f.write("	output ["+str(net)+":0] fpout;\n")
f.write("\n")
f.write("	input clk,rst;\n")
f.write("\n")
f.write("\n")
f.write("	wire ["+str(net)+": 0] fxout1;\n")
f.write("	wire ["+str(net)+": 0] fxout2;\n")
f.write("\n")
f.write("	reg ["+str(net)+": 0] pipe1;\n")
f.write("	reg ["+str(net)+": 0] pipe2;\n")
f.write("\n")
f.write("	LUT1 lut1 (.addr(fpin["+str(net-1)+":"+str(mantissa)+"]),.log(fxout1)); // LUT for exponent\n")
##Above was 17:10 didn't understand what to move to
f.write("\n")
#f.write("`ifdef MANT10\n")
f.write("	LUT2 lut2 (.addr(fpin["+str(int(mantissa)-1)+":"+str(int(mantissa)-int(accuracy))+"]),.log(fxout2));  // LUT for mantissa\n")
##f.write("`elsif MANT9\n")
##f.write("	LUT2_9 lut2 (.addr(fpin[9:1]),.log(fxout2));  \n")
##f.write("`elsif MANT8\n")
##f.write("	LUT2_8 lut2 (.addr(fpin[9:2]),.log(fxout2)); \n")
##f.write("`elsif MANT7\n")
##f.write("	LUT2_7 lut2 (.addr(fpin[9:3]),.log(fxout2)); \n")
##f.write("`elsif MANT6\n")
##f.write("	LUT2_6 lut2 (.addr(fpin[9:4]),.log(fxout2)); \n")
##f.write("`elsif MANT5\n")
##f.write("	LUT2_5 lut2 (.addr(fpin[9:5]),.log(fxout2)); \n")
##f.write("`endif\n")
f.write("\n")
f.write("	DW_fp_addsub add(.a(pipe1), .b(pipe2), .rnd(3'b0), .op(1'b0), .z(fpout), .status());\n")
f.write("\n")
f.write("always @(posedge clk or negedge rst)\n")
f.write("begin\n")
f.write("	if (!rst) begin\n")
f.write("		pipe1 <= 0;\n")
f.write("		pipe2 <= 0;\n")
f.write("	end\n")
f.write("	else begin\n")
f.write("		pipe1 <= fxout1;\n")
f.write("		pipe2 <= fxout2;\n")
f.write("	end\n")
f.write("end\n")
f.write("endmodule\n")
f.close()
