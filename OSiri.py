import mei
import time
import yaml
import scan
import skill

def say_something():
    text = input('話しかける:')
    if text == 'ラーメンタイマー' or text == '砂時計':
        skill.ramen()
    elif text == '癒やして':
        skill.care()
    elif text == '計算' or text == '電卓':
        skill.calculation()
    else:
        scan.scan(text)
        
        
    
while True:        
    if __name__ == '__main__':
        say_something()