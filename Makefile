##command to execute python script

EXPONENT ?= 8
MANTISSA ?= 7
ACCURACY ?= 7
BASE ?= e
STORAGE ?= LG
PIPELINE ?= no_pipe

SUFFIX ?= e${EXPONENT}_m${MANTISSA}_a${ACCURACY}
DEPENDENCY ?= logunit_${SUFFIX}.v
DEPENDENCY2 ?= LUT1_${SUFFIX}_b${BASE}.v
DEPENDENCY3 ?= LUT2_${SUFFIX}_b${BASE}.v
DEPENDENCY:
	python logunit.py -e ${EXPONENT} -m ${MANTISSA} -a ${ACCURACY} -o ${DEPENDENCY}
	python LUT1.py -e ${EXPONENT} -m ${MANTISSA} -a ${ACCURACY} -b ${BASE} -o ${DEPENDENCY2}
	python LUT2.py -e ${EXPONENT} -m ${MANTISSA} -a ${ACCURACY} -b ${BASE} -o ${DEPENDENCY3}

