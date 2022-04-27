import os


def find_files() -> list[str]:
    #os.chdir()

    files_paths: list[str] = []
    for root, dirs, files in os.walk("."):
        for name in files:
            if(name.endswith(".py")):
                files_paths.append(os.path.join(root, name))
    return files_paths
