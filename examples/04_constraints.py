# TSPF Reference Implementation
# Copyright (c) 2025 QSymbolic LLC
# Non-Commercial Research License – see LICENSE.md

from tspf import TriangleRegister, ConstraintSolver, collapse
solver = ConstraintSolver()
solver.add_rule("no_collapse_before_phase")
t = TriangleRegister("T",6,8,30)
try:
    collapse(t, solver)
except Exception as e:
    print("Blocked:", e)
t.set_phase(0.5)
collapse(t, solver)
print(t)
