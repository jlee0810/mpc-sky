import pexpect

child = pexpect.spawn("./mascot-ecdsa-party.x -p 1 -h localhost")

p2k = child.readline().decode()
spk = child.readline().decode()
pcks = child.readline().decode()

print(pcks.split()[-1])