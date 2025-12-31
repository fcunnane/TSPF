class ConstraintSolver:
    def __init__(self):
        self.rules = []
    def add_rule(self, rule):
        self.rules.append(rule)
    def check_collapse_allowed(self, register):
        if "no_collapse_before_phase" in self.rules and register.phase is None:
            raise Exception("Collapse forbidden before phase assignment")
