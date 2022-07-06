# LogGen

# Introduction 

Several applications like Deep Learning (DL), Image Processing, and Digital Signal Processing (DSP) rely on the frequent and efficient computation of the logarithm function. Many of these applications use lower precision floating-point datatypes like IEEE half-precision (FP16), bfloat16 (BF16), tensorfloat32 (TF32) instead of single-precision (FP32) and double-precision (FP64). This is because lower precision reduces the computational complexity and memory bandwidth required, albeit with a small degradation in accuracy. While developing logarithm units for FP32 and FP64 datatypes has received a lot of attention, not a lot of effort has been put into the designs of logarithm units for smaller datatypes. Also, different DL applications have different area, delay, memory, accuracy, and datatype requirements. A one-size-fits-all design cannot satisfy all these requirements. LogGen is an open-source, parameterized generator for generating logarithm unit implementations optimized for smaller floating-point datatypes. LogGen enables generation of designs by varying multiple knobs - precision, accuracy, base of logarithm, storage, and latency. It uses a flexible and efficient Look-Up Table (LUT) based architecture that leverages the small size of datatypes to optimize this architecture. 

 If you find this work useful in your research, please cite the paper:
 
     https://ieeexplore.ieee.org/abstract/document/9806139
 
 You can also view the presentation on Youtube here: https://www.youtube.com/watch?v=oe2UdLfCCR8

# Knobs

Precision: This knob defines the floating-point precision (datatype) supported by the generated design. It controls the exponent and mantissa width of the floating-point input. For example, if the input of the knob is f5,10g, then the generated LOG unit will be for FP16. This knob supports any positive exponent and mantissa bit-width values as inputs.

Accuracy: This knob controls the number of most significant bits of mantissa used to index the LUT for mantissa (LUT-MANT). Thus, this knob defines the LUT-MANT size. Positive values less than or equal to the mantissa width of the Precision knob will be considered as valid inputs. For example, the mantissa width for FP16 is 10 but the first 8 bits from the most significant bit of the mantissa can be used to index LUT-MANT. The last 2 bits are ignored. This reduces the size of LUT-MANT from 2^10 to 2^8 entries, but lowers the accuracy of the design.

Base of Logarithm: This knob defines the base of the logarithm function of the design. All positive numbers are considered as valid inputs. The default value for
this knob is e and the LOG unit calculates natural logarithm. Other values like 2 or 10 can be used the generate LOG units that compute log2(x) or log10(x) respectively.

Storage: The LUT values can either be implemented using logic gates (LG) or can be stored in hard macro RAMs (RAM) or flip-flop based memories (FF) for ASIC designs. For FF, the synchronous single-port, read/write flip-flop based RAM (DW_ram_rw_s_dff) from the Synopsys DesignWare library was used. The simulation and synthesis models for the hard macro RAM were obtained using the OpenRAM tool. For FPGA designs, these values can be implemented using configurable logic blocks (CLB) or stored in Block RAMs (BRAM). Note: Currently, the LogGen repo currently only supports LG (the RTL for CLB knob is the same). For RAM, the LUTs can be replaced with modules from OpenRAM tool (https://github.com/VLSIDA/OpenRAM). For FF, the LUTs can be replaced with DW_ram_rw_s_dff if you have license for Synopsys Designware IP. For BRAM, Xilinx Vivado IP manager can be used to generate BRAM blocks. The LUT1.py and LUT2.py scripts can be modified to generate the pre-computed values for RAM, FF and BRAM. 

Pipeline: This knob is used to choose between the different floating-point adder implementations. Currently, this knob is only valid for ASIC designs and can take two values - pipe or no pipe. There are two different implementations of the floating-point adder. The first one has been obtained from the Synopsys DesignWare IP library called DW_fp_addsub and the other one is a custom design called FP_AddSub that has been designed by us. Note: Currently, FP_AddSub has not been open-sourced. You can use your own floating point adder module by simply replacing the DW_fp_addsub module instantiation with your module. If you would like to use FP_AddSub module, please contact me at prp1998@utexas.edu

# Makefile

The following command can be run to generate a natural log unit for BF16 with Accuracy knob = 7 -

    make EXPONENT=8 MANTISSA=7 ACCURACY=7 BASE=e 
You can modify the knob values to generate the desired configuration

Please report any bugs to prp1998@utexas.edu
