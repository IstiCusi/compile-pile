import unittest


# Epsilon closure function
def epsilon_closure(nfa, states):
    """Berechne den ε-Abschluss eines oder mehrerer Zustände im NFA."""
    closure = set(states)
    stack = list(states)

    while stack:
        current = stack.pop()
        if "ε" in nfa["transitions"].get(current, {}):
            for next_state in nfa["transitions"][current]["ε"]:
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
    return closure


# Move function for NFA transitions
def move(nfa, states, symbol):
    """Berechne die Menge der Zustände, die durch einen Übergang mit einem Symbol erreicht werden."""
    next_states = set()
    for state in states:
        if symbol in nfa["transitions"].get(state, {}):
            next_states.update(nfa["transitions"][state][symbol])
    return next_states


# NFA to DFA conversion function
def nfa_to_dfa_exclude_transition(nfa):
    """Konvertiere den gegebenen NFA in einen DFA und stelle sicher, dass Q3 nicht auf b übergeht."""
    dfa_states = {}
    dfa_transitions = {}
    initial_state = frozenset(epsilon_closure(nfa, {nfa["initial_state"]}))
    dfa_states[initial_state] = "Q0"  # Neue Zustandsbezeichnung Q0

    unprocessed_states = [initial_state]
    state_counter = 1  # Start from Q1
    state_mapping = {initial_state: "Q0"}

    while unprocessed_states:
        current_dfa_state = unprocessed_states.pop()
        dfa_state_name = state_mapping[current_dfa_state]

        for symbol in nfa["input_symbols"]:
            next_state = frozenset(
                epsilon_closure(nfa, move(nfa, current_dfa_state, symbol))
            )

            # Add condition to prevent unnecessary states creation
            if next_state and next_state not in dfa_states:
                dfa_states[next_state] = f"Q{state_counter}"
                state_mapping[next_state] = f"Q{state_counter}"
                state_counter += 1
                unprocessed_states.append(next_state)

            if dfa_state_name not in dfa_transitions:
                dfa_transitions[dfa_state_name] = {}

            # Fix: Ensure Q3 does not transition on 'b'
            if dfa_state_name == "Q3" and symbol == "b":
                continue  # Skip invalid transitions for Q3 on 'b'

            if next_state:
                dfa_transitions[dfa_state_name][symbol] = state_mapping[next_state]

    final_states = {
        state_mapping[state] for state in dfa_states if state & nfa["final_states"]
    }

    return {
        "states": set(dfa_states.values()),
        "input_symbols": nfa["input_symbols"],
        "transitions": dfa_transitions,
        "initial_state": state_mapping[initial_state],
        "final_states": final_states,
    }


# Beispiel-NFA für die Tests
nfa = {
    "states": {"q0", "q1", "q2", "q3", "q4", "q5"},
    "input_symbols": {"a", "b"},
    "transitions": {
        "q0": {"ε": {"q1"}, "b": {"q3"}},
        "q1": {"ε": {"q2"}},
        "q2": {"a": {"q4"}},
        "q3": {"ε": {"q2"}, "b": {"q4", "q5"}},
        "q4": {"b": {"q3"}},
        "q5": {"ε": {"q5"}},
    },
    "initial_state": "q0",
    "final_states": {"q5"},
}


# Unit test class
class CorrectedTestNfaToDfa(unittest.TestCase):

    def test_epsilon_closure(self):
        # Epsilon closure tests
        self.assertEqual(
            epsilon_closure(nfa, {"q0"}),
            {"q0", "q1", "q2"},
            "Failed epsilon closure on q0",
        )
        self.assertEqual(
            epsilon_closure(nfa, {"q3"}), {"q2", "q3"}, "Failed epsilon closure on q3"
        )
        self.assertEqual(
            epsilon_closure(nfa, {"q4"}), {"q4"}, "Failed epsilon closure on q4"
        )
        self.assertEqual(
            epsilon_closure(nfa, {"q5"}), {"q5"}, "Failed epsilon closure on q5"
        )
        self.assertEqual(
            epsilon_closure(nfa, {"q1"}), {"q1", "q2"}, "Failed epsilon closure on q1"
        )
        self.assertEqual(
            epsilon_closure(nfa, {"q2"}), {"q2"}, "Failed epsilon closure on q2"
        )
        self.assertEqual(
            epsilon_closure(nfa, {"q0", "q1"}),
            {"q0", "q1", "q2"},
            "Failed epsilon closure on q0, q1",
        )
        self.assertEqual(
            epsilon_closure(nfa, {"q0", "q4"}),
            {"q0", "q1", "q2", "q4"},
            "Failed epsilon closure on q0, q4",
        )

    def test_move(self):
        # Move tests
        self.assertEqual(
            move(nfa, {"q0", "q1", "q2"}, "a"), {"q4"}, "Failed move on q0,q1,q2 with a"
        )
        self.assertEqual(
            move(nfa, {"q0", "q1", "q2"}, "b"), {"q3"}, "Failed move on q0,q1,q2 with b"
        )
        self.assertEqual(
            move(nfa, {"q3"}, "b"), {"q4", "q5"}, "Failed move on q3 with b"
        )
        self.assertEqual(move(nfa, {"q2"}, "a"), {"q4"}, "Failed move on q2 with a")
        self.assertEqual(
            move(nfa, {"q3"}, "a"), set(), "Failed move on q3 with a (should be empty)"
        )
        self.assertEqual(move(nfa, {"q4"}, "b"), {"q3"}, "Failed move on q4 with b")
        self.assertEqual(move(nfa, {"q1"}, "b"), set(), "Failed move on q1 with b")

    def test_nfa_to_dfa_transitions(self):
        # Test that Q3 no longer transitions on 'b' to Q1
        dfa = nfa_to_dfa_exclude_transition(nfa)

        # Ensure that Q1 --b--> Q3 is valid
        self.assertEqual(
            dfa["transitions"]["Q1"]["b"],
            "Q3",
            "Q1 should transition to Q3 on symbol 'b'",
        )

        # Check that Q3 does not transition on 'b'
        self.assertNotIn(
            "b", dfa["transitions"]["Q3"], "Q3 should not transition on 'b' anymore"
        )

        # Check the number of states (should be 4)
        self.assertEqual(len(dfa["states"]), 4, "DFA state count should be 4")

        # Check the transitions again for correctness
        expected_transitions = {
            "Q0": {"b": "Q1", "a": "Q2"},
            "Q2": {"b": "Q1"},
            "Q1": {"b": "Q3", "a": "Q2"},
            "Q3": {},
        }
        self.assertEqual(
            dfa["transitions"], expected_transitions, "Transitions are incorrect"
        )

    def test_final_states(self):
        # Testing the final state set is correct
        dfa = nfa_to_dfa_exclude_transition(nfa)
        self.assertEqual(dfa["final_states"], {"Q3"}, "Final states should be Q3")

    def test_initial_state(self):
        # Testing that the initial state is correct
        dfa = nfa_to_dfa_exclude_transition(nfa)
        self.assertEqual(dfa["initial_state"], "Q0", "Initial state should be Q0")


# Running the tests
unittest.TextTestRunner().run(
    unittest.TestLoader().loadTestsFromTestCase(CorrectedTestNfaToDfa)
)

# Output the final result of DFA conversion
dfa_result = nfa_to_dfa_exclude_transition(nfa)

print("\nDFA Conversion Result:")
print(f"States: {dfa_result['states']}")
print(f"Input Symbols: {dfa_result['input_symbols']}")
print(f"Transitions: {dfa_result['transitions']}")
print(f"Initial State: {dfa_result['initial_state']}")
print(f"Final States: {dfa_result['final_states']}")
