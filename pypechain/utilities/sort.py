"""Sorting utilities."""


def get_intersection_and_unique(lists: list[list[str]]) -> tuple[set[str], set[str]]:
    """Process a list of lists of strings to get the intersection and unique values.

    The intersection is a set of strings that occur in all sub-lists.
    The unique values are strings that only occur in one sub-list.

    Parameters
    ----------
    lists : list[list[str]]
        A list of lists of strings, where each sub-list is an entity to compute sets over.

    Returns
    -------
    tuple[set[str], set[str]]
        The (intersection, unique_values) sets
    """
    intersection = set(lists[0])
    for lst in lists[1:]:
        intersection &= set(lst)
    string_counts = {}
    for lst in lists:
        for item in set(lst):
            string_counts[item] = string_counts.get(item, 0) + 1
    unique_values = {item for item, count in string_counts.items() if count == 1}
    return (intersection, unique_values)
