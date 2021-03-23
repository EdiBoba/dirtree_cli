from .command_dispatcher import CommandDispatcher


def main():
    dispatcher = CommandDispatcher()
    print("RUN DirTree CLI. (Press CTRL+C to quit)")
    while True:
        command = input(">>> ")
        if command:
            try:
                result = dispatcher.execute(command)
                if result:
                    print(result)
            except Exception as exc:
                print(exc)
