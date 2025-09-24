










    def load(self, hello: str = "Hello") -> str:


    def save(self, data: str, hello: str = "Hello") -> None:



# Load:

# No kwarg:
print(example_input.load())
# Alternative kwarg:
print(example_input.load(hello="Hello there"))


# No kwarg, with load options:
print(with_load_options.load())
# Alternative kwarg, with load options:
print(with_load_options.load(hello="Hi"))
print(type(with_load_options))

# Save:

# No kwarg:
example_output.save("world.txt@L2: Hello world!", hello="Hello")
# Alternative kwarg:
example_output.save("world.txt@L2: Guten tag world!", hello="Guten tag")


# No kwarg, with save options:

# Alternative kwarg, with save options:
with_save_options.save("world.txt@L2: Hi world!", hello="Hi")
print(type(with_save_options))
