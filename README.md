# logwatch

A CLI tool that reads a log file, parses it into structured data, analyses it, and outputs stats.

## Installation

```bash
git clone https://github.com/lukantozi/logwatch-py.git
cd logwatch
pip install -e .
```

## Usage

```bash
logwatch -f sample.log                        # analyse all levels, json output
logwatch -f sample.log -l ERROR               # only ERROR lines
logwatch -f sample.log -o report.json -m json # write json report to file
logwatch -f sample.log -o report.txt -m text  # write text report to file
```

## Flags

| Flag | Description | Default |
|------|-------------|---------|
| `-f` | Input log file (required) | — |
| `-l` | Filter by level: `INFO`, `ERROR`, `WARNING` | all levels |
| `-m` | Output mode: `json` or `text` | `json` |
| `-o` | Output file | `output.json` |

## Sample log format

```
2024-01-01 08:00:01 INFO service started
2024-01-01 08:01:03 ERROR disk read failed
2024-01-01 08:01:45 WARNING high memory usage
```

## Project structure

```
logwatch/
├── logwatch/
│   ├── __init__.py
│   ├── logwatch.py   # entry point + argparse
│   ├── parser.py     # file reading + line parsing
│   ├── analyser.py   # class-based analysis
│   └── report.py     # output formatting
├── README.md
├── sample.log
└── setup.py
```
