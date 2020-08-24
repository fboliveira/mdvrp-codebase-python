from Problem import Problem
from CommandLine import CommandLine
import sys

def main():
    c = CommandLine(sys.argv)
    c.run()

    problem = Problem(c.instance())
    problem.processInstanceFiles()
    problem.print()

if __name__ == "__main__":
    # execute only if run as a script
    main()
