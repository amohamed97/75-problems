#!/bin/bash

# A script to quickly commit changes to the 75-problem file
git add -A
git commit -m "$1"
git push origin gh-pages
echo "Pushed successfully, Keep It Up"