#!/usr/bin/env python3

import sys
import argparse
from unidiff import PatchSet

parser = argparse.ArgumentParser("annotate-diff")
parser.add_argument('--severity', default='error', help='severity of diff annotations')
args = parser.parse_args()

diff = sys.stdin.read()
patch = PatchSet(diff)

for file in patch:
    for hunk in file:
        filename = file.source_file.lstrip('a/')
        print(f'::{args.severity} title=LintMismatch,file={filename},line={hunk.source_start},endLine={hunk.source_start+hunk.source_length-1}::{str(hunk).replace("\n","%0A")}')
