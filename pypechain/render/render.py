"""Functions to render Python files from an abi usng a jinja2 template."""

from __future__ import annotations

import os
from functools import partial
from multiprocessing import Pool
from pathlib import Path

from pypechain.render.contract import ContractInfo, get_contract_infos, render_contract_file
from pypechain.render.types import render_types_file
from pypechain.utilities.abi import AbiInfo
from pypechain.utilities.file import write_string_to_file
from pypechain.utilities.format import format_file
from pypechain.utilities.types import RenderOutput


def render_contracts(
    abi_infos: list[AbiInfo],
    output_dir: str,
    line_length: int = 120,
    apply_formatting: bool = True,
    parallel: bool = False,
    chunksize: int | None = None,
) -> list[RenderOutput]:
    """Processes a single JSON file to generate class and types files.


    Parameters
    ----------
    abi_infos : list[AbiInfo]
        A list of objects containing each ABI and metadata.
    output_dir : str
        The directory where files will be written to.
    line_length : int, optional
        Black's line-length config option.
    apply_formatting : bool, optional
        If True, autoflake, isort and black will be applied to the file in that order, by default True.
    parallel : bool, optional
        If True, multiple processes will be used to process the ABIs in parallel.
    chunksize: int, optional
        If set, abis are processed in approximately groups of chunksize.
        Use 1 for one process per ABI.
        Defaults to the number of ABIs // 10.

    Returns
    -------
    list[RenderOutput]
        A list of filenames and definitions for the generated files.
    """
    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-positional-arguments

    contract_infos = get_contract_infos(abi_infos)

    # this is what we are returning
    file_outputs: list[RenderOutput] = []

    # for every [ContractName] generate a:
    #    1. [ContractName]Contract.py
    #    2. [ContractName]Types.py
    #  The Contract file defines the Contract class and functions.
    #  The Types file has the structs and events defined in the solidity contract.

    if parallel:
        # make a parallel pool; defaults to the number of available CPUs
        with Pool() as pool:
            # chunksize should be increased with the number of iterables
            chunksize = len(contract_infos) // 10
            for file_output_sublist in pool.imap(
                partial(
                    render_contract, output_dir=output_dir, line_length=line_length, apply_formatting=apply_formatting
                ),
                list(contract_infos.values()),
                chunksize=chunksize,
            ):
                file_outputs.extend(file_output_sublist)
    # Sequential mode
    else:
        for contract_info in contract_infos.values():
            file_outputs.extend(
                render_contract(
                    contract_info=contract_info,
                    output_dir=output_dir,
                    line_length=line_length,
                    apply_formatting=apply_formatting,
                )
            )

    return file_outputs


def render_contract(
    contract_info: ContractInfo, output_dir: str, line_length: int, apply_formatting: bool
) -> list[RenderOutput]:
    """Get the file name for a single ContractInfo object


    Parameters
    ----------
    contract_info : ContractInfo
        A ContractInfo object created from an ABI.
    output_dir : str
        The directory where files will be written to.
    line_length : int, optional
        Black's line-length config option.
    apply_formatting : bool, optional
        If True, autoflake, isort and black will be applied to the file in that order, by default True.

    Returns
    -------
    list[RenderOutput]
        A list of filenames and definitions for the generated Contract and Types files.
    """
    file_outputs: list[RenderOutput] = []
    file_path = Path(output_dir)

    rendered_contract_code = render_contract_file(contract_info)
    if rendered_contract_code:
        contract_file_name = contract_info.contract_name + "Contract.py"
        contract_file_path = Path(os.path.join(file_path, contract_file_name))
        write_string_to_file(contract_file_path, rendered_contract_code)
        if apply_formatting is True:
            format_file(contract_file_path, line_length)
        # We expose only the contract function from the contract file
        file_outputs.append(
            RenderOutput(
                filename=f"{contract_info.contract_name}Contract",
                definitions=[f"{contract_info.contract_name}Contract"],
            )
        )

    rendered_types_code = render_types_file(contract_info)
    if rendered_types_code:
        types_file_name = contract_info.contract_name + "Types.py"
        types_file_path = Path(os.path.join(file_path, types_file_name))
        write_string_to_file(types_file_path, rendered_types_code)
        if apply_formatting is True:
            format_file(types_file_path, line_length)

        # We don't expose anything from the types file to avoid name collisions.
        # Any imports from types file require the fully qualified name.

    return file_outputs
