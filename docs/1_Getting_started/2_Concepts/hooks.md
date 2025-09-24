




## Why hooks are useful

To see how hooks can be useful, let's consider the following example:

=== "nodes.py"
    ```python
    import catalog

    @node(
        inputs=catalog.names,
        outputs=catalog.greetings
    )
    def greet(names: tuple[str, ...]) -> list[str]:
        """Returns a greeting for each person."""
        greetings = []
        for name in names:
            greetings.append(f"Hello, {name}!")
        return greetings
    ```

=== "catalog.py"
    ```python
    from ordeq_files import CSV, Text
    from pathlib import Path

    names = CSV(path=Path("names.csv"))
    greetings = Text(path=Path("greetings.txt"))
    ```

As we learned [earlier][running-a-node], running the node `greet` is roughly equivalent to:

```pycon
>>> import catalog
>>> names = catalog.names.load()
>>> greetings = greet(names)
>>> catalog.greetings.save(greetings)
```

With hooks, you can inject custom logic around each step.
For example, you might want to log the time taken to load the input `names`:

```pycon hl_lines="2 3 5 6"
>>> import catalog
>>> import time
>>> start_time = time.time()
>>> names = catalog.names.load()
>>> end_time = time.time()
>>> print(f"Loading names took {end_time - start_time} seconds")
>>> greetings = greet(names)
>>> catalog.greetings.save(greetings)
```

As you can see, this custom logic adds a lot of boilerplate code around loading the input.
If you want to do this for every input, it quickly becomes tedious and error-prone.

Instead, you can use a hook to run this logic automatically around every input loading:

```python




class TimeHook(InputHook):

        self.start_time = time.time()


        end_time = time.time()
        print(f"Loading {io} took {end_time - self.start_time} seconds")
```

To ensure the hook is executed, it needs to be attached to the input:

=== "catalog.py"
    ```python
    from ordeq_files import CSV, Text
    from pathlib import Path

    names = CSV(
        path=Path("names.csv")
    ).with_input_hooks(TimeHook())
    greetings = Text(path=Path("greetings.txt"))
    ```

### Types of hooks
Ordeq provides three types of hooks:


- `NodeHook`: called around running a node
- `InputHook`: called around the loading of inputs
- `OutputHook`: called around the saving of outputs

The following diagram depicts how the hooks are applied by Ordeq:

```mermaid


































```

This page demonstrated the concept of hooks and discussed an elementary examples.
For a more elaborate guide, including details on how to implement your own hooks, see [Creating custom hooks][custom-hooks].


!!!success "Where to go from here?"
    - See how to create custom hooks in the [guide][custom-hooks]
    - Check out the [guide on testing nodes][testing-nodes]


[custom-hooks]: ../../2_Guides/custom_hooks.md
[testing-nodes]: ../../2_Guides/testing_nodes.md
[running-a-node]: ./_nodes.md#running-a-node
