import sys
import re

for _ in range(3):
    line = sys.stdin.readline()
    print(f"Hm... {line}", file=sys.stderr)
    if not re.match(r"(0|([1-9][0-9]*))\n", line):
        sys.exit(43)
    try:
        x = int(line)

        if not 0 <= x <= 1000:
            sys.exit(43)
    except ValueError:
        sys.exit(43)

if sys.stdin.readline() != "":
    sys.exit(43)
sys.exit(42)
