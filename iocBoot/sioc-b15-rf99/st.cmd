#!../../bin/linuxRT-x86_64/llrfHLS_Sc

< envPaths

# ====================================================================
# Setup system specific environment variables
# ====================================================================
# Setup environment variables
epicsEnvSet("IOC",      "sioc-b15-rf99")
epicsEnvSet("PRIMARY",  "SIOC")
epicsEnvSet("LOCA",     "B15")
epicsEnvSet("UNIT",     "RF99")
epicsEnvSet("INST",     "0")
epicsEnvSet("FPGA_IP0", "10.0.1.103")

# ====================================================================
# Call common script for, for the SC LINAC LLRF firmware.
# -- call ../common/st.cmd_SC
# ====================================================================
< ../common/st.cmd_SC_3

