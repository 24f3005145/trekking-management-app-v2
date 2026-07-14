from pathlib import Path

IGNORE_DIRS = {
    ".git",
    ".venv",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".idea",
    ".vscode",
    "dist",
    "build",
    "migrations"
}

IGNORE_FILES = {
    ".DS_Store"
}


def tree(directory: Path, prefix=""):
    entries = sorted(
        [e for e in directory.iterdir()
         if e.name not in IGNORE_DIRS
         and e.name not in IGNORE_FILES],
        key=lambda x: (x.is_file(), x.name.lower())
    )
    lines = []

    for index, entry in enumerate(entries):
        connector = "└── " if index == len(entries) - 1 else "├── "

        lines.append(prefix + connector + entry.name)

        if entry.is_dir():
            extension = "    " if index == len(entries) - 1 else "│   "
            lines.extend(tree(entry, prefix + extension))

    return lines


root = Path.cwd()

output = [root.name]
output.extend(tree(root))

with open("project_structure_new_6.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output))

print("project_structure_new_6.txt generated successfully.")