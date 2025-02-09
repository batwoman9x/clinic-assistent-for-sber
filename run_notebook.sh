#!/bin/bash

if [ -d '.venv' ]; then
  source .venv/bin/activate
  echo "Python Virtual env activated"
else
  python3 -m venv .venv
  source .venv/bin/activate
  echo "Python Virtual env create and activated"
fi
#curl -k "https://gu-st.ru/content/Other/doc/russian_trusted_root_ca.cer" -w "\n" >> $(python3 -m certifi)
pip3 install -U notebook
python3 -m notebook