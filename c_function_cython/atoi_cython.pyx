from libc.stdlib cimport atoi

cdef int parse_charptr_to_py_int(char* s):
    return atoi(s)

def parse_s_to_i(s):
    return parse_charptr_to_py_int(s)
