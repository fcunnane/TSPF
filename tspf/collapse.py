from tspf.errors import CollapseError

def collapse(register, solver=None):
    if register.collapsed:
        raise CollapseError("Register already collapsed")
    if solver:
        solver.check_collapse_allowed(register)
    register.state = 0
    register.collapsed = True
    for other in register.entangled:
        if other.state == "Δ":
            other.state = register.state
