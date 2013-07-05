import pprint
import types

def var_dumpy(obj, level = 0, **kwargs):
    """
    Example of usage:
    >>> class MyObject():
    ...     my_list = ['t','e','s','t']
    ...     def __init__(self):
    ...         self.my_hello = ['h','e','l','l','o']
    ...         self.my_int = 50
    >>>
    >>> myobject = MyObject()

    the test shud failed but it throws you the dump of myobject:
    >>> var_dumpy(myobject)

    or you could use with globals() or locals()
    >>> var_dumpy(globals())

    """
    indent = '\t' * level
    print ('%s "%s" %s' %( indent, obj, type(obj)  ) )
    try:
        for attr in dir(obj) :
            attr_type = getattr(obj, attr)
            if 'all' in kwargs and kwargs['all'] == True:
                if attr.startswith('__'):
                    print ('%s "%s" %s %s' %( indent, attr, type(attr_type) , attr_type) )
                else:
                    pass
            else:
                pass
            if not attr.startswith('__') :
                if not isinstance(attr_type,  types.TupleType) and \
                   not isinstance(attr_type, types.ListType) and \
                   not isinstance(attr_type, types.DictType):
                    print ('%s "%s" %s %s' %( indent, attr, type(attr_type) , attr_type) )
                else:
                    print ('%s "%s" %s' %( indent, attr, type(attr)) )
                    var_dumpy(getattr(obj, attr), (level + 1), **kwargs)
            else:
                pass #print ('%s "%s" %s' %( indent, attr, type(attr)) )
    except Exception as e:
        print ('%s %s' %(e,type(e)))
        print ('%s %s' %(obj, type(obj)))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
