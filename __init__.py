import string
from functools import lru_cache

import unicodedata


# This can improve performance by avoiding redundant computations when the function is
# called multiple times with the same arguments.
@lru_cache
def lookup(
    l: str, case_sens: bool = True, replace: str = "", add_to_printable: str = ""
):
    r"""
    Look up information about a character and suggest a replacement.

    Args:
        l (str): The character to look up.
        case_sens (bool, optional): Whether to consider case sensitivity for replacements. Defaults to True.
        replace (str, optional): The default replacement character when not found. Defaults to ''.
        add_to_printable (str, optional): Additional uppercase characters to consider as printable. Defaults to ''.

    Returns:
        dict: A dictionary containing the following information:
            - 'all_data': A sorted list of words representing the character name.
            - 'is_printable_letter': True if the character is a printable letter, False otherwise.
            - 'is_printable': True if the character is printable, False otherwise.
            - 'is_capital': True if the character is a capital letter, False otherwise.
            - 'suggested': The suggested replacement for the character based on the provided criteria.
    Example:
        sen = "Montréal, über, 12.89, Mère, Françoise, noël, 889"
        norm = ''.join([lookup(k, case_sens=True, replace='x', add_to_printable='')['suggested'] for k in sen])
        print(norm)
        #########################
        sen2 = 'kožušček'
        norm2 = ''.join([lookup(k, case_sens=True, replace='x', add_to_printable='')['suggested'] for k in sen2])
        print(norm2)
        #########################

        sen3="Falsches Üben von Xylophonmusik quält jeden größeren Zwerg."
        norm3 = ''.join([lookup(k, case_sens=True, replace='x', add_to_printable='')['suggested'] for k in sen3]) # doesn't preserve ü - ue ...
        print(norm3)
        #########################
        sen4 = "cætera"
        norm4 = ''.join([lookup(k, case_sens=True, replace='x', add_to_printable='ae')['suggested'] for k in
                         sen4])  # doesn't preserve ü - ue ...
        print(norm4)


        # Montreal, uber, 12.89, Mere, Francoise, noel, 889
        # kozuscek
        # Falsches Uben von Xylophonmusik qualt jeden groseren Zwerg.
        # caetera
    """
    # The name of the character l is retrieved using the unicodedata.name()
    # function and split into a list of words and sorted by len (shortest is the wanted letter)
    v = sorted(unicodedata.name(l).split(), key=len)
    sug = replace
    stri_pri = string.printable + add_to_printable.upper()
    is_printable_letter = v[0] in stri_pri
    is_printable = l in stri_pri
    is_capital = "CAPITAL" in v
    # Depending on the values of the boolean variables, the variable sug may be
    # updated to suggest a replacement for the character l. If the character is a printable letter,
    # the suggested replacement is set to the first word in the sorted list of names (v).
    # If case_sens is True and the character is a printable letter but not a capital,
    # the suggested replacement is set to the lowercase version of the first word in v.
    # If the character is printable, the suggested replacement is set to the character l itself.
    if is_printable_letter:
        sug = v[0]

        if case_sens:
            if not is_capital:
                sug = v[0].lower()
    elif is_printable:
        sug = l
    return {
        "all_data": v,
        "is_printable_letter": is_printable_letter,
        "is_printable": is_printable,
        "is_capital": is_capital,
        "suggested": sug,
    }
