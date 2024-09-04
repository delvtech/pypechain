"""Script to recursively format json files under a directory."""

import json
import os


def _format_json_dir(json_dir):
    for root, dirs, files in os.walk(json_dir):
        # Format any outer json files
        for file in files:
            if file.endswith(".json"):
                json_file = os.path.join(root, file)
                # Format the JSON file
                with open(json_file, "r", encoding="utf-8") as file:
                    data = json.load(file)
                with open(json_file, "w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False, indent=2)

        for d in dirs:
            _format_json_dir(d)


if __name__ == "__main__":
    _format_json_dir("example/abis/")
    _format_json_dir("pypechain/test/")
