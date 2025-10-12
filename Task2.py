

def get_cats_info(path: str) -> list[dict]:
    """
    Reads a file with data about cats and returns a list of dictionaries with information about each cat.

    :param path: path to a text file with data in the format 'id,name,age'
    :return: list of dictionaries [{"id": ..., "name": ..., "age": ...}, ...]"""
    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    cat_id, name, age = line.split(',')
                    cats.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    print(f"Incorect line, skipping: {line}")
                    continue

    except FileNotFoundError:
        print(f"Error: file {path} not found")
    except Exception as e:
        print(f"Error: can't process file: {e}")

    return cats


if __name__ == "__main__":
    cats_info = get_cats_info("cats.txt")
    print(cats_info)