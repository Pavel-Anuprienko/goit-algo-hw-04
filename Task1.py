

def total_salary(path: str) -> tuple[int,float]:
    """Calculates the total and average salary of developers from a file.

    :param path: path to a text file containing records in the format 'str ,salary'
    :return: tuple (total, average)"""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []

            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    _, salary_str = line.split(',')
                    salaries.append(int(salary_str))
                except ValueError:
                    print(f"Incorect line, skipping: {line}")

            if not salaries:
                return 0, 0.0

            total = sum(salaries)
            average = total / len(salaries)
            return total, average

    except FileNotFoundError:
        print(f"Error: file {path} not found")
        return 0, 0.0
    except Exception as e:
        print(f"Error: can't process file: {e}")
        return 0, 0.0











if __name__ == "__main__":
    total, average = total_salary("salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    print(total_salary("nonexistingfile.txt"))
    print(total_salary("wrongline.txt"))