#!/bin/bash

echo "installing dependencies..."
python --version &>/dev/null
if [ "$?" != "0" ]; then
    echo "please install python 2.7"
    exit 1
fi

pip --version &>/dev/null
if [ "$?" != "0" ]; then
    echo "please install pip for python 2.7"
    exit 1
fi

pip install -r requirements.txt &>/dev/null