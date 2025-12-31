def entangle(r1, r2):
    r1.entangled.add(r2)
    r2.entangled.add(r1)
