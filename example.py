def vmdread(file):
    result = {}
    f = open(file,"rb")
    header = f.read(30) ; result["headers"] = header
    name = f.read(20) ; result["name"] = name
    motioncount = int.from_bytes(f.read(4),"little") ; result["motioncount"] = motioncount
    motion = f.read(motioncount*111) ; result["motion"] = motion
    morphcount = int.from_bytes(f.read(4),"little") ; result["morphcount"] = morphcount
    morph = f.read(morphcount*23) ; result["morph"] = morph
    cameracount = int.from_bytes(f.read(4),"little") ; result["cameracount"] = cameracount
    camera = f.read(cameracount*61) ; result["camera"] = camera
    lightcount = int.from_bytes(f.read(4),"little") ; result["lightcount"] = lightcount
    light = f.read(lightcount*61) ; result["light"] = light
    shadowcount = int.from_bytes(f.read(4),"little") ; result["shadowcount"] = shadowcount
    shadow = f.read(shadowcount*61) ; result["shadow"] = shadow
    ikcount = int.from_bytes(f.read(4),"little")
    ikshow = int.from_bytes(f.read(1),"little")
    iknumber = int.from_bytes(f.read(4),"little")
    ik = f.read(iknumber*21)
    result["ikcount"] = ikcount
    result["ikshow"] = ikshow
    result["iknumber"] = iknumber
    result["ik"] = ik
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
        x,y,z = [int.from_bytes(result[-1]["position"][i:i+3],"little") for i in range(0,9,3)]
        result[-1]["position"] = [x,y,z]
    return result

def ikreader(ik):
    result = []
    for k in range(0,len(ik),21):
        result.append({})
        result[-1]["name"] = ik[k:k+20]
        result[-1]["enable"] = int.from_bytes(ik[k+20:k+21],"little")
        try:
            result[-1]["name"] = result[-1]["name"].decode("cp932")
        except:
            pass
    return result

vmd = vmdread("13.vmd")
motion = motionreader(vmd)
ik = ikreader(vmd["ik"])

print(vmd)
print(motion)
print(ik)
