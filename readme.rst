========================================================================
                          leonLPST
========================================================================

**leonLPST** is an implementation of Lazy Propagation Segment Tree for
python users.

An brief introduction to Lazy Propagation Tree can be found here
http://www.geeksforgeeks.org/lazy-propagation-in-segment-tree/

Lazy Propagation Segment Tree is optimized for quickly retrieving the 
summation, minmization or maximizition of a given interval, adding or 
setting the same value to all elements in the interval.

LPST's computational complexity in doing interval updating or summation
is O(logn), while that of normal array is O(n). So LPST can dramatically
increase the speed of your programe.

Download and source code
========================

You can fetch **leonLPST** from:
    - GitHub https://github.com/yuexihan/leonLPST

Quick start
===========

To install, go to the downloaded folder::

    python setup.py install

Then create an LPSTree::

    >>> import leonLPST
    >>> tree = leonLPST.LPSTree(100)

All elements are set to 0 automatically. You can designate the initial value
by writing like this::

    >>> tree = leonLPST.LPSTree(100, value=11)

You can retrieve element and set value by using common sequence operations::

    >>> len(tree)
    100
    >>> tree[1]
    11
    >>> tree[2] = 1000
    >>> tree[2]
    1000

You can get the sum of an interval [start, stop)::

    >>> tree.get(10, 20)
    110

You can add or set all elements in an interval [start, stop) with a constant
value::

    >>> tree.set(0, 10, 9)
    >>> tree.add(9, 14, -10)
    >>> tree
    [9, 9, 9, 9, 9, 9, 9, 9, 9, -1, 1, 1, 1, 1, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]

If you create a tree by setting the reduce function, then you will get the 
reduced result of an interval according to the reduce function when you call
get method. For example::

    >>> tree = leonLPST.LPSTree(10, reducef=max)
    >>> tree.add(0, 5, -2)
    >>> tree.add(2, 4, 5)
    >>> tree.get(0, 7)
    3
    >>> tree
    [-2, -2, 3, 3, -2, 0, 0, 0, 0, 0]

The tree is set to use max as its reduce function. So when you use the get
method, it will return you the maximum value in the interval. The default 
reduce function is sum.

If you set the modulo number, the tree will do the modulo operation for
you automatically::

    >>> tree = leonLPST.LPSTree(10, value=11 , modulo=5)
    >>> tree.set(5, 10, 13)
    >>> tree.add(1, 3, 3)
    >>> tree.get(0, 9)
    3
    >>> tree
    [1, 4, 4, 1, 1, 3, 3, 3, 3, 3]