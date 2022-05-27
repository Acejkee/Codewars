select sailorsenshi.senshi_name as sailor_senshi , sailorsenshi.real_name_jpn as real_name , cats.name as cat  , schools.school as school
from sailorsenshi
LEFT JOIN cats ON sailorsenshi.cat_id = cats.id
LEFT JOIN schools ON sailorsenshi.school_id = schools.id