def make_ping_command():
     return f'*1\r\n$4\r\nPING\r\n'

def make_echo_command(arg):
     return f'*2\r\n${len("ECHO")}\r\nECHO\r\n${len(arg)}\r\n{arg}\r\n'

def make_set_command(key, value):
     return f'*3\r\n$3\r\nSET\r\n${len(key)}\r\n{key}\r\n${len(value)}\r\n{value}\r\n'

def make_get_command(key):
     return f'*2\r\n$3\r\nGET\r\n${len(key)}\r\n{key}\r\n'