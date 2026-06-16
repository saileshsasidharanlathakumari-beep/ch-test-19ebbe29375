#!/bin/bash

rm -rf temp_dependencies dependencies

if [ ! -s requirements.txt ]; then
    echo "No dependencies to install. Skipping..."
else
    mkdir -p temp_dependencies
    echo "Downloading dependencies..."
    pip3 download -r requirements.txt -d temp_dependencies
    pip3 install --target=dependencies/ temp_dependencies/*
fi