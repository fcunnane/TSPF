class TriangleRegister:
    def __init__(self, name, a, b, C, state="Δ"):
        self.name = name
        self.a = a
        self.b = b
        self.C = C
        self.state = state
        self.phase = None
        self.entangled = set()
        self.collapsed = False

    def set_phase(self, theta):
        self.phase = theta

    def __repr__(self):
        return f"<TriangleRegister {self.name}: state={self.state}, phase={self.phase}, collapsed={self.collapsed}>"
