TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#========================================
USR_CXXFLAGS += -DHAVE_YAML -fno-delete-null-pointer-checks
# ================================================
# Build the IOC application
# =======================================================
# This will attempt to build an IOC application
# for every target including the host computer.

# In this case, I would like to build only for linuxRT 
# which is the target OS for the LLRF ATCA-based Platform
# ========================================================

ifeq ($(T_A),linuxRT-x86_64)
 PROD_IOC = llrfHLS_Nc
endif


# llrfHLS_Nc.dbd will be created and installed
DBD += llrfHLS_Nc.dbd

# llrfHLS_Nc.dbd will be made up from these files:
llrfHLS_Nc_DBD += base.dbd
llrfHLS_Nc_DBD += asyn.dbd
llrfHLS_Nc_DBD += yamlLoader.dbd
llrfHLS_Nc_DBD += yamlDownloader.dbd
llrfHLS_Nc_DBD += devIocStats.dbd
llrfHLS_Nc_DBD += asSupport.dbd
llrfHLS_Nc_DBD += caPutLog.dbd
llrfHLS_Nc_DBD += $(CEXP_DBDS)
llrfHLS_Nc_DBD += crossbarControl.dbd
llrfHLS_Nc_DBD += tprTriggerAsynDriver.dbd
llrfHLS_Nc_DBD += tprPatternAsynDriver.dbd

# LCLS1 style BSA
llrfHLS_Nc_DBD += bsaCore.dbd
llrfHLS_Nc_DBD += bsa.dbd

llrfHLS_Nc_DBD += RFCommon.dbd
llrfHLS_Nc_DBD += ATCACommon.dbd
llrfHLS_Nc_DBD += llrfHlsAsynDriver.dbd
llrfHLS_Nc_DBD += interlockRtmAsyn.dbd
llrfHLS_Nc_DBD += timeAxisGenerator.dbd
llrfHLS_Nc_DBD += llrfAmcAsyn.dbd
# ================================================================================
# The system command will be mainly used by linux hosted IOCs
# Very useful for changing kernel thread priorities for kernel drivers
# ================================================================================
llrfHLS_Nc_DBD += system.dbd

# ======================================================================
# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
llrfHLS_Nc_SRCS += llrfHLS_Nc_registerRecordDeviceDriver.cpp

llrfHLS_Nc_SRCS_DEFAULT += llrfHLS_NcMain.cpp

llrfHLS_Nc_SRCS_vxWorks += -nil-

# ========================================================================
# ========================================================================
# Add locally compiled object code
# For example, subroutines
# ========================================================================
#llrfHLS_Nc_SRCS +=

# =====================================================
# Link in the code from other libraries
# =====================================================
llrfHLS_Nc_LIBS += yamlLoader
llrfHLS_Nc_LIBS += yamlDownloader
llrfHLS_Nc_LIBS += tprTrigger
llrfHLS_Nc_LIBS += tprPattern
llrfHLS_Nc_LIBS += ATCACommon
llrfHLS_Nc_LIBS += RFCommon
llrfHLS_Nc_LIBS += llrfHlsAsyn
llrfHLS_Nc_LIBS += interlockRtmAsyn
llrfHLS_Nc_LIBS += llrfAmcAsyn

# LCLS1 style BSA
llrfHLS_Nc_LIBS += eventBsaSupport
llrfHLS_Nc_LIBS += BsaCore

# put asyn here to avoid link order issue
llrfHLS_Nc_LIBS += asyn

# Needed to link in iocAdmin support
llrfHLS_Nc_LIBS += devIocStats

# Needed to link in autosave support
llrfHLS_Nc_LIBS += autosave

# Needed to link caPutLog support
llrfHLS_Nc_LIBS += caPutLog

# Needed to link cexpsh() support
llrfHLS_Nc_LIBS += $(CEXP_LIBS)

# =====================================================
# Path to "NON EPICS" External PACKAGES: USER INCLUDES
#======================================================
USR_INCLUDES =  -I$(BOOST_INCLUDE) 
USR_INCLUDES += -I$(CPSW_FRAMEWORK_INCLUDE) 
USR_INCLUDES += -I$(YAML_INCLUDE) 
USR_INCLUDES += -I$(LLRFAMC_INCLUDE) 
USR_INCLUDES += -I$(YAMLREADER_INCLUDE) 
USR_INCLUDES += -I$(DEVICELIB_INCLUDE) 

# =====================================================

#======================================================
# PATH TO "NON EPICS" EXTERNAL PACKAGES: USER LIBRARIES
#======================================================
cpsw_DIR = $(CPSW_FRAMEWORK_LIB)
boost_system_DIR = $(BOOST_LIB)
yaml-cpp_DIR = $(YAML_LIB)
hpstpr_DIR = $(HPSTPR_LIB)
bsa_DIR = $(BSA_LIB)
commonATCA_DIR = $(COMMONATCA_LIB)
llrfHls_DIR = $(LLRFHLS_LIB)
commonRF_DIR = $(COMMONRF_LIB)
llrfAmc_DIR = $(LLRFAMC_LIB)
deviceLib_DIR = $(DEVICELIB_LIB)
yamlReader_DIR  = $(YAMLREADER_LIB)
# =====================================================

# ======================================================
# LINK "NON EPICS" EXTERNAL PACKAGE LIBRARIES STATICALLY
#=======================================================
USR_LIBS_Linux += cpsw
USR_LIBS_Linux += boost_system
USR_LIBS_Linux += yaml-cpp
USR_LIBS_Linux += hpstpr
USR_LIBS_Linux += commonATCA
USR_LIBS_Linux += commonRF
USR_LIBS_Linux += llrfHls
USR_LIBS_Linux += llrfAmc
USR_LIBS_Linux += yamlReader
USR_LIBS_Linux += deviceLib 
# ======================================================

# ===================================================
# Include Support for EPICS version 7 (old PVA API)
# Link QSRV (pvAccess Server) if available
# ===================================================
llrfHLS_Nc_LIBS += qsrv
llrfHLS_Nc_LIBS += $(EPICS_BASE_PVA_CORE_LIBS)
llrfHLS_Nc_DBD  += PVAServerRegister.dbd
llrfHLS_Nc_DBD  += qsrv.dbd
# ===================================================




llrfHLS_Nc_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE
