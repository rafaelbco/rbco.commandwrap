from formatters import (simple_named_args_formatter, simple_args_formatter,
    simple_kwargs_formatter)

class CommandLineMaker(object):
    """
    `cmd_template` example:
    mycmd %(named1)s %(named2)s %(kwargs)s -x --verbose %(args)s
    
    Will behave like a function with this signature:
    f(named1, named2, *args, **kwargs)
    """        
    
    template = None
    signature = None
    named_args_formatter = simple_named_args_formatter
    args_formatter = simple_args_formatter
    kwargs_formatter = simple_kwargs_formatter
    
    def __init__(self,
        template, 
        signature, 
        named_args_formatter=None, 
        args_formatter=None,
        kwargs_formatter=None):
        
        self.template = template
        self.signature = signature
        
        if named_args_formatter:
            self.named_args_formatter = named_args_formatter
        if kwargs_formatter:
            self.kwargs_formatter = kwargs_formatter
        if args_formatter:
            self.args_formatter = args_formatter
        
    def __call__(self, *args, **kwargs):
        bindings = self.signature.bind(*args, **kwargs)
        values = {}
        
        for (k, v) in bindings.iteritems():
            if k == self.signature.var_args:
                value = self.args_formatter(v)
            elif k == self.signature.var_kw_args:
                value = self.kwargs_formatter(v)
            else:
                value = self.named_args_formatter(k, v)
            
            values[k] = value
        
        return self.template % values   
    
