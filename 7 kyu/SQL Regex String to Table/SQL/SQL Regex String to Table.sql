select regexp_split_to_table(text , 'a|e|i|o|u') as results
from random_string