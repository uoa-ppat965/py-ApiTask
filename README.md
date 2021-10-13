# Pull Request Counter
The Pull request counter is an command line interface that can find the number of open pull requests of public a repository (repo) given repo name and owner name. The interface was created using python.
## Installation
To install the package ensure all files are located in the same folder. This code needs to be run in a python environment. The necessary tools/libraries that need to be downloaded is Requests which can be downloaded using the following instruction
```bash
python -m pip install requests
```
To ensure the code works correctly, in the python environment, ensure the current directory set to the folder location which can be done using cd with the folder path like the following,
```bash 
cd "C:\users\[Computer Name]\...\py-ApiTask"
```
Note: the cd instruction above is only valid for Windows and Mac systems.
## Usage
The counter can be run in a terminal with python using the following command (provided the above instructions were followed)
```bash 
python technicalTask.py
```
The command line interface would require the user to input a valid Github owner name and repo. The pull requests data can only be retreived for public repos.
## Acknowledgements
The ascii artwork was from the following source:


Author: "pi314", Link: "https://github.com/pi314/ascii-arts/blob/master/octocat.asciiart"

The ascii artwork was printed using code influenced from the following source:
Author: "learnlearn", Link: "https://learnlearn.uk/python/ascii-art/"

