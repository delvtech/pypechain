"""Updates README.md with a package list."""

import os
from typing import Dict

import requests
import toml


def get_package_info_from_pypi(package_name: str) -> Dict[str, str]:
    """Gets package names and descriptions from pypi

    Parameters
    ----------
    package_name : str
        The package name.

    Returns
    -------
    Dict[str, str]
        A dictionary of information.
    """
    try:
        response = requests.get(f"https://pypi.org/pypi/{package_name}/json", timeout=10000)
        response.raise_for_status()
        data = response.json()
        version = data["info"]["version"]
        description = data["info"]["summary"]
        return {"name": package_name, "version": version, "description": description}
    except requests.RequestException:
        return {"name": package_name, "version": "N/A", "description": "Description not available"}


def parse_pyproject_toml(file_path: str) -> Dict[str, Dict]:
    """Parses the pyproject.toml for dependencies.

    Parameters
    ----------
    file_path : str
        The path to pyproject.toml.

    Returns
    -------
    Dict[str, Dict]
        Dependency information.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = toml.load(file)
    return data


def generate_markdown_table(project_data: Dict[str, Dict]) -> str:
    """Generates the packages section of the README.md

    Parameters
    ----------
    project_data : Dict[str, Dict]
        Data to populate the table with.

    Returns
    -------
    str
        The generated table.
    """
    markdown_table = "## Packages 📦\n\n"
    markdown_table += "| Package Name | Version | Description |\n"
    markdown_table += "|--------------|---------|-------------|\n"

    package_name = project_data["project"]["name"]
    version_badge = f"![](https://img.shields.io/pypi/v/{package_name}.svg)"
    version_link = f"(https://pypi.org/pypi/{package_name}/)"
    version = f"[{version_badge}]({version_link})"
    description = project_data["project"]["description"]
    markdown_table += f"| {package_name} | {version} | {description} |\n"

    dependencies = project_data["project"].get("dependencies", [])
    for dep in dependencies:
        dep_name = dep.split(" ")[0]
        package_info = get_package_info_from_pypi(dep_name)
        version_badge = f"![](https://img.shields.io/pypi/v/{dep_name}.svg)"
        version_link = f"(https://pypi.org/pypi/{dep_name}/)"
        markdown_table += (
            f"| {package_info['name']} | [{version_badge}]({version_link}) | {package_info['description']} |\n"
        )

    return markdown_table


def update_readme(readme_path: str, markdown_table: str) -> None:
    """Updates the READM.md packages section.

    Parameters
    ----------
    readme_path : str
        path to the README.md file
    markdown_table : str
        The table to generate

    """
    with open(readme_path, "r", encoding="utf-8") as file:
        content = file.readlines()

    # Find and replace the markdown table section
    start_marker = "## Packages 📦\n"
    end_marker = "##"
    start_index = -1
    end_index = -1

    for i, line in enumerate(content):
        if start_marker in line:
            start_index = i
        elif end_marker in line and start_index != -1 and i > start_index:
            end_index = i
            break

    if start_index != -1 and end_index != -1:
        content = content[:start_index] + [markdown_table] + content[end_index:]
    elif start_index != -1:
        content = content[:start_index] + [markdown_table]
    else:
        content.append("\n" + markdown_table)

    with open(readme_path, "w", encoding="utf-8") as file:
        file.writelines(content)


if __name__ == "__main__":
    SCRIPT_DIR = os.path.dirname(__file__)
    PROJECT_ROOT = os.path.join(SCRIPT_DIR, "..")

    pyproject_toml_path = os.path.join(PROJECT_ROOT, "pyproject.toml")
    _readme_path = os.path.join(PROJECT_ROOT, "README.md")

    _project_data = parse_pyproject_toml(pyproject_toml_path)
    _markdown_table = generate_markdown_table(_project_data)
    update_readme(_readme_path, _markdown_table)
