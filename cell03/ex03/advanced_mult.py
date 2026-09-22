#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print("none")
    sys.exit()
    
i = 0
while i <= 10:
    j = 0
    while j <= 10:
        print(f"{i} x {j} = {i * j}")
        j += 1
    i += 1
