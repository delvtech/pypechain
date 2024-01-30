"""Functions to render Python types from an abi usng a jinja2 template."""

from __future__ import annotations

from pypechain.render.contract import ContractInfo
from pypechain.utilities.abi import get_structs_for_abi
from pypechain.utilities.templates import get_jinja_env


def render_types_file(contract_info: ContractInfo) -> str | None:
    """Returns the serialized code of the types file to be generated.

    Parameters
    ----------
    contract_info: ContractInfo
        Information related to the solidity contract.

    Returns
    -------
    str | None
        A serialized python file.
    """
    env = get_jinja_env()
    types_template = env.get_template("types.py.jinja2")

    structs = contract_info.structs.values()
    events = contract_info.events.values()
    errors = contract_info.errors.values()
    has_events = bool(events)
    has_structs = bool(structs)
    has_event_params = any(len(event.inputs) > 0 for event in events)

    structs_used = get_structs_for_abi(contract_info.abi)
    types_files_imported = {
        struct.contract_name for struct in structs_used if struct.contract_name != contract_info.contract_name
    }

    if not has_events and not has_structs:
        return None

    return types_template.render(
        contract_name=contract_info.contract_name,
        structs=structs,
        types_files_imported=list(types_files_imported),
        events=events,
        errors=errors,
        has_events=has_events,
        has_event_params=has_event_params,
    )
