from ordeq import Input, InputHook, Node, Output, OutputHook, node, run




    def before_input_load(self, io: Input[str]) -> None:
        print("Before loading data from:", io)


        self, io: Input[str], data: str

        print("After loading data from:", io)




        self, io: Output[str], data: str

        print("Before saving data to:", io)


        self, io: Output[str], data: str

        print("After saving data to:", io)











run(node(hello_world, inputs=hooked_input, outputs=hooked_output))

