# TSPF Reference Implementation
# Copyright (c) 2025 QSymbolic LLC
# Non-Commercial Research License – see LICENSE.md

def entangle(r1, r2):
    r1.entangled.add(r2)
    r2.entangled.add(r1)
