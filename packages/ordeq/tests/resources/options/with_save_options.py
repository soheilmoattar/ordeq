






class ExampleOutputSaveKwarg(Output):



    def save(self, data: str, hello: str = "Guten tag") -> None:



example_output = ExampleOutputSaveKwarg(path=Path("hello.txt"), attribute="L1")
# No kwarg:
example_output.save("hello.txt@L1: Guten tag world!")
# Alternative kwarg:
example_output.save("hello.txt@L1: Bonjour world!", hello="Bonjour")



# No kwarg, with save options:

# Alternative kwarg, with save options:
with_options.save("hello.txt@L1: Buenos dias world!", hello="Buenos dias")



@dataclass(kw_only=True, frozen=True)
class ExampleOutputSaveArg(Output):
    path: Path
    attribute: str

    def save(self, data: str, hello: str = "Hello") -> None:
        assert data == f"{self.path}@{self.attribute}: {hello} world!"


example_input_arg = ExampleOutputSaveArg(path=Path("hello.txt"), attribute="L1")
example_input_arg.save("hello.txt@L1: Hello world!", "Hello")
print(type(example_input_arg))

with_options_arg = example_input_arg.with_save_options(hello="Hello")
# This should raise a type error,
# but still run as we fill the missing arg on save:
with_options_arg.save("hello.txt@L1: Hello world!")
# Alternative arg, with save options:
with_options_arg.save("hello.txt@L1: Hi world!", hello="Hi")
print(type(with_options_arg))

example_input_arg.with_save_options(unknown_kwarg="Hello")  # should error
