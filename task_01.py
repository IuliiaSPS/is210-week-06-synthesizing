#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_01"""


def get_party_stats(families, table_size=6):
    """This function counts objects and and

    Args:
        families (list): Arg to be counted and divided.
        table_size (int): Just a random number. Defult is 6.

    Returns:
        tuple: Number of objects in families and ceiling division of nested list
        s by table_size.

    Examples:
        >>> get_party_stats([['Jan'], ['Jen','Jess'], ['Jem', 'Jack', 'Janis']])
        (6, 3)
        >>> get_party_stats([['Jan'], ['Jen','Jess'], ['Jem', 'Jack', 'Janis']],
            2)
        (6, 4)
    """
    tables = 0
    people = 0
    for number, _ in enumerate(families):
        tables += - (-len(families[number]) // table_size)
        people += len(families[number])
    return (people, tables)
