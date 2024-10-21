# DFA Conversion and Visualization

This repository contains sketches and exploratory work related to converting a Non-deterministic Finite Automaton (NFA) to a Deterministic Finite Automaton (DFA), along with visualization using **Manim**. These scripts were created as part of another project, and I am sharing them here for reference.
[Detailed Theory Explanation](./THEORY.md)

## Files in This Repository

- **`robin_scott.py`**:

  - This file contains Python functions to convert an NFA into a DFA using the epsilon-closure method.
  - It includes functions for:
    - **Epsilon Closure**: Calculates the epsilon closure for NFA states.
    - **Move Function**: Determines the set of states reached by a specific input symbol.
    - **NFA to DFA Conversion**: Converts a given NFA into a DFA by systematically handling the epsilon transitions and input symbols.
  - Unit tests for all major functions are included to verify correctness.

- **`show_graph_manim.py`**:

  - This file visualizes the structure of a DFA using **Manim**, a popular Python library for creating mathematical animations.
  - It uses the Kamada-Kawai layout to generate nodes and transitions and supports custom color animations for nodes and labels.
  - The script calculates DFA transitions and visualizes input strings passing through the DFA.

- **`check_input.py`**:
  - This script creates a DFA using the `automata.fa.dfa.DFA` class and visualizes it using `visual_automata.fa.dfa.VisualDFA`.
  - It also checks if various input strings are accepted by the DFA and prints the results.

## Installation and Setup

### Prerequisites

To run these scripts, you will need to install the following:

- **Python 3.7+**: Ensure you have a compatible version of Python.
- **Manim**: The `show_graph_manim.py` script uses Manim to animate the DFA. You can install Manim by following the [official installation guide](https://docs.manim.community/en/stable/installation.html).
- **Automata Library**: Used in `check_input.py` to define and manipulate finite automata.

  Install it via:

  ```bash
  pip install automata-lib
  ```

- **Visual Automata Library**: For DFA visualization in `check_input.py`.
  ```bash
  pip install visual_automata
  ```

### Running the Scripts

1. **DFA Conversion and Tests** (`robin_scott.py`):

   - Run this script to perform NFA to DFA conversion and execute the unit tests.

   ```bash
   python robin_scott.py
   ```

2. **DFA Visualization with Manim** (`show_graph_manim.py`):

   - To visualize the DFA with Manim, ensure Manim is installed and run the following command:

   ```bash
   manim -pql show_graph_manim.py
   ```

3. **Checking Input Strings** (`check_input.py`):
   - Run this script to check whether a set of input strings is accepted by the DFA:
   ```bash
   python check_input.py
   ```

## Unit Tests

- The unit tests in **`robin_scott.py`** verify the following:
  - Correct calculation of epsilon closures for various NFA states.
  - Proper state transitions based on input symbols.
  - Full NFA to DFA conversion.
- Example:
  ```bash
  python -m unittest robin_scott.py
  ```

## Next Steps

If you wish to expand this project, here are some potential next steps:

- **Enhanced Visualization**: Extend the Manim animation to support more complex automata, including NFAs and other state machine types.
- **Interactive Inputs**: Modify the `check_input.py` script to accept user input from the command line and visualize the DFA transitions based on this input.
- **Error Handling**: Add more sophisticated error handling and validation in the DFA/NFA creation process to ensure robustness.

This repository represents exploratory sketches and is open for further improvements and contributions.
