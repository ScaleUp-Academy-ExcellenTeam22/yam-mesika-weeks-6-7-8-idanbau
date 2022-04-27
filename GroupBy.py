import itertools


def group_by(function, iterables):
    """
    :param function: Group by our specific function to check
    :param iterables: Iterables item to apply function
    :return: Dictionary that includes function results and all its variables that had it
    """
    return {key: list(value) for key, value in itertools.groupby(sorted(iterables, key=function), function)}
