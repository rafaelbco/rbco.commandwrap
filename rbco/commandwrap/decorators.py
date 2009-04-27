from commands import getstatusoutput
from pep362 import Signature
from cmdlinemaker import CommandLineMaker

def wrap_command(
    template,
    named_args_formatter=None,
    args_formatter=None,
    kwargs_formatter=None):
    
    def wrapper(func):
        return CommandLineMaker(
            template,
            Signature(func),
            named_args_formatter,
            args_formatter,
            kwargs_formatter
        )
        
    return wrapper    

def run_command(cmd_line_maker):
    def new_func(*args, **kwargs):
        cmd = cmd_line_maker(*args, **kwargs)
        print cmd
        return getstatusoutput(cmd)
    
    return new_func

def check_status(command_runner):
    def new_func(*args, **kwargs):
        (status, output) = command_runner(*args, **kwargs)
        if status != 0:
            raise RuntimeError(output)
        
        return (status, output)
    
    return new_func

def retain_only_output(command_runner):
    def new_func(*args, **kwargs):
        return command_runner(*args, **kwargs)[1]
            
    return new_func

def split_output(callable_returning_a_str):        
    def new_func(*args, **kwargs):
        return callable_returning_a_str(*args, **kwargs).split()
            
    return new_func

def output_none(command_runner):
    def new_func(*args, **kwargs):
        command_runner(*args, **kwargs)[1]
            
    return new_func    
