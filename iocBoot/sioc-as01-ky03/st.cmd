#!../../bin/linuxRT-x86_64/llrf

< envPaths

# ====================================================================
# Setup system specific environment variables
# ====================================================================
# Setup environment variables
epicsEnvSet("IOC",      "sioc-as01-ky03")
epicsEnvSet("PRIMARY",  "SIOC")
epicsEnvSet("LOCA",     "AS01")
epicsEnvSet("UNIT",     "KY03")
epicsEnvSet("INST",     "0")
epicsEnvSet("FPGA_IP0", "10.0.1.105")

# ====================================================================
# Call common script for, for the specific system type
# - Gen1 : call ../common/st.cmd_gen1
# - Gen2 : call ../common/st.cmd_gen2
# for UED
# - Gen1 : call ../common/st.cmd_ued_gen1
# - Gen2 : call ../common/st.cmd_ued_gen2
# ====================================================================
< ../common/st.cmd_ued_gen1

