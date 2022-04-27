from functools import cmp_to_key
"""
Пройтись по всем файлам в директории    +
Отфильтровать python файлы              +
Отсортировать импорты в каждом файле    

Modules:
    files_iterator      -   Модуль для прохождения по всем файлам директории и нахождения python файлов
    imports_formatter   -   Модуль для сортировки импортов в файле
    driver              -   Драйвер (собирает прогу и запускает) 
"""
def format(): 
    print("test from formatter")


def sort_imports(file: str) -> str:
    imports: tuple[list[str], ...] = get_imports(file)
    sorted_imports_list: list[list[str]] = [ [], [], [] ]
    sorted_imports_list[0] = sorted(imports[0], key=cmp_to_key(compare_imports), reverse=True)
    sorted_imports_list[1] = sorted(imports[1], key=cmp_to_key(compare_imports), reverse=True)
    sorted_imports_list[2] = imports[2]
    #return str(imports)
    #text: list[str] = ["\n".join(sorted_imports_list[0]), "\n".join(sorted_imports_list[1]), "\n".join(sorted_imports_list[2])]
    #return "".join(text)
    return "".join(sorted_imports_list[0]) + "".join(sorted_imports_list[1]) + "".join(sorted_imports_list[2])


def compare_imports(a: str, b: str) -> int:
    a = delete_import_keywords(a)
    b = delete_import_keywords(b)
    return cmp(a, b)


def cmp(a: str, b: str) -> bool:
    return 1 if a <= b else -1


def delete_import_keywords(a: str) -> str:
    return a.replace("import ", "").replace("from ", "")


def get_imports(file: str) -> tuple[list[str], ...]:
    imports: tuple[list[str], ...] = tuple([[], [], []])

    lines: list[str] = [
        line
        for line in file.split("\n")
        if not line.isspace()
    ]
    
    counter: int = count_imports_lines(lines)
    #other_code: list[str] = []
    
    for line in lines[:counter]:
        if line.startswith("import "):
            imports[0].append(line + "\n")
        elif line.startswith("from "):
            imports[1].append(line + "\n")

    #imports[2].append(line)
    
    #imports[2][len(lines[counter:])+1:] = str(counter)
    imports[2][counter:] = lines[counter:]
    return imports


def is_import(line: str) -> bool:
    return line.startswith("import ") or line.startswith("from ") or not line


def count_imports_lines(lines: list[str]) -> int:
    counter: int = 0
    while counter < len(lines) and is_import(lines[counter]):
        counter += 1

    return counter



#reverse



