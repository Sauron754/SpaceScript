We use PEP8 style guiding with a couple exceptions/specifications:

variable names: camelCase
function names: underline
method names: underline
class names: camelCase
global variables(only allowed inside one module): _camelCase

We have decided to specify the variable type after the variable(appendix), for better readability:

_int = integer</br>
_float = float</br>
_str = string</br>
_bool = boolean</br>
_char = character</br>
_obj = object</br>
_arr = array</br>
_dict = dictionary</br>
_q = queue(cross-thread object)</br>
_p = pipe(cross-thread object)</br>
_a = cross-thread array(cross-thread object)</br>
_v = cross-thread value(cross-thread object)</br>
_proc = multiprocessing threaded process</br>

We are using a maximum line length of 80 characters(this can be neglected if it improves readability)
