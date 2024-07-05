import pexpect

child = pexpect.spawn("./mascot-ecdsa-party.x -p 0 -h localhost")

serverkey = "01"
child.sendline(serverkey)
spk = child.readline().decode()
p1pl = child.readline().decode()
p2pk = child.readline().decode()
cpk = child.readline().decode()
spl = child.readline().decode()
pcks = child.readline().decode()

print(pcks.split()[-1])