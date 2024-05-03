#!/usr/bin/env bash

read -p 'BLD: ' BLD
read -p 'RF: ' RF
read -p 'INST: ' INST

. $EPICS_SETUP/epicsenv-7.0.3.1-1.0.bash
. $TOOLS/script/use_pydm.sh

LLRF_HLS_VERSION=llrf_hls-git
LLRF_HLS_TOP=/u/gu/romero12/romero12/llrfhls/

pydm --version

PYDM_STYLESHEET_INCLUDE_DEFAULT=1 pydm -m "DEV=SIOC:B${BLD}:RF${RF}:${INST}, LOCA=B${BLD}, IOC_UNIT=RF${RF},INST=${INST}" \
    --stylesheet ${LLRF_HLS_TOP}/${LLRF_HLS_VERSION}/pydm/llrf.qss \
    ${LLRF_HLS_TOP}/${LLRF_HLS_VERSION}/pydm/atcaLLRF.py &
