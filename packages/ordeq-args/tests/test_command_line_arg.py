
import sys
from unittest.mock import patch


from ordeq import node, run




def test_it_loads():
    with patch.object(sys, "argv", ["sth", "--name", "Barend"]):
        arg = CommandLineArg("--name").load()
        assert arg == "Barend"


def test_it_loads_int():
    with patch.object(sys, "argv", ["sth", "--num", "4"]):

        assert arg == 4


def test_it_loads_only_known_arg():
    with patch.object(sys, "argv", ["sth", "--name", "Barend", "--num", "4"]):

        assert arg == 4


def test_it_loads_flag():
    with patch.object(sys, "argv", ["sth", "-n", "4"]):

        assert arg == 4


def test_it_loads_positional_arg():
    with patch.object(sys, "argv", ["sth", "4"]):

        assert arg == 4



































        run(n)

















            run(n)








