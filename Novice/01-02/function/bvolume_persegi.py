def ls_persegi(sisi):
    luas = sisi * sisi
    return luas

def vol_persegi(sisi):
    volume = ls_persegi(sisi) * sisi
    return volume

print(vol_persegi(6))