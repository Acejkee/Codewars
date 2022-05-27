select CONCAT(md5, REPEAT('1' ,length(sha256) - length(md5))) as md5 , concat(REPEAT('0' ,length(sha256) - Length(sha1)) ,sha1) as sha1 , sha256
from encryption