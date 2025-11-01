# VMD-PARSER
python read vmd

```py
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
    if ikcount>0:
        iknumber = int.from_bytes(f.read(5),"little")
    else:
        iknumber = 0
    ikbyte= (9+21*iknumber)
    result["ikcount"] = ikcount
    result["ikbyte"] = ikbyte
    result["iknumber"] = iknumber
    try:
        ik = f.read(ikcount*ikbyte) ; result["ik"] = ik
    except MemoryError:
        result["ik"] = "this vmd ik not for this script"
        pass
    end = f.read(-1) ; result["end"] = end
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

vmd = vmdread("13.vmd")
motion = motionreader(vmd)
```

reference

https://github.com/syoyo/MMDLoader/blob/master/vmd_reader.cc

https://github.com/59naga/vpvp-vmd/blob/master/src/reader.coffee
