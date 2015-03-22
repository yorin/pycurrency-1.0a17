Overview
----------
This is a quick overview of the pycurrency package. The package uses Google's currency calculator to do live conversions.
I cannot promise how accurate compared to bank rates on the ground in the various countries, but they are acceptable for making estimates.

Be a responsible citizen and don't write code that polls google for every query, instead do caching where ever you can. Caching will make your
app run faster anyway!

Installation:

To install pycurrency use the command::

	pip install pycurrency

or::

	easy_install pycurrency

Usage:

Converting from one currency to another
The syntax is Converter(amount,from_currency,to_currency), for example
to convert from 1 USD to Jamaican Dollars::

	>>> from pycurrency import converter
	>>> myconverter = converter.Converter(1,'USD','JMD')
	>>> myconverter.result()
	u'85.2878465'


If you need other information there is a dictionary which returns the 'to' and 'from' values which 
can be retrieved with the 'ratio' method::

	>>> myconverter.ratio()
	{'to': u'85.2878465', 'from': u'1'}

You can change any parameter 'from_cur', 'to_cur' or 'amount'::

	>>> myconverter.to_cur='EUR'
	>>> myconverter.update()
	{'to': u'0.72838517', 'from': u'1'}
	>>> myconverter.from_cur='EUR'
	>>> myconverter.to_cur='JMD'
	>>> myconverter.update()
	{'to': u'117.091684', 'from': u'1'}

Here's an example of changing the amount to be converted::

	>>> myconverter.amount = '400'
	>>> myconverter.update()
	{'to': u'46836.6736', 'from': u'1'}

