# -*- coding: utf-8 -*-

import sys
import time

o = 0
for i in sys.argv[1:]:
    time.sleep(1.5)
    o += float(i)

print(o)

# exit(0)
