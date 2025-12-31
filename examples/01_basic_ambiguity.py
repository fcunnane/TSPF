# TSPF Reference Implementation
# Copyright (c) 2025 QSymbolic LLC
# Non-Commercial Research License – see LICENSE.md

from tspf import TriangleRegister, collapse
t = TriangleRegister("T",3,4,60)
print(t)
t.set_phase(0.25)
collapse(t)
print(t)
