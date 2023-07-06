# character normalization (especially for Latin letters - linguistic purposes)

## pip install normaltext 

the lookup function simplifies character analysis, provides replacement
 suggestions, and offers performance improvements through memorization. 
 It can be beneficial for tasks involving character normalization, 
 text processing, or any scenario where character properties and 
 substitutions are relevant.

#### Tested against Windows 10 / Python 3.10 / Anaconda 


The lookup function can be used by developers or anyone working 
with text processing or character manipulation tasks. It provides 
information about a given character and suggests 
a replacement based on certain criteria.

### Character Information: 

The function retrieves the name of the character using unicodedata.name() and provides a sorted list of words representing the character name. 
This can be useful for analyzing and understanding the properties of a character.

### Suggested Replacement: 

The function suggests a replacement for the character based on the provided criteria. 
By considering factors like case sensitivity, printability, and capitalization, the function offers a recommended substitution. 
This can be beneficial when you need to transform 
or normalize characters in a specific context.

### Memoization and Performance: 

The function utilizes the functools.lru_cache decorator, which caches the results of previous function calls. 
This means that if the function is called multiple times with the same character, 
the result is retrieved from the cache instead of recomputing it.
This caching mechanism can significantly improve the performance of the function when there are repetitive 
or redundant character lookups.

### Flexibility: 

The lookup function provides optional parameters that allow customization of its behavior. 
The case_sens parameter determines whether case sensitivity is considered for replacements. 
The replace parameter allows setting a default replacement character. 
The add_to_printable parameter enables the addition of extra uppercase characters to the set of printable characters. 
These options provide flexibility to adapt the 
function to different requirements and use cases.




```python
from normaltext import lookup
sen = "Montréal, über, 12.89, Mère, Françoise, noël, 889"
norm = ''.join([lookup(k, case_sens=True, replace='x', add_to_printable='')['suggested'] for k in sen])
print(norm)
#########################
sen2 = 'kožušček'
norm2 = ''.join([lookup(k, case_sens=True, replace='x', add_to_printable='')['suggested'] for k in sen2])
print(norm2)
#########################
sen3 = "Falsches Üben von Xylophonmusik quält jeden größeren Zwerg."
norm3 = ''.join([lookup(k, case_sens=True, replace='x', add_to_printable='')['suggested'] for k in
                 sen3])  # doesn't preserve ü - ue ...
print(norm3)
#########################
sen4 = "cætera"
norm4 = ''.join([lookup(k, case_sens=True, replace='x', add_to_printable='ae')['suggested'] for k in
                 sen4])  # doesn't preserve ü - ue ...
print(norm4)
Montreal, uber, 12.89, Mere, Francoise, noel, 889
kozuscek
Falsches Uben von Xylophonmusik qualt jeden groseren Zwerg.
caetera

```