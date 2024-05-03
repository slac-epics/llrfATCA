#!../../bin/linuxRT-x86_64/llrfHLS_Nc
# ====================================================================
# NC-HXR (LCLS-I Timing)
# Will be used for NC [XTCAV and LCLS LINAC Upgrades] by llrfHLS_NCApp
# ====================================================================

< envPaths

# ====================================================================
# Setup system specific environment variables
# ====================================================================
# Setup environment variables
epicsEnvSet("IOC",      "sioc-b084-rf54")
epicsEnvSet("PRIMARY",  "SIOC")
epicsEnvSet("LOCA",     "B084")
epicsEnvSet("UNIT",     "RF54")
epicsEnvSet("INST",     "0")
epicsEnvSet("FPGA_IP0", "10.1.1.102")

# ====================================================================
# Call common script for, for the NC LINAC LLRF firmware.
# -- call ../common/st.cmd_NC
# ====================================================================
< ../common/st.cmd_NC

