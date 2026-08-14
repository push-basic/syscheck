import argparse
from pathlib import Path

from .output import system_output



def main():
    parser = argparse.ArgumentParser(description="System health check utility")
    parser.add_argument("--json", help="json formatted ")
    args = parser.parse_args()

    system_path = Path("/")

    print(system_output(system_path))

if __name__ == "__main__":
    main()
