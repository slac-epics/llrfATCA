#!../../bin/linuxRT-x86_64/llrfHLS_Sc
# ====================================================================
# SC-HXR (LCLS-II Timing)
# Will be used for SC [STCAV and XTCAV] by llrfHLS_SCApp
# ====================================================================

< envPaths

# ====================================================================
# Setup system specific environment variables
# ====================================================================
# Setup environment variables
epicsEnvSet("IOC",      "sioc-b15-rf05")
epicsEnvSet("PRIMARY",  "SIOC")
epicsEnvSet("LOCA",     "B15")
epicsEnvSet("UNIT",     "RF05")
epicsEnvSet("INST",     "0")
epicsEnvSet("FPGA_IP0", "10.0.1.105")

# ====================================================================
# Call common script for, for the SC LINAC LLRF firmware.
# -- call ../common/st.cmd_SC
# ====================================================================
< ../common/st.cmd_SC

