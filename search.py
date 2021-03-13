import xml.etree.ElementTree as ET 
import csv
import dateutil.parser

class Search:
    
    def round_dictionary(self, dict, decimals=2):
        """
        Rounds all values to no more than 2 decimal places. You'll
        need to call this on your dictionaries before returning to
        take care of any floating point weirdness.
        Note: You'll only need this in the methods that return
        dictionaries with a floating point value. 
        """
        for key in dict:
            dict[key] = round(dict[key], 2)
        return dict 

    def amount_spent(self, category):
        """
        Returns the amount spent in category
        """
        tree = ET.parse('sales-data.xml')
        root = tree.getroot()
        sum = 0
        for sale in root.findall('./person'):
            cat = sale.find('category').text
            if(cat==category):
                sum+=float(sale.find('amount').text)
        return sum
            
    def spent_by_gender(self):
        """
        Returns a dictionary with a M and F key and the
        amount spent by each gender
        """
        tree = ET.parse('sales-data.xml')
        root = tree.getroot()

        ret = {'M':0.0,'F':0.0}

        for sale in root.findall('./person'):
            gender = sale.find('gender').text
            ret[gender]+=float(sale.find('amount').text)
        return self.round_dictionary(ret)
        
    def all_categories(self):
        """
        Returns a dictionary with amounts spent in each
        category. The category should be the key, the
        sum of all sales in that category is the value
        """
        tree = ET.parse('sales-data.xml')
        root = tree.getroot()

        ret = {}

        for sale in root.findall('./person'):
            key = sale.find('category').text
            if not key in ret:
                ret[key] = float(sale.find('amount').text)
            else:
                ret[key]+=float(sale.find('amount').text)
        return self.round_dictionary(ret)

    def spent_between(self, start_date, end_date):
        """
        Returns the sum of all sales between start_date
        and end_date, inclusive
        """
        tree = ET.parse('sales-data.xml')
        root = tree.getroot()

        amt = 0

        for sale in root.findall('./person'):
            currDate = dateutil.parser.parse(sale.find('timestamp').text)
            if(currDate>=start_date and currDate<=end_date):
                amt+=float(sale.find('amount').text)
        return amt

    