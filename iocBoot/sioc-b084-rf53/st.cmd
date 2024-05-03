#!../../bin/linuxRT-x86_64/llrf

< envPaths

# ====================================================================
# Setup system specific environment variables
# ====================================================================
# Setup environment variables
epicsEnvSet("IOC",      "sioc-b084-rf53")
epicsEnvSet("PRIMARY",  "SIOC")
epicsEnvSet("LOCA",     "B084")
epicsEnvSet("UNIT",     "RF53")
epicsEnvSet("INST",     "0")
epicsEnvSet("FPGA_IP0", "10.0.1.106")

# ====================================================================
# Call common script for, for the specific system type
# - Gen1 : call ../common/st.cmd_gen1
# - Gen2 : call ../common/st.cmd_gen2
# ====================================================================
< ../common/st.cmd_gen1

