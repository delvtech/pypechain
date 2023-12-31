"""Functions to render Python types from an abi usng a jinja2 template."""
from __future__ import annotations

from dataclasses import asdict
from pathlib import Path

from pypechain.utilities.abi import get_events_for_abi, get_structs_for_abi, load_abi_from_file
from pypechain.utilities.templates import get_jinja_env


def render_types_file(contract_name: str, abi_file_path: Path) -> str | None:
    """Returns the serialized code of the types file to be generated.

    Arguments
    ---------
    contract_name : str
        The name of the contract to be parsed.
    types_template : Template
        A jinja template containging types for all structs within an abi.
    abi_file_path : Path
        The path to the abi file to parse.

    Returns
    -------
    str
        A serialized python file.
    """
    env = get_jinja_env()
    types_template = env.get_template("types.py.jinja2")

    abi, _ = load_abi_from_file(abi_file_path)

    structs_by_name = get_structs_for_abi(abi)
    structs_list = list(structs_by_name.values())
    structs = [asdict(struct) for struct in structs_list]
    events = [asdict(event) for event in get_events_for_abi(abi)]
    has_events = bool(events)
    has_structs = bool(structs)
    has_event_params = any(len(event["inputs"]) > 0 for event in events)

    if not has_events and not has_structs:
        return None

    return types_template.render(
        contract_name=contract_name,
        structs=structs,
        events=events,
        has_events=has_events,
        has_event_params=has_event_params,
    )
