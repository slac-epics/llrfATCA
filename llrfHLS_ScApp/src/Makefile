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
 PROD_IOC = llrfHLS_Sc
endif


# llrfHLS_Sc.dbd will be created and installed
DBD += llrfHLS_Sc.dbd

# llrfHLS_Sc.dbd will be made up from these files:
llrfHLS_Sc_DBD += base.dbd
llrfHLS_Sc_DBD += asyn.dbd
llrfHLS_Sc_DBD += yamlLoader.dbd
llrfHLS_Sc_DBD += yamlDownloader.dbd
llrfHLS_Sc_DBD += devIocStats.dbd
llrfHLS_Sc_DBD += asSupport.dbd
llrfHLS_Sc_DBD += caPutLog.dbd
llrfHLS_Sc_DBD += $(CEXP_DBDS)
llrfHLS_Sc_DBD += crossbarControl.dbd
llrfHLS_Sc_DBD += tprTriggerAsynDriver.dbd
llrfHLS_Sc_DBD += bsaAsynDriver.dbd
llrfHLS_Sc_DBD += RFCommon.dbd
llrfHLS_Sc_DBD += ATCACommon.dbd
llrfHLS_Sc_DBD += llrfHlsAsynDriver.dbd
llrfHLS_Sc_DBD += interlockRtmAsyn.dbd
llrfHLS_Sc_DBD += timeAxisGenerator.dbd
llrfHLS_Sc_DBD += llrfAmcAsyn.dbd

# ================================================================================
# The system command will be mainly used by linux hosted IOCs
# Very useful for changing kernel thread priorities for kernel drivers
# ================================================================================
llrfHLS_Sc_DBD += system.dbd

# ======================================================================
# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
llrfHLS_Sc_SRCS += llrfHLS_Sc_registerRecordDeviceDriver.cpp

llrfHLS_Sc_SRCS_DEFAULT += llrfHLS_ScMain.cpp

llrfHLS_Sc_SRCS_vxWorks += -nil-

# ========================================================================
# ========================================================================
# Add locally compiled object code
# For example, subroutines
# ========================================================================
#llrfHLS_Sc_SRCS +=

# =====================================================
# Link in the code from other libraries
# =====================================================
llrfHLS_Sc_LIBS += yamlLoader
llrfHLS_Sc_LIBS += yamlDownloader
llrfHLS_Sc_LIBS += tprTrigger
llrfHLS_Sc_LIBS += bsaDriver
llrfHLS_Sc_LIBS += ATCACommon
llrfHLS_Sc_LIBS += RFCommon
llrfHLS_Sc_LIBS += llrfHlsAsyn
llrfHLS_Sc_LIBS += interlockRtmAsyn
llrfHLS_Sc_LIBS += llrfAmcAsyn

# put asyn here to avoid link order issue
llrfHLS_Sc_LIBS += asyn

# Needed to link in iocAdmin support
llrfHLS_Sc_LIBS += devIocStats

# Needed to link in autosave support
llrfHLS_Sc_LIBS += autosave

# Needed to link caPutLog support
llrfHLS_Sc_LIBS += caPutLog

# Needed to link cexpsh() support
llrfHLS_Sc_LIBS += $(CEXP_LIBS)


llrfHLS_Sc_LIBS += dummyBsaCore_SC


# =====================================================
# Path to "NON EPICS" External PACKAGES: USER INCLUDES
#======================================================
USR_INCLUDES =  -I$(BOOST_INCLUDE) 
USR_INCLUDES += -I$(CPSW_FRAMEWORK_INCLUDE) 
USR_INCLUDES += -I$(BSA_INCLUDE)
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
bsa_DIR =  $(BSA_LIB)
yaml-cpp_DIR = $(YAML_LIB)
hpstpr_DIR = $(HPSTPR_LIB)
commonATCA_DIR = $(COMMONATCA_LIB)
llrfHls_DIR = $(LLRFHLS_LIB)
commonRF_DIR = $(COMMONRF_LIB)
llrfAmc_DIR = $(LLRFAMC_LIB)
deviceLib_DIR = $(DEVICELIB_LIB)
yamlReader_DIR  = $(YAMLREADER_LIB)
jitterCleaner_DIR = $(JITTERCLEANER_LIB)
# =====================================================

# ======================================================
# LINK "NON EPICS" EXTERNAL PACKAGE LIBRARIES STATICALLY
#=======================================================
USR_LIBS_Linux += cpsw
USR_LIBS_Linux += boost_system
USR_LIBS_Linux += yaml-cpp
USR_LIBS_Linux += bsa
USR_LIBS_Linux += hpstpr
USR_LIBS_Linux += commonATCA
USR_LIBS_Linux += commonRF
USR_LIBS_Linux += llrfHls
USR_LIBS_Linux += llrfAmc
USR_LIBS_Linux += yamlReader
USR_LIBS_Linux += deviceLib 
# ======================================================


# ===========================================
# EPICS 7 PVXS support (new PVA API)
# Order of the two libraries is important:
# ===========================================
llrfHLS_Sc_LIBS += pvxsIoc
llrfHLS_Sc_LIBS += pvxs
llrfHLS_Sc_DBD  += pvxsIoc.dbd
# ===========================================

# ===================================================
# Include Support for EPICS version 7 (old PVA API)
# Link QSRV (pvAccess Server) if available
# ===================================================
llrfHLS_Sc_LIBS += qsrv
llrfHLS_Sc_LIBS += $(EPICS_BASE_PVA_CORE_LIBS)
llrfHLS_Sc_DBD  += PVAServerRegister.dbd
llrfHLS_Sc_DBD  += qsrv.dbd
# ===================================================




llrfHLS_Sc_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE
