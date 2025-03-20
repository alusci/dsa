def decorator_func(func):
    def wrapper_func(*args, **kwargs):
        print("Before execution")
        func(*args, **kwargs)
        print("After execution")

    return wrapper_func


@decorator_func
def foo(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    foo("Alessandro")

