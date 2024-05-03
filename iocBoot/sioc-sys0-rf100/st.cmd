#!../../bin/rhel6-x86_64/soft

#- You may have to change soft to something else
#- everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/soft.dbd"
soft_registerRecordDeviceDriver pdbbase

## Load record instances
#dbLoadRecords("db/xxx.db","user=ktkim")

dbLoadRecords("db/middle_man.db", "PV_NAME=SIOC:B15:RF02:0:VCODAC,INP=SIOC:B15:RF02:0:STR0:STREAM_SLOWSHORT3.\[-1\],SCAN=Passive")
dbLoadRecords("db/middle_man.db", "PV_NAME=SIOC:B15:RF03:0:VCODAC,INP=SIOC:B15:RF03:0:STR0:STREAM_SLOWSHORT3.\[-1\],SCAN=Passive")
#dbLoadRecords("db/middle_man.db", "PV_NAME=SIOC:B15:RF13:0:VCODAC,INP=SIOC:B15:RF13:0:STR0:STREAM_SLOWSHORT3.\[-1\],SCAN=Passive")
dbLoadRecords("db/middle_man.db", "PV_NAME=SIOC:B084:RF54:0:VCODAC,INP=SIOC:B084:RF54:0:STR0:STREAM_SLOWSHORT3.\[-1\],SCAN=Passive")

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=ktkim"
