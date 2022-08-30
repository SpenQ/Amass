from ctypes import *

lib = cdll.LoadLibrary("./library.so")

# go type

class go_string(Structure):
    _fields_ = [
        ("p", c_char_p),
        ("n", c_int)]

class GoSlice(Structure):
    _fields_ = [("data", POINTER(go_string)), ("len", c_longlong), ("cap", c_longlong)]

runEnumCommand = lib.runEnumCommand

# class runEnumCommand(Structure):
#     _fields_ = [('a', c_int),
#                 ('b', c_int),
#                 ('c', c_int),
#                 ('d', c_int),
#                 ('e', c_int),
#                 ('f', c_int)]
# lib.runEnumCommand.restype = runEnumCommand

lib.runEnumCommand.argtypes = [GoSlice]

args = [
    b"-d",
    b"tesla.com"
]

t = GoSlice((go_string * 2)(go_string(c_char_p(args[0]), len(args[0])), go_string(c_char_p(args[1]), len(args[1]))), 2, 2)
f = lib.runEnumCommand(t)
f # should be 0 for no errors
