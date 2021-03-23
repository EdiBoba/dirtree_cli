class ExistError(Exception):
    def __init__(self, operation, path, element):
        super().__init__(
            f"Cannot {operation} {path} - {element} already exist"
        )


class NotExistError(Exception):
    def __init__(self, operation, path, element):
        super().__init__(
            f"Cannot {operation} {path} - {element} doesn't exist"
        )
