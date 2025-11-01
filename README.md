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
    ik = f.read(ikcount*ikbyte) ; result["ik"] = ik
    end = f.read(-1) ; result["end"] = end
    return result
```

reference

https://github.com/syoyo/MMDLoader/blob/master/vmd_reader.cc

https://github.com/59naga/vpvp-vmd/blob/master/src/reader.coffee
