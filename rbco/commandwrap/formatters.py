def simple_named_args_formatter(self, name, value):
    if not value:
        return ''
    
    return str(value)

def simple_args_formatter(self, args):
    return ' '.join(str(a) for a in args)

def simple_kwargs_formatter(self, kwargs):
    args = []
    for (k, v) in kwargs.iteritems():
        if (not v) or (not k):
            continue
        
        suffix = '-'
        separator = ' '
        if len(k) > 1:
            suffix = '--'
            separator = '='        
                
        if v is True:
            arg = suffix + k
        else:                         
            arg = suffix + k + separator + str(v)
        
        args.append(arg)
            
    return simple_args_formatter(self, args)