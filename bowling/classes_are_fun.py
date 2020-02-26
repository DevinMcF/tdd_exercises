class Test:
    """
    >>> Test.foo
    21

    >>> a = Test()
    >>> b = Test()
    >>> a.foo
    21
    
    >>> b.foo
    21
    
    >>> a.foo += 9
    >>> a.foo
    30
    
    >>> b.foo
    21
    
    >>> Test.foo
    21
    
    >>> Test.foo -= 10
    >>> Test.foo
    11
    
    >>> a.foo
    30
    
    >>> b.foo
    11
    """
    foo = 21
