#!/bin/bash

# Define colors for output
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Compile the C++ file
echo -e "${GREEN}Compiling Module_1.cpp...${NC}"
clang++ -std=c++17 -o Module_1 Module_1.cpp

# Check if compilation was successful
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Compilation successful. Running program:${NC}"
    echo -e "${GREEN}----------------------------------------${NC}"
    # Run the program
    ./Module_1
else
    echo "Compilation failed. Please fix the errors and try again."
fi