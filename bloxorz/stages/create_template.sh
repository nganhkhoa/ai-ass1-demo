#!/bin/bash

if [ "$#" -ne 1 ]; then
      echo '--- ./create_template.sh <stage number>'
      exit 1
fi


if [ -f stage$1.py ]; then
      echo '--- File already exists'
      exit 2
fi

echo '[+] Creating file from template'
sed s/_/$1/ < template.py > stage$1.py

echo '[+] Adding to __init__.py'
echo "from .stage$1 import stage$1" >> __init__.py

echo '[+] Completed'
echo '[+] Remember to update the GenStage.py maxlv file'