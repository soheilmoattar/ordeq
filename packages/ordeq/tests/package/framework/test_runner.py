import copy




from ordeq.framework.graph import NodeGraph
from ordeq.framework.runner import _run_graph, _run_node, run


A, B, D = [StringBuffer(c) for c in "ABD"]
C = StringBuffer()
E = StringBuffer()
F = StringBuffer()


def test_run_regular_node():
    Bp = copy.copy(B)
    Bp.unpersist()
    node = Node(inputs=(A,), outputs=(Bp,), func=lambda x: x + x)
    computed = _run_node(node, hooks=())
    assert computed[Bp] == "AA"


def test_run_node_returns_none():
    node = Node(inputs=(A,), outputs=(), func=lambda _: None)
    computed = _run_node(node, hooks=())
    assert computed == {}


def test_run_node_with_zero_inputs():
    Bp = copy.copy(B)
    Bp.unpersist()
    node = Node(inputs=(), outputs=(Bp,), func=lambda: "something")
    loaded = {Bp: "something"}
    computed = _run_node(node, hooks=())
    assert loaded == computed


def test_run_node_with_zero_inputs_and_outputs():
    node = Node(inputs=(), outputs=(), func=lambda: print("Hello!"))
    loaded = {}
    computed = _run_node(node, hooks=())





















            {C: "A + BAAsomething", E: "A + BAAsomething - D"},

        ([get_node(plus)], {C: "A + BAAsomething"}),


def test_run_graph(nodes, expected_data_store):
    data_store = _run_graph(NodeGraph.from_nodes(nodes))














        ((plus, minus), {C: "A + BAAsomething", E: "A + BAAsomething - D"}),
        ((plus,), {C: "A + BAAsomething"}),


def test_run_parametrized(nodes, expected_data_store):
    data_store = run(*nodes)

