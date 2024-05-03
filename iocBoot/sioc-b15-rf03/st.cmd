#!../../bin/linuxRT-x86_64/llrfHLS_Nc

< envPaths

# ====================================================================
# Setup system specific environment variables
# ====================================================================
# Setup environment variables
epicsEnvSet("IOC",      "sioc-b15-rf03")
epicsEnvSet("PRIMARY",  "SIOC")
epicsEnvSet("LOCA",     "B15")
epicsEnvSet("UNIT",     "RF03")
epicsEnvSet("INST",     "0")
epicsEnvSet("FPGA_IP0", "10.0.1.103")
#epicsEnvSet("FPGA_IP0", "10.0.1.102")

# ====================================================================
# Call common script for, for the NC LINAC LLRF firmware.
# -- call ../common/st.cmd_NC
# ====================================================================
< ../common/st.cmd_NC

