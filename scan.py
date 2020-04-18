import yaml
import mei

with open('vocablary.yaml') as file:
    talk = yaml.safe_load(file)



def scan(text):
    with open('vocablary.yaml') as file:
        talk = yaml.safe_load(file)
    i = 0
    p = 0
    n = str(talk['end'])
    while i <= int(n):
        if text == talk[i][0]:
            text = talk[i][2]
            if talk[i][1] == 'n':
                mei.jtalk_normal(text)
            elif talk[i][1] == 'h':
                mei.jtalk_happy(text)
            elif talk[i][1] == 'a':
                mei.jtalk_angry(text)
            elif talk[i][1] == 's':
                mei.jtalk_sad(text)
            elif talk[i][1] == 'b':
                mei.jtalk_bashful
            p = 1
        else:
            i += 1
    if p == 0:
        text = 'すみません。よくわかりません。よかったらボキャブラリーに追加していってください。'
        mei.jtalk_normal(text)
