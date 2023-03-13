# cscanner
A simple script to scan C files for vulnerable functions

------------------

## Installation
Download the zip file and extract it to a directory of your choice. Then run the `cscanner` file.

## Usage
`cscanner.py [-h] [-nh] path`
```
positional arguments:
  path             Path to the directory containing the C code to scan

optional arguments:
  -h, --help       show this help message and exit
  -nh, --noheader  don't scan header files
```
The script can also scan `.h` files by default. To disable this, use the `-nh` flag.

## Notes
Please note that this project is still in development and is not yet complete. It is not recommended to use this script on any code that you do not have permission to scan.
This tool is indended to be used for educational purposes only (for example in CTFs). The author is not responsible for any damage caused by this tool.