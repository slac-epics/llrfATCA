# PyDM Engineering Screens

PyDM-based engineering screens for the LLRF_HLS project.

## Prerequisites
 * pydm

## Open display:
```
pydm -m "DEV=SIOC:B${BLD}:RF${RF}:${INST}, LOCA=B${BLD}, IOC_UNIT=RF${RF}, INST=${INST}" \
    atcaLLRF.py
```

Where:
- `BLD`: is the building number (for example: `084`, `34`, etc.)
- `RF`: is the RF station number (for example: `52`, `53`, etc.)
- `INST`: is the instance number (for example: `0`)
