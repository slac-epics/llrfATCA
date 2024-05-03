TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application
ifeq ($(T_A),rhel6-x86_64)
	PROD_IOC = soft
endif
#PROD_IOC = soft

# soft.dbd will be created and installed
DBD += soft.dbd

# soft.dbd will be made up from these files:
soft_DBD += base.dbd

# Include dbd files from all support applications:
#soft_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#soft_LIBS += xxx

# soft_registerRecordDeviceDriver.cpp derives from soft.dbd
soft_SRCS += soft_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
soft_SRCS_DEFAULT += softMain.cpp
soft_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#soft_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
soft_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

