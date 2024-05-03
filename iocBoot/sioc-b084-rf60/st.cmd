#!../../bin/linuxRT-x86_64/llrf

< envPaths

# ====================================================================
# Setup system specific environment variables
# ====================================================================
# Setup environment variables
epicsEnvSet("IOC",      "sioc-b084-rf60")
epicsEnvSet("PRIMARY",  "SIOC")
epicsEnvSet("LOCA",     "B084")
epicsEnvSet("UNIT",     "RF60")
epicsEnvSet("INST",     "0")
epicsEnvSet("FPGA_IP0", "10.0.2.104")


# ====================================================================
# Call common script for, for the specific system type
# - Gen1 : call ../common/st.cmd_gen1
# - Gen2 : call ../common/st.cmd_gen2
# for UED
# - Gen1 : call ../common/st.cmd_ued_gen1
# - Gen2 : call ../common/st.cmd_ued_gen2
# ====================================================================
< ../common/st.cmd_ued_gen1

