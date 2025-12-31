# Triangle Symbolic Processing Framework (TSPF)

**A Symbolic Front-End for Hybrid Quantum Systems — Without Quantum Physics**

TSPF is a **symbolic semantic framework** for reasoning about hybrid quantum–classical workflows.  
It captures the *logical structure* of quantum computation—uncertainty, correlation, phase, and measurement—using **purely classical symbolic semantics**.

This repository contains a **research reference implementation and toy artifact** corresponding to the paper:

> **A Symbolic Front-End for Hybrid Quantum Systems Without Quantum Physics**  
> Francis X. Cunnane III — QSymbolic Research

---

## Motivation

Modern quantum computing systems are inherently hybrid.  
While quantum hardware executes circuits, the *meaning* of those circuits—control flow, uncertainty management, measurement ordering, and policy constraints—is handled in classical software.

In most frameworks, this reasoning is:
- implicit
- scattered across host-language code
- difficult to audit or validate

**TSPF addresses this gap** by introducing an explicit *semantic layer* that models quantum-inspired ideas symbolically, without simulating quantum physics.

---

## Core Ideas

TSPF models **quantum ideas**, not quantum mechanics.

| Quantum Concept | TSPF Semantic Analog |
|----------------|----------------------|
| Superposition | Explicit ambiguity state `Δ` |
| Measurement | Irreversible collapse `COLΔ` |
| Entanglement | Declared symbolic correlation `ENT` |
| Phase | Symbolic coherence parameter `θ` |
| Branching | Ambiguity-driven symbolic paths |

These constructs:
- do **not** model amplitudes or noise
- do **not** claim computational speedup
- **do** make uncertainty and commitment explicit and inspectable

---

## Triangle Symbolic Registers

The fundamental unit of state in TSPF is a **triangle symbolic register**, defined by:

- Structural identity `(a, b, C)`  
- Symbolic state: `Δ` or a concrete value  
- Optional symbolic phase `θ`

The triangle representation provides:
- stable identity for symbolic state
- compositional structure for correlation graphs
- a uniform scaffold for constraint solving and branching

> The geometry is semantic, not physical.

---

## What This Repository Contains

This repository is a **research artifact**, not a production compiler.

### 📁 `tspf/`
Core symbolic primitives:
- triangle registers
- ambiguity (`Δ`) handling
- collapse semantics
- symbolic correlation graphs

### 📁 `examples/`
Toy examples demonstrating:
- ambiguity-driven branching
- symbolic correlation
- deferred collapse
- constraint-aware execution

### 📁 `solver/`
A lightweight constraint solver used to:
- prune infeasible symbolic branches
- enforce policy and ordering rules
- validate collapse admissibility

### 📁 `docs/`
Design notes and diagrams aligned with the paper.

---

## What TSPF Is *Not*

TSPF intentionally avoids:

- simulating quantum physics
- modeling noise or error correction
- replacing quantum programming languages
- claiming quantum advantage or speedup

It is **not** a competitor to:
- Qiskit
- Cirq
- OpenQASM
- PennyLane

Instead, it sits **above circuit description** and **below application orchestration**.

---

## Intended Use Cases

- Academic research on hybrid quantum semantics
- Symbolic reasoning about quantum workflows
- Constraint-aware orchestration of quantum backends
- Policy and trust-boundary enforcement
- Teaching quantum concepts without physics overhead
- Prototyping hybrid execution models

---

## Artifact Status

This is a **reference implementation / toy artifact** intended to:
- support peer review
- illustrate semantics
- validate conceptual feasibility

It is deliberately lightweight and abstract.

Future work may include:
- richer examples
- backend adapters
- empirical evaluation

---

## License

This repository is released under a **Non-Commercial Research License**.

✔ Allowed:
- academic research
- teaching
- evaluation
- prototyping
- non-commercial experimentation

✘ Not allowed without a separate license:
- commercial use
- deployment
- integration into products or services
- hardware implementation

See [`LICENSE.md`](./LICENSE.md) for full terms.

---

## Citation

If you use or reference this work, please cite:

