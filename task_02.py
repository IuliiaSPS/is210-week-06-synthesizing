#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02"""


MAIL = 'Dear {0},\nI look forward to meeting with you on {1}.\nBest,\nMe'


def prepare_email(appointments):
    """This function formats base string according to sent arguments.

    Args:
        appointments (list of tuples): Arg to take list of tuples with strings.

    Returns:
        list: New formatted MAIL list with arguments inserted.

    Examples:
        >>>prepare_email([('Jen', '2015'), ('Max', 'March 3')])
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe', 'D
        ear Max,\nI look forward to meeting with you on March 3.\nBest,\nMe']
    """
    new_list = []
    for pos, _ in enumerate(appointments):
        new_list.append(MAIL.format(appointments[pos][0], appointments[pos][1]))
    return new_list
