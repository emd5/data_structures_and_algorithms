class Roman(object):
    r = {
        # value is an array of strings for each key in
        # the ones, tens, hundreds, and thousands places
        # up to 3000 (since given max is 3999)
        1: ['I', 'X', 'C', 'M'],
        2: ['II', 'XX', 'CC', 'MM'],
        3: ['III', 'XXX', 'CCC', 'MMM'],
        4: ['IV', 'XL', 'CD'],
        5: ['V', 'L', 'D'],
        6: ['VI', 'LX', 'DC'],
        7: ['VII', 'LXX', 'DCC'],
        8: ['VIII', 'LXXX', 'DCCC'],
        9: ['IX', 'XC', 'CM']
    }

    def int_to_roman(self,num):
        """
        :type num: int
        :rtype: str
        """
        ret = ""
        for i in range(len(str(num))):
            digit = (num // (10 ** i)) % 10
            if digit > 0:
                ret = self.r[digit][i] + ret
        return ret
