from galactic_description_logical_classic import BooleanDescription
from galactic_characteristic_logical import Bool
from galactic.algebras.lattice import *
from galactic.algebras.poset import HasseDiagram
from galactic.population import Population
from galactic.descriptions import Member
from galactic.concepts import ConceptLattice, Concept, ConceptRenderer
from galactic.strategies import *
from galactic.characteristics import *
from galactic.examples import *
from galactic.concepts import ConceptLattice
from galactic_strategy_logical_classic_basic import BooleanStrategy
# the data
data = {
0: ["c", "e", "s"],
1: ["o", "s"],
2: ["e", "p"],
3: ["o", "p"],
4: ["c", "e", "s"],
5: ["o", "p"],
6: ["c", "e"],
7: ["o", "p"],
8: ["c", "e"],
9: ["c", "o", "s"],
}
## creating a population from the data
population = Population(data)
## creating descriptions
descriptions = [
BooleanDescription(Bool(Member(name="c"))),
BooleanDescription(Bool(Member(name="e"))),
BooleanDescription(Bool(Member(name="o"))),
BooleanDescription(Bool(Member(name="p"))),
BooleanDescription(Bool(Member(name="s"))),
]
## creating a concept lattice based on the population and the descriptions
lattice = ConceptLattice(population, descriptions)
## using the stragtegies to generate the lattice
lattice.apply([
BooleanStrategy(Bool(Member(name="c"))),
BooleanStrategy(Bool(Member(name="e"))),
BooleanStrategy(Bool(Member(name="o"))),
BooleanStrategy(Bool(Member(name="p"))),
BooleanStrategy(Bool(Member(name="s"))),
])
## showing the hasse diagram
HasseDiagram(lattice, domain_renderer=ConceptRenderer())
