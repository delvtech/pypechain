"""Script to recursively format json files under a directory."""

from pypechain.utilities.format import format_json_dir

if __name__ == "__main__":
    format_json_dir("example/abis/")
