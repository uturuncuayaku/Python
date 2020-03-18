#generater expressions from
#PEP 289
# Author python at rnc.com Raymond Hettinger
#
#Abstract
"""
Generator expressions as a high performance, memory efficient generalization
of list comprehensions and generators

Rationale
List comprehensions has shown their usefulness throughout python
Many cases do not need a full list created in memory.
Instead you only need to iterate over the elements one at a time

"""

def main()
    
    #summation code will build a full list of 
    #squares in memory, iterate over those
    #values, and, when the reference is no
    #longer needed, delete the list

    sum([x*x for x in range(10)])
    
"""

    Memory is conserved by using a generator expression instead:
    """
    sum(x*x for x in range(10))

"""
    similar benefits are conferred on constructors for container objects

""" 
    s = set(word for line in page for word in line.split())
    d = dict( (k, func(k)) for k in keylist)

"""
    Generator expressions are especially useful with functions 
    like sum(), min(), and max() that reduce an iterable input to a 
    single value:

    """
    max(len(line) for line in file if line.strip())
"""
    Generator expressions also addres some examples of functionals
    coded with lambda:
    """
    reduce(lambda s, a: s+a.myattr, data,0)
    reduce(lambda s, a: s+a[3], data, 0)

    # These simplify to:
    sum(a.myattr for a in data)
    sum(a[3] for a in data)

"""
    List comprehensions greatly reduced the need for filter() and
    map()). Likewise, generator expressions are expected to 
    minimize the need for itertools.ifilter() and itertools.imap())).
    In contrast, the utility of other itertools will be enhanced by
    generator expressions::

    
        """
    dotproduct = sum(x*y for x,y in itertools.izip(x_verctor, y_vector))
"""
    Having a  syntax similar to list comprehensions also makes it
    easy to convert existing code into a generator expression when
    scaling up application.
    Early timings showed that generators had a significant
    performance advantage over list comprehensions. However, the
    latter were highly optimized for Py2.4 and now the performance
    is roughly comparable for small to mid-sized datasets. As the 
    data volumes grow larger, generator expressions tend to perform 
    better because they do not exhaust cache memory and they allow
    Python  to re-use objects between iterations.
    
        
        """
    g = (x**2 for x in range(10))
    print g.next()

    #is equivalent to 
def __gen(exp):
    for x in exp:
        yield x**2
g = __gen(iter(range(10)))
    print g.next()

    """
    Only the outermost for-expression is evaluated immediately
    the other expressions are deferred until the generator is run:

    """
    g= (tgtexp for var1 in exp1 if exp2 for var2 in exp3 if exp4)
    var2 in exp3 if exp4)
    # is equivalent to:
def __gen(bound_exp):
    for var1 in bound_exp:
        if exp2:
            for var2 in exp3:
                if exp4:
                    yield tgtexp
g = __gen(iter(exp1))
del __gen
"""
    The syntax requires that a generator expression always needs
    to be directly inside a set of parentheses and cannot have
    a comma on either side. With reference to the file Grammar/Grammar
    in CVS, two rules change.

    A. The rule
"""
atom: '(' [testlist] ')'
#changes to:
atom: '(' [testlist_gexp] ')'
#where testlist_gexp is almost the same as listmake,
#but only allows a single test after 'for' ... 'in':
testlist_gexp: test ( gen_for | (','test)*[','])
#the rule for arglist needs simi;lar changes
#this means you can write:

sum(x**2 for x in range(10))
#but you would have to write:
reduce(operator.add, (x**2 for x in range(10)))
#and alkso
g = (x**2 for x in range())
"""
    i.e if a function call has a single positional argument it
    can be a generator expression without extra parentheses,
    but in all other cases you have to parenthesize it.

3. The loop variable (if it is a simple variable or a tuple of
simple variables) is not exposed to the surrounding function.
This facilitates the implementation and makes typical use cases
more reliable. In some future version of python, list
comprehensions will also hide the induction variable from
 the surrounding code and in py2.4 warnings will be
 issued for code accessing the induction variable.

 for example
"""
x = "hello"
y = list(x for x in "abc")
print x #prints "hello", not "c"

# list comprehensions will remain unchanged for example

[x for x in S] #this is a list comprehension
[(x for x in S)] # this is a list containing one generator expression

#unfortunately there is a currently a slight syntactic difference. the expression
[x for x in 1,2,3]
#is legal, meaning:
[x for x in (1,2,3)]
#but generator expressions will not allow the former version

"""

is illegal

"""













if "__name__" = __main__ 
    main()
