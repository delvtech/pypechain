"""Functions to render Python types from an abi usng a jinja2 template."""
from __future__ import annotations

from pypechain.render.contract import ContractInfo
from pypechain.utilities.templates import get_jinja_env


def render_types_file(contract_info: ContractInfo) -> str | None:
    """Returns the serialized code of the types file to be generated.

    Parameters
    ----------
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

    structs = contract_info.structs.values()
    events = contract_info.events.values()
    has_events = bool(events)
    has_structs = bool(structs)
    has_event_params = any(len(event.inputs) > 0 for event in events)

    if not has_events and not has_structs:
        return None

    return types_template.render(
        contract_name=contract_info.contract_name,
        structs=structs,
        events=events,
        has_events=has_events,
        has_event_params=has_event_params,
    )
