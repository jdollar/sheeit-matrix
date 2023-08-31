#!/usr/bin/env bash

project_dir=$(git rev-parse --show-toplevel)
pyinstaller --onefile $project_dir/src/templater.py

mkdir -p $project_dir/dist/templater_linux
cp $project_dir/dist/templater $project_dir/dist/templater_linux/
cp $project_dir/default.html.j2 $project_dir/dist/templater_linux/

(cd $project_dir/dist/templater_linux && zip -r templater_linux.zip .)
