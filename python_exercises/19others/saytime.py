import sys
import time

__version__ = "1.1.0"

class numwords():
    """
        return a number as words,
        e.g., 42 becomes "forty-two"
    """
    _words = {
        'ones': (
            'oh', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
        ), 'tens': (
            '', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
        ), 'teens': (
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen' 
        ), 'quarters': (
            'o\'clock', 'quarter', 'half'
        ), 'range': {
            'hundred': 'hundred'
        }, 'misc': {
            'minus': 'minus'
        }
    }
    _oor = 'OOR'    # Out Of Range

    def __init__(self, n):
        self.__number = n;

    def numwords(self, num = None):
        "Return the number as words"
        n = self.__number if num is None else num
        s = ''
        if n < 0:           # negative numbers
            s += self._words['misc']['minus'] + ' '
            n = abs(n)
        if n < 10:          # single-digit numbers
            s += self._words['ones'][n]  
        elif n < 20:        # teens
            s += self._words['teens'][n - 10]
        elif n < 100:       # tens
            m = n % 10
            t = n // 10
            s += self._words['tens'][t]
            if m: s += '-' + numwords(m).numwords()    # recurse for remainder
        elif n < 1000:      # hundreds
            m = n % 100
            t = n // 100
            s += self._words['ones'][t] + ' ' + self._words['range']['hundred']
            if m: s += ' ' + numwords(m).numwords()    # recurse for remainder
        else:
            s += self._oor
        return s

    def number(self):
        "Return the number as a number"
        return str(self.__number);

class saytime(numwords):
    """
        return the time (from two parameters) as words,
        e.g., fourteen til noon, quarter past one, etc.
    """

    _specials = {
        'noon': 'noon',
        'midnight': 'midnight',
        'til': 'til',
        'past': 'past'
    }

    def __init__(self, h, m):
        self._hour = abs(int(h))
        self._min = abs(int(m))

    def words(self):
        h = self._hour
        m = self._min
        
        if h > 23: return self._oor     # OOR errors
        if m > 59: return self._oor

        sign = self._specials['past']        
        if self._min > 30:
            sign = self._specials['til']
            h += 1
            m = 60 - m
        if h > 23: h -= 24
        elif h > 12: h -= 12

        # hword is the hours word)
        if h is 0: hword = self._specials['midnight']
        elif h is 12: hword = self._specials['noon']
        else: hword = self.numwords(h)

        if m is 0:
            if h in (0, 12): return hword   # for noon and midnight
            else: return "{} {}".format(self.numwords(h), self._words['quarters'][m])
        if m % 15 is 0:
            return "{} {} {}".format(self._words['quarters'][m // 15], sign, hword) 
        return "{} {} {}".format(self.numwords(m), sign, hword) 

    def digits(self):
        "return the traditionl time, e.g., 13:42"
        return "{:02}:{:02}".format(self._hour, self._min)

class saytime_t(saytime):   # wrapper for saytime to use time object
    """
        return the time (from a time object) as words
        e.g., fourteen til noon
    """
    def __init__(self, t):
        self._hour = t.tm_hour
        self._min = t.tm_min

def main():
    print(saytime_t(time.localtime()).words())

if __name__ == "__main__": main()
#main()