import socket
import xml.etree.ElementTree as ET

# Juliusと接続 --- (*1)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def julius_connect():
    HOST = "localhost"
    PORT = 10500
    client.connect((HOST, PORT))

# Juliusからデータを連続で受信する --- (*2)
def julius_recv(callback):
    tmp = bytes()
    try:
            # XML形式でデータを受け取る --- (*3)
            buf = client.recv(1024)
            tmp += buf
            # \n.\n がJuliusの区切り文字
            n = tmp.find(b"\n.\n")
            if n < 0: continue
            line = tmp[:n].decode("utf-8")
            tmp = tmp[n+3:]
            # print(line) # 受信したXML
            # 切り取ったデータをXMLとして処理 --- (*4)
            root = ET.fromstring(line)
            if root.tag != "RECOGOUT": continue
            shypo = root[0]
            # 認識した語句を取り出す
            words = []
            for whypo in shypo:
                words.append(whypo.attrib['WORD'])
            # 最初と最後は[s]..[/s]なので削る --- (*5)
            words = words[1:len(words)-1]
            if callback(words) == False:
                break
        except KeyboardInterrupt:
            break
    socket.close()
    return

# 受信した時に実行する関数を定義した --- (*6)
def test_callback(words):
    print("認識した語句=", words)
    return True

# メイン --- (*7)
if __name__ == "__main__":
    julius_connect()
    julius_recv(test_callback)