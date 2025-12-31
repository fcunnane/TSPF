# TSPF Reference Implementation
# Copyright (c) 2025 QSymbolic LLC
# Non-Commercial Research License – see LICENSE.md

from tspf import TriangleRegister, branch_on_ambiguity, collapse
t = TriangleRegister("T",5,5,90)
branches = branch_on_ambiguity(t)
for k,b in branches.items():
    print(k,b)
collapse(t)
print("Committed:",t)
