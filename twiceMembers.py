twice = {
                "Debut": 20151020,
                #"Color": "Apricot & Neon Magenta",
                #color apricot (#FCC89B) Neon Magenta (#FF5FA2)
                "Color": '#FCC89B'
}

nayeon = {
                #"Name": "Im Nayeon",
                "Name": "Im Nayeon" or "임나연",
                "Birthday": 19950922,
                "Blood Type": "A",
                #"Color": "sky blue"
                "Color": '#81D4FA'
}

jeongyeon = {
                "Name": "Yoo Jeongyeon" or "유정연",
                "Birthday": 19961101,
                "Blood Type": "O",
                #"Color": "yellow-green"
                "Color": '#AED581'
}

momo = {
                "Name": "Hirai Momo",
                "Birthday": 19961109,
                "Blood Type": "A",
                #"Color": "pink"
                "Color": "#FFCDD2"
}

sana = {
                "Name": "Minatozaki Sana",
                "Birthday": 19961229,
                "Blood Type": "B",
                #"Color": "purple"
                "Color": '#9FA8DA'
}

jihyo = {
                "Name": "Park Jihyo",
                "Birthday": 19970201,
                "Blood Type": "O",
                #"Color": "apricot"
                "Color": 'FFB74D'
}

mina = {
                "Name": "Myoui Mina",
                "Birthday": 19970324,
                "Blood Type": "A",
                #"Color": "mint"
                "Color": '#80CBC4'
}

dahyun = {
                "Name": "Kim Dahyun",
                "Birthday": 19980528,
                "Blood Type": "O",
                #"Color": "white"
                "Color": '#FFFFFF'
}
chaeyoung = {
                "Name": "Son Chaeyoung",
                "Birthday": 19990423,
                "Blood Type": "B", 
                #"Color": "red"
                "Color": '#FF1744'
}

tzuyu = {
                "Name": "Chou Tzuyu",
                "Birthday": 19990614,
                "Blood Type": "A",
                #"Color": "blue"
                "Color": '#0277BD'
}

def getTwice(member):
    #if member == "Nayeon" or '임나연':
    if member == "Nayeon":
        return nayeon
    #if member == "Jeongyeon" or '유정연':
    if member == "Jeongyeon":
        return jeongyeon
    #if member == "Momo" or '모모' or '平井 もも':
    if member == "Momo":
        return momo
    #if member == "Sana" or '사나' or '湊崎 紗夏':
    if member == "Sana":
        return sana
    #if member == "Jihyo" or '박지효':
    if member == "Jihyo":
      return jihyo
    #if member == "Mina" or '미나' or '名井 南':
    if member == "Mina":
        return mina
    #if member == "Dahyun" or '김다현':
    if member == "Dahyun":
        return dahyun
    #if member == "Chaeyoung" or '손채영':
    if member == "Chaeyoung":
        return chaeyoung
    #if member == "Tzuyu" or '쯔위' or '周子瑜:
    if member == "Tzuyu":
        return tzuyu
    