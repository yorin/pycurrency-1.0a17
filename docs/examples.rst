``pycurrency`` examples
==========================

This serves as primitive test suite and documentation of some examples.

Using the ``Converter``
--------------------------

First import
``converter`` from the ``pycurrency`` module:

    >>> from pycurrency import converter
    >>> myconverter = converter.Converter(1,'USD','JMD')

Now let's test it:

    >>> result = myconverter.result()
    >>> result = float(result)
    >>> type(result)
    <type 'float'>

It should be possible to also change currency:

    >>> myconverter.from_cur = 'EUR'
    >>> myconverter.query['from']
    'USD'
    >>> output = myconverter.update()
    >>> myconverter.query['from']
    'EUR'

The ``rates`` dictionary (repsonsible usage)
----------------------------------------------
PyCurrency supports the concept of a rates dictionary
a rate is stored as a float and represented in the form
[from_cur]-[to_cur] e.g. USD-JMD means the cost of 1 USD in JMD. 
see the example below::

    >>> rates = {'EUR-USD':3.1}

The Converter accepts an optional 'rates' dictonary as an argument on instantiation::

    >>> myconverter = converter.Converter(1,'USD','JMD',rates)

The add_rate() method can be used to load new rates at anytime::

    >>> myconverter.add_rate('USD-JMD',85.6)

Rates are stored in a rates dictionary (_rates).

   >>> int(myconverter._rates['USD-JMD'])
   85
   >>> int(myconverter._rates['EUR-USD'])
   3

There is also a rates method which, by default, retrieves all rates::
    
   >>> allrates = myconverter.rates()
   >>> int(allrates['USD-JMD'])
   85
   >>> int(allrates['EUR-USD'])
   3

The default behaviour of the Converter object is to check the rates first before polling Google for rates.
If there is no existing rate it will search for a inverse rate, for example a JMD-USD conversion could be treated as an inverse rate of USD-JMD (using the formula Amount * 1/rate).
If there is neither a matching inverse rate or rate then it 'polls' Google for the current rate and adds it to rate dictionary.

Conversions 'on the fly'
--------------------------
The ``convert`` method is quick way to do conversions on the fly::

    from pyrcurrency.converter import convert
    convert(125,'EUR','GBP')
    109.504265

    >>> from pycurrency.converter import convert
    >>> result = convert(125,'EUR','GBP')
    >>> type(result)
    <type 'float'>
