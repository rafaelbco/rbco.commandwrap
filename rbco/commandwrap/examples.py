from decorators import *
import os


@retain_only_output
@check_status
@run_command
@wrap_command('ls %(kwargs)s %(path)s %(args)s')
def ls(path=None, *args, **kwargs): pass

ls_split = split_output(ls)

def process_diff_output(command_runner):
    def new_func(*args, **kwargs):
        (status, output) = command_runner(*args, **kwargs)        
        if status in (0, 1, 256):
            return not status
        
        raise RuntimeError(output)
    
    return new_func

@process_diff_output
@run_command
@wrap_command('diff %(kwargs)s %(a)s %(b)s')
def are_files_equal(a, b, **kwargs): pass

