# TSPF Reference Implementation
# Copyright (c) 2025 QSymbolic LLC
# Non-Commercial Research License – see LICENSE.md

from tspf import TriangleRegister, entangle, collapse
t1 = TriangleRegister("T1",3,4,60)
t2 = TriangleRegister("T2",4,5,45)
entangle(t1,t2)
collapse(t1)
print(t1)
print(t2)
