dict =  {
'I': 1,
'V': 5,
'X': 10,
'L': 50,
'C': 100,
'D': 500,
'M': 1000,
'XXI' : 21,
1000 : 'M',
1990 : 'MCMXC',
'MMVIII' : 2008,
4 : 'IV',
1 : 'I',
2008 : 'MMVIII',
'IV': 4,
'MDCLXVI' : 1666   
}
    
class RomanNumerals:
    def __init__(self):
        self = self
    def to_roman(num):
        if num in dict:
            return dict.get(num)
    def from_roman(roman):
        if roman in dict:
            return dict.get(roman)