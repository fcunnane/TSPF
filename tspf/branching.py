import copy

def branch_on_ambiguity(register):
    if register.state != "Δ":
        raise ValueError("Branching only allowed on ambiguous state")
    return {"branch_A": copy.deepcopy(register), "branch_B": copy.deepcopy(register)}
