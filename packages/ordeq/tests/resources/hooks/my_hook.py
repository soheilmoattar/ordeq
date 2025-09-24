
from ordeq.framework import get_node





        self, op: Output[str], data: str

        print(f"saving data `{data}` to output `{op}`")














untyped_hook.before_output_save(StringBuffer("A"), "hello")


fixed_output_hook.before_node_run(get_node(func))
fixed_output_hook.before_output_save(StringBuffer("B"), "world")
