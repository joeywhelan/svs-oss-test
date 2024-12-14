# Fusion Demo

## Contents
1.  [Summary](#summary)
2.  [Prerequisites](#prerequisites)
3.  [Installation](#installation)
4.  [Usage](#usage)


## Summary <a name="summary"></a>
Test script of the open-source Intel SVS lib.  

## Prerequisites <a name="prerequisites"></a>
- python3
- pip

## Installation <a name="installation"></a>
```bash
git clone git@github.com:joeywhelan/svs-oss-test.git && cd svs-oss-test.git
git clone https://github.com/intel/ScalableVectorSearch && cd ScalableVectorSearch && pip install bindings/python && cd -
```
- Rename .env_sample to .env and replace the placeholder in API_KEY with your key.

## Usage <a name="usage"></a>
```bash
python3 test.py
```