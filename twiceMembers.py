twice = {
                "Debut": 20151020,
                #"Color": "Apricot & Neon Magenta",
                #color apricot (#FCC89B) Neon Magenta (#FF5FA2)
                "Color": '#FCC89B'
}

nayeon = {
                "Name": "Im Nayeon",
                "Birthday": 19950922,
                "Blood Type": "A",
                "Color": "sky blue"
}

jeongyeon = {
                "Name": "Yoo Jeongyeon",
                "Birthday": 19961101,
                "Blood Type": "O",
                "Color": "yellow-green"
}

momo = {
                "Name": "Hirai Momo",
                "Birthday": 19961109,
                "Blood Type": "A",
                "Color": "pink"
}

sana = {
                "Name": "Minatozaki Sana",
                "Birthday": 19961229,
                "Blood Type": "B",
                "Color": "purple"
}

jihyo = {
                "Name": "Park Jihyo",
                "Birthday": 19970201,
                "Blood Type": "O",
                "Color": "apricot"
}

mina = {
                "Name": "Myoui Mina",
                "Birthday": 19970324,
                "Blood Type": "A",
                "Color": "mint"
}

dahyun = {
                "Name": "Kim Dahyun",
                "Birthday": 19980528,
                "Blood Type": "O",
                "Color": "white"
}
chaeyoung = {
                "Name": "Son Chaeyoung",
                "Birthday": 19990423,
                "Blood Type": "B", 
                "Color": "red"
}

tzuyu = {
                "Name": "Chou Tzuyu",
                "Birthday": 19990614,
                "Blood Type": "A",
                "Color": "blue"
}

def getTwice(member):
    if member == "Nayeon" or '나연':
        return nayeon
    if member == "Jeongyeon" or '정연':
        return jeongyeon
    if member == "Momo" or '모모':
        return momo
    if member == "Sana" or '사나':
        return sana
    if member == "Jihyo" or '지효':
      return jihyo
    if member == "Mina" or '미나':
        return mina
    if member == "Dahyun" or '다현':
        return dahyun
    if member == "Chaeyoung" or '채영':
        return chaeyoung
    if member == "Tzuyu" or '쯔위':
        return tzuyu
    