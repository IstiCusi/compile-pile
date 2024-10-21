# Done by Stephan Strauss in 2024 to transfer later to Manim for a teaching video

from automata.fa.dfa import DFA
from manim import (
    RED,
    WHITE,
    AnimationGroup,
    Create,
    Graph,
    Mobject,
    Scene,
    Text,
    VGroup,
)


class DFAAnimation(Scene):
    """
    Animates the graph traversal of a regular expression by showing its DFA
    """

    def calc_edges(self):
        """
        Calculates the Edges (the Delta function) in shape S x Sigma x S (f, z, t)
        """
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
        self.dfa = dfa

        nodes_wo_loops = list(dfa.states)

        edges_wo_loops = [
            (u, symbol, v)
            for u in dfa.transitions
            for symbol in dfa.transitions[u]
            for v in [dfa.transitions[u][symbol]]
            if u != v
        ]

        return (nodes_wo_loops, edges_wo_loops)

    def construct(self):

        nodes_wo_loops, edges_wo_loops = self.calc_edges()
        graph = Graph(
            nodes_wo_loops,
            edges=[(u, v) for u, _, v in edges_wo_loops],
            layout="kamada_kawai",
            labels=True,
        )
        self.add(graph)

        self.play(Create(graph))
        self.wait(5)

        q0_vertex: Mobject = graph.vertices["q0"]
        # self.play(q0_vertex.animate.set_color(RED))
        # label_q0 = labels_dict["q0"]
        label_q0 = graph._labels["q0"]
        # label_q0 = graph["q0"]
        # self.play(label_q0.animate.set_color(WHITE))

        self.play(
            AnimationGroup(
                q0_vertex.animate.set_color(RED),
                label_q0.animate.set_color(WHITE),
            )
        )
        # labels = VGroup(*labels_dict.values())
        # self.bring_to_front(labels)
