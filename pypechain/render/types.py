"""Functions to render Python types from an abi usng a jinja2 template."""

from __future__ import annotations

import importlib.metadata

from pypechain.render.contract import ContractInfo
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
    has_events = len(events) > 0
    has_structs = len(structs) > 0

    # We need to identify any inner structs that are defined in other contracts.
    types_files_imported = []
    # Iterate through all structs and look at the contract_name of each struct value
    for struct in structs:
        for struct_value in struct.values:
            # Add an import if it's a struct
            if struct_value.is_struct:
                if struct_value.contract_name is not None:
                    types_files_imported.append(struct_value.contract_name)
                # There's a case where a struct is imported locally without a contract name.
                # In this case, we use the name of the struct as the contract name.
                else:
                    types_files_imported.append(struct_value.name)

    if not has_events and not has_structs:
        return None

    return types_template.render(
        pypechain_version=importlib.metadata.version("pypechain"),
        contract_name=contract_info.contract_name,
        structs=structs,
        types_files_imported=list(types_files_imported),
        events=events,
        has_events=has_events,
        errors=errors,
    )
