import os


class EnvironmentVariables:
    def __init__(self, *args: str):
        for name in args:
            variable = os.getenv(name)

            if variable is None:
                raise KeyError(f'Missing important variable named {name}')

            object.__setattr__(self, name, variable)

    def __setattr__(self, *args) -> None:
        raise TypeError(__class__.__name__ + ' is immutable')

    def __delattr__(self, *args) -> None:
        raise TypeError(__class__.__name__ + ' is immutable')
            

if __name__ == '__main__':
    var = EnvironmentVariables('DATABASE_PORT')
    print(var.DATABASE_PORT)
    var.DATABASE_PORT = 123
    print(var.DATABASE_PORT)

