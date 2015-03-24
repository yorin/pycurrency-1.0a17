import urllib2
import re

class Converter:
    """ A currency converter class """
    def __init__(self,amount,from_cur,to_cur,rates={}):
        self.amount = amount
        self.from_cur = from_cur
        self.to_cur = to_cur
        self._rates = rates
        self._ratio = self.update()

    def ratio(self):
        return self._ratio

    def update(self):

        fromto = "%s-%s" % (self.from_cur,self.to_cur)
        cur_ratio = {}

        if self._rates.has_key(fromto):
            result = self._rates[fromto] * self.amount
            cur_ratio['from'] = self.amount
            cur_ratio['to'] = result

        else:
            self.query = {'amount':self.amount, 
             'from':self.from_cur,
             'to' :self.to_cur}

            #depricated url does not exist
            #self.url = "http://www.google.com/ig/calculator?hl=en&q=%(amount)s%(from)s%(eq)s%(to)s" % self.query

            #https://www.google.com/finance/converter?a=1&from=USD&to=PHP
            #{'to': 'PHP', 'amount': 1, 'from': 'USD'}
            self.url = 'https://www.google.com/finance/converter?a='+ "%(amount)s" % self.query + '&from=' + "%(from)s" % self.query + '&to=' + "%(to)s" % self.query

            request = urllib2.urlopen(self.url)
            raw_data = request.read()
            raw_data = re.search("<div id=currency_converter_result>.*", raw_data).group()
            p = re.compile(r'<.*?>|=')
            list1 = re.split("\s+", p.sub('', raw_data))
            lhs = float(list1[0])
            rhs = float(list1[2])
            cur_ratio['from'] = lhs
            cur_ratio['to'] = rhs
            self._rates[fromto] = rhs / self.amount


        self._ratio = cur_ratio

        return cur_ratio

    def result(self):

        return self._ratio['to']

      
    def add_rate(self,fromto,value):
        self._rates[fromto] = value

    def rates(self):
        return self._rates

def convert(amount,from_cur,to_cur):
    return Converter(amount,from_cur,to_cur).result()
