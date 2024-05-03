#!../../bin/linuxRT-x86_64/llrfHLS_Sc
# ===============================================================================
# 2600 MHz Upconverter/Downconverter AMC cards used for SC PCAV and LaserLocker
# So, can we use the NC LLRF firmware??
# ===============================================================================

< envPaths

# ====================================================================
# Setup system specific environment variables
# ====================================================================
# Setup environment variables
epicsEnvSet("IOC",      "sioc-b084-rf99")
epicsEnvSet("PRIMARY",  "SIOC")
epicsEnvSet("LOCA",     "B084")
epicsEnvSet("UNIT",     "RF99")
epicsEnvSet("INST",     "0")
epicsEnvSet("FPGA_IP0", "10.0.1.105")

# ====================================================================
# Call common script for, for the SC LINAC LLRF firmware.
# -- call ../common/st.cmd_SC_2600_gen2
# ====================================================================
< ../common/st.cmd_SC_2600_gen2

