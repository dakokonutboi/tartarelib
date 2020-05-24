import rsa
import sys

pub = eval("rsa."+str(sys.argv[1]))
msg = sys.argv[2].encode('utf8')

print(str(rsa.encrypt(msg,pub)).replace('"',"[GUI]").replace("\\","[ASL]"))
