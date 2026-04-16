from .analyzer import LogAnalyzer, FilteredLogAnalyzer
from .report import write_report
from .parser import parse
import argparse


def main():
    par = argparse.ArgumentParser()
    par.add_argument("-f", help="Input filename", required=True)
    par.add_argument("-l", help="Level filter: [INFO|ERROR|WARNING]")
    par.add_argument("-m", help="Output mode: [text|json]", default="json")
    par.add_argument("-o", help="Output filename", default="output.json")
    args = par.parse_args()

    file = args.f
    level = args.l
    mode = args.m
    output = args.o

    logs = parse(file)
    if level:
        analyzed = FilteredLogAnalyzer(logs, level)
    else:
        analyzed = LogAnalyzer(logs)
    write_report(analyzed, output, mode)

if __name__ == "__main__":
    main()
