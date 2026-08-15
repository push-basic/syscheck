# Syscheck

A command-line utility for checking the health of a Linux system.

## What it does

`syscheck` performs a series of system checks and reports the results in the terminal.

Currently, it checks:

- Disk% used
- Memory usage
- Load
- If a website is reachable
- If a hostname can be resolved

## Requirements

- Python 3.12+
- Linux

## Installation

Clone the repository:

```
git clone https://github.com/push-basic/syscheck.git
cd syscheck/
```
Create and activate a virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
```

Install the project:

```
pip install -e .
```

## Usage
Run:
```
syscheck
```

## Running the tests
```
python3 -m unittest discover -s tests -v
```




