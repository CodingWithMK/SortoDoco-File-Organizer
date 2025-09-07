from pathlib import Path
import json

def load_rules(json_path: Path) -> dict[str, list[str]]:

    with open(json_path, "r") as file:
        extensions = json.load(file)

    cleaned_extensions: dict[str, list[str]] = {}
    for category, ext_list in extensions.items():
        cleaned_extensions[category] = [
            ext.lower().removeprefix(".") for ext in ext_list
            ]

    return cleaned_extensions

def build_ext_map(rules: dict[str, list[str]]) -> dict[str, str]:
    ext_map: dict[str, str] = {}

    for category, ext_list in rules.items():
        for ext in ext_list:
            if ext in ext_map and ext_map[ext] != category:
                raise ValueError(
                    f"Extension '{ext}' already mapped to '{ext_map[ext]}', also found in '{category}'."
                )
            ext_map[ext] = category
        
    return ext_map