from vmd import *
import copy

vmd = vmdread("b.vmd")
motion = motionreader(vmd)
ik = ikreader(vmd["ik"])

WriteVMD("example.vmd", motion)



vmdc = copy.deepcopy(vmd)
vmdc["motion"] = vmdc["motion"][:32]
vmdc["morph"] = vmdc["morph"][:32]

print("vmd")
print(vmdc)
print()

print("motion")
print(motion[:6])
print()

print(ik)

print(ik)

