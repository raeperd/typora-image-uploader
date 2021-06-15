import argparse
from pathlib import Path
from typing import List


class TyporaArgumentParser:
    def __init__(self):
        self._parser = argparse.ArgumentParser()
        self._parser.add_argument("files", type=Path, nargs='*')

    def parse(self) -> List[Path]:
        return vars(self._parser.parse_args())['files']


if __name__ == '__main__':
    parser = TyporaArgumentParser()
    print(parser.parse())
