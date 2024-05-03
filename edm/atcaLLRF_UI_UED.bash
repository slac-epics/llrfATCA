read -p 'BLD: ' BLD
read -p 'RF: ' RF
read -p 'INST: ' INST

source /afs/slac/g/lcls/epics/setup/epicsenv-7.0.3.1-1.0.bash
source /afs/slac/g/lcls/package/pydm/use_pydm.bash
#export PYTHONPATH=/u/re/slepicka/development/sandbox/git-slaclab/pydm-git:$PYTHONPATH
export EPICS_IOC_TOP=/afs/slac/g/acctest/epics/iocTop/R3-14-12

LLRF_HLS_VERSION=R3.0.1-br

pydm --version 
#pydm -m "DEVICE=SIOC:B${BLD}:RF${RF}:${INST}, RTM=SIOC:B${BLD}:RF${RF}:${INST}, LOCA=B${BLD}, IOC_UNIT=RF${RF},INST=${INST}" \
#    --stylesheet $TOOLS/pydm/stylesheet/default.qss \
#    --stylesheet ${EPICS_IOC_TOP}/llrf_hls/${LLRF_HLS_VERSION}/pydm/llrf.qss \
#    ${EPICS_IOC_TOP}/llrf_hls/${LLRF_HLS_VERSION}/pydm/atcaLLRF.py &

#pydm -m "DEV=SIOC:B${BLD}:RF${RF}:${INST}, LOCA=B${BLD}, IOC_UNIT=RF${RF},INST=${INST}" \
#    --stylesheet $TOOLS/pydm/stylesheet/default.qss \
#    --stylesheet ${EPICS_IOC_TOP}/Klystron/${LLRF_HLS_VERSION}/pydm/llrf.qss \
#    ${EPICS_IOC_TOP}/Klystron/${LLRF_HLS_VERSION}/pydm/atcaLLRF.py &

pydm -m "DEV=SIOC:AS${BLD}:KY${RF}:${INST}, LOCA=AS${BLD}, IOC_UNIT=KY${RF}, INST=${INST}" \
    --stylesheet $TOOLS/pydm/stylesheet/default.qss \
    --stylesheet ${EPICS_IOC_TOP}/llrf_hls/${LLRF_HLS_VERSION}/pydm/llrf.qss \
    ${EPICS_IOC_TOP}/llrf_hls/${LLRF_HLS_VERSION}/pydm/atcaLLRF.py &
