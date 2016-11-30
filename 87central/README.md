# 8/7 Central
## Description
This python script contains functions that deal with datetime calculation, mostly
for Central Standard Time (PST). The script contains the following functions,

* on_hour_early - return one hour eariler than the current input time
* is_centeral_time - determine if current operation system time is centernal time or not
* to_calendar_format - return an input time IOS 8601 format in UTC

## Language
Python is a language as choose.

## Libraries Use

    appnope==0.1.0
    backports.shutil-get-terminal-size==1.0.0
    decorator==4.0.10
    enum34==1.1.6
    ipython==5.1.0
    ipython-genutils==0.1.0
    pathlib2==2.1.0
    pexpect==4.2.1
    pickleshare==0.7.4
    prompt-toolkit==1.0.9
    ptyprocess==0.5.1
    Pygments==2.1.3
    python-dateutil==2.6.0
    pytz==2016.7
    simplegeneric==0.8.1
    six==1.10.0
    traitlets==4.3.1
    tzlocal==1.3
    wcwidth==0.1.7

## Running A Python Script

* To run the python script, execute `python 87central.py`. This will output result to a console.
* To create a text file via running script, execute `python 87central.py > 87central.out.txt`.
  The result text file will be created at current directory

## Result
./87central.out.txt

## Source
./87central/87central.out.txt

## Development Tools

* vi as a primary editor
* ipython for experienmenting expression
* python -m pdb for debugging
