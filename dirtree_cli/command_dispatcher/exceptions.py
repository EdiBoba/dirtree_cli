class UnknownCommandError(Exception):
    def __init__(self, command: str):
        super().__init__(
            f"ERROR: unknown command '{command}'"
        )
