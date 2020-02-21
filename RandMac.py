import subprocess
import optparse

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change!")
    parse_object.add_option("-m", "--mac", dest="mac_adresi", help="new mac address")

    return parse_object.parse_args()


def mac_degistirici(user_int,user_mac):
    subprocess.call(["ifconfig",user_int,"down"])
    subprocess.call(["ifconfig",user_int,"hw","ether",user_mac])
    subprocess.call(["ifconfig",user_int,"up"])

def mac_kontrol(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    print(ifconfig)

print("Mac Changer Started!")

(user_input,arguments) = get_user_input()
mac_degistirici(user_input.interface,user_input.mac_adresi)
mac_kontrol(user_input.interface)
