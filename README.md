# LogGen

Repo under construction. Please contact me at prp1998@utexas.edu if you would like to use the log units

#Abstract 

Several applications like Deep Learning (DL), Image Processing, and Digital Signal Processing (DSP) rely on the frequent and efficient computation of the logarithm function. Many of these applications use lower precision floating-point datatypes like IEEE half-precision (FP16), bfloat16 (BF16), tensorfloat32 (TF32) instead of single-precision (FP32) and double-precision (FP64). This is because lower precision reduces the computational complexity and memory bandwidth required, albeit with a small degradation in accuracy. While developing logarithm units for FP32 and FP64 datatypes has received a lot of attention, not a lot of effort has been put into the designs of logarithm units for smaller datatypes. Also, different DL applications have different area, delay, memory, accuracy, and datatype requirements. A one-size-fits-all design cannot satisfy all these requirements. LogGen is an open-source, parameterized generator for generating logarithm unit implementations optimized for smaller floating-point datatypes. LogGen enables generation of designs by varying multiple knobs - precision, accuracy, base of logarithm, storage, and latency. It uses a flexible and efficient Look-Up Table (LUT) based architecture that leverages the small size of datatypes to optimize this architecture. 

 If you find this work useful in your research, please cite:
 
 You can also view the presentation on Youtube here:
 
     https://www.youtube.com/watch?v=oe2UdLfCCR8
