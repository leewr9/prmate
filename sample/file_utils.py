def read_file(filepath: str) -> str:
    try:
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return ""
    except IOError as e:
        print(f"Error reading file {filepath}: {e}")
        return ""

def write_file(filepath: str, content: str) -> None:
    try:
        with open(filepath, "w") as f:
            f.write(content)
    except IOError as e:
        print(f"Error writing to file {filepath}: {e}")


# def read_file(filepath: str) -> str:
#     try:
#         with open(filepath, "r") as f:
#             return f.read()
#     except FileNotFoundError:
#         print(f"File not found: {filepath}")
#         return ""
#     except IOError as e:
#         print(f"Error reading file {filepath}: {e}")
#         return ""
# 
# def write_file(filepath: str, content: str) -> None:
#     try:
#         with open(filepath, "w") as f:
#             f.write(content)
#     except IOError as e:
#         print(f"Error writing to file {filepath}: {e}")

