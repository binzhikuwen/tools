import sys
import pexpect

PROMPT = ['# ','>>> ','> ','\$ ']

if len(sys.argv) != 3:
    print 'argc erro'
    exit(0)

user = sys.argv[1]
#passwd can be hard code
passwd = sys.argv[2]
server = '127.0.0.1'
command = 'ssh ' + user + '@' + server
child = pexpect.spawn(command)
ret = child.expect([pexpect.TIMEOUT,'[P|p]assword:'])
if ret == 0:
    print 'error connecting'
    exit(0)
if ret == 1:
    child.sendline(passwd)
    ret = child.expect(PROMPT)
    if ret != 0:
        print 'connecting success'
        child.interact()
        exit(0)

print 'error connecting'
