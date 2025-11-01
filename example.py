import struct

def vmdread(file):
    result = {}
    f = open(file,"rb")

    
    header = f.read(30)
    result["headers"] = header

    
    name = f.read(20)
    result["name"] = name

    
    motioncount = int.from_bytes(f.read(4),"little")
    result["motioncount"] = motioncount
    
    motion = f.read(motioncount*111)
    result["motion"] = motion

    
    morphcount = int.from_bytes(f.read(4),"little")
    result["morphcount"] = morphcount
    
    morph = f.read(morphcount*23)
    result["morph"] = morph

    
    cameracount = int.from_bytes(f.read(4),"little")
    result["cameracount"] = cameracount
    
    camera = f.read(cameracount*61)
    result["camera"] = camera

    
    lightcount = int.from_bytes(f.read(4),"little")
    result["lightcount"] = lightcount
    
    light = f.read(lightcount*61)
    result["light"] = light

    
    shadowcount = int.from_bytes(f.read(4),"little")
    result["shadowcount"] = shadowcount
    
    shadow = f.read(shadowcount*61)
    result["shadow"] = shadow

    iktotalcount = int.from_bytes(f.read(4),"little")
    result["iktotalcount"] = iktotalcount

    result["ik"] = []
    
    for i in range(iktotalcount):
        ikcount = int.from_bytes(f.read(4),"little")
        ikshow = int.from_bytes(f.read(1),"little")
        iknumber = int.from_bytes(f.read(4),"little")
        ik = f.read(iknumber*21)
        result["ik"].append({})
        result["ik"][-1]["ikcount"] = ikcount
        result["ik"][-1]["ikshow"] = ikshow
        result["ik"][-1]["iknumber"] = iknumber
        result["ik"][-1]["ik"] = ik

    
    end = f.read(-1) ; result["end"] = end

    
    try:
        result["name"] = result["name"].decode("cp932")
    except:
        pass
    
    
    return result


def motionreader(parser):
    result = []
    for i in range(0,len(parser['motion']),111):
        result.append({})
        result[-1]["name"] = parser['motion'][i+0:i+15]
        result[-1]["frame"] = parser['motion'][i+15:i+19]
        result[-1]["position"] = parser['motion'][i+19:i+31]
        result[-1]["quaternion"] = parser['motion'][i+31:i+47]
        result[-1]["bezier"] = parser['motion'][i+47:i+111]
        try:
            result[-1]["name"] = result[-1]["name"].decode("cp932")
        except:
            pass
        
        result[-1]["frame"] = int.from_bytes(result[-1]["frame"],"little")
        
        x,y,z = [struct.unpack('f', result[-1]["position"][i:i+4])[0] for i in range(0,12,4)]
        result[-1]["position"] = [x,y,z]
        
        x,y,z,w = [struct.unpack('f', result[-1]["quaternion"][i:i+4])[0] for i in range(0,16,4)]
        result[-1]["quaternion"] = [x,y,z,w]
        
    return result

def ikreader(ik_):
    totalresult = []
    for ik__ in ik_:
        result = []
        ik = ik__["ik"]
        for k in range(0,len(ik),21):
            result.append({})
            result[-1]["name"] = ik[k:k+20]
            result[-1]["enable"] = int.from_bytes(ik[k+20:k+21],"little")
            
            try:
                result[-1]["name"] = result[-1]["name"].decode("cp932")
            except:
                pass
        content = {}
        content['ikcount'] = ik__['ikcount']
        content['ikshow'] = ik__['ikshow']
        content['iknumber'] = ik__['iknumber']
        content['ik'] = result
        totalresult.append(content)
        
    return totalresult

vmd = vmdread("b.vmd")
motion = motionreader(vmd)
ik = ikreader(vmd["ik"])

vmdc = vmd.copy()
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
