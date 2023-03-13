#!/usr/bin/env python3
import sys
import os
import pathlib
import argparse

def check_scanf(line, line_number):
    if "scanf" in line and "%s" in line:
        print("Function scanf not used properly on line", line_number, "in file", filename)
        print(line)
        return True
    return False

def check_printf(line, line_number):
    if "printf(" in line and '\"' not in line:
        print("Function printf not used properly on line", line_number, "in file", filename)
        print(line)
        return True
    return False

def check_strcpy(line, line_number):
    if("strcpy(" in line):
        #TODO: parse the strcpy argument in a better way
        second_arg = line.split(",")[1]
        # print(second_arg)
        if '\"' not in second_arg:
            print("Function strcpy not used properly on line", line_number, "in file", filename)
            print(line)
            return True
    return False

def scan(filename):
        # vulnerable functions
    vulnerable = {"gets", "strcat"}
    # print("Reading from file", filename)
    with open(filename, 'r') as f:
        # read each line keeping track of the line number
        try:
            for line_number, line in enumerate(f, 1):
                # print(line_number, line, end='')
                # check if the line contains a vulnerable function
                for vuln in vulnerable:
                    if vuln in line:
                        print("Potentially vulnerable function", vuln, "found on line", line_number, "in file", filename)
                        print(line)
                # check if the line contains a scanf
                check_scanf(line, line_number)
                # check if the line contains a printf
                check_printf(line, line_number)
                # check if the line contains a strcpy
                check_strcpy(line, line_number)
        except UnicodeDecodeError:
            # print("UnicodeDecodeError")
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated C code scanner to find potential vulnerabilities")
    parser.add_argument("path", help="Path to the directory containing the C code to scan")
    # parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("-nh", "--noheader", help="don't scan header files", action="store_true")
    args = parser.parse_args()

    path = pathlib.Path(args.path)
    # for each c file in path, recursively
    for filename in path.rglob("*.c"):
        scan(filename)
    
    # for each .h file in path, recursively
    if args.noheader is False:
        for filename in path.rglob("*.h"):
            scan(filename)
