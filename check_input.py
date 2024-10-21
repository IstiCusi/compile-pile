# Done by Stephan Strauss in 2024 to tranfer later to Manum for a teaching video


from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA

dfa = DFA(
    states={"q0", "q3", "q4", "q5"},  # States
    input_symbols={"a", "b"},  # Alphabet
    transitions={
        "q0": {"a": "q4", "b": "q3"},
        "q4": {"a": "q4", "b": "q3"},
        "q3": {"a": "q4", "b": "q5"},
        "q5": {"a": "q5", "b": "q5"},
    },
    initial_state="q0",  # Initial state
    final_states={"q4", "q5"},  # Final states
)

nodes_wo_loops = list(dfa.states)

nodes = nodes_wo_loops.copy()
for state in dfa.states:
    if state in dfa.transitions and state in dfa.transitions[state].values():
        nodes.append(state + "_loop")

edges_wo_loops = [
    (u, symbol, v)
    for u in dfa.transitions
    for symbol in dfa.transitions[u]
    for v in [dfa.transitions[u][symbol]]
    if u != v
]

edges = [
    ((u, symbol, v) if u != v else (u, v + "_loop"))
    for u in dfa.transitions
    for symbol in dfa.transitions[u]
    for v in [dfa.transitions[u][symbol]]
]

# The edges represent the Delta Function representation of a transition table (as subset of S x Delta * S)

print(nodes)
print(edges)

print(nodes_wo_loops)
print(edges_wo_loops)

inputs = ["a", "ab", "abb"]

for input_str in inputs:
    if dfa.accepts_input(input_str):
        print(f'The input "{input_str}" is accepted.')
    else:
        print(f'The input "{input_str}" is not accepted.')
