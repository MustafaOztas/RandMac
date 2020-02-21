import subprocess
import optparse

def get_user_input():
    parse = optparse.OptionParser()
    parse.add_option("-i",dest="interface",help="Değiştirmek İçin Bir Arayüz")
    parse.add_option("-m",dest="mac_adresi",help="Yeni Mac Adresi")

    return parse.parse_args()


def mac_değistici(user_int,user_mac):
    subprocess.call(["ifconfig",user_int,"down"])
    subprocess.call(["ifconfig",user_int,"hw","ether",user_mac])
    subprocess.call(["ifconfig",user_int,"up"])

def mac_kontrol():
    ifconfig = subprocess.check_output(["ifconfig",interface])
    print(ifconfig)

print("Mac Değiştirici Başlatıldı!")

(user_input,arguments) = get_user_input()
mac_değistici(user_input.interface,user_input.mac_adresi)
mac_kontrol(user_input.interface)