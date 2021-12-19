from winreg import *
import sys

reg_path = r"SYSTEM\CurrentControlSet\Control\StorageDevicePolicies"


def make_Write_handle():
    CreateKey(HKEY_LOCAL_MACHINE, reg_path)
    reg_handle = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
    return OpenKey(reg_handle, reg_path, 0, KEY_WRITE)


def make_Access_handle():
    CreateKey(HKEY_LOCAL_MACHINE, reg_path)
    reg_handle = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
    return OpenKey(reg_handle, reg_path, 0, KEY_ALL_ACCESS)


def set_value():
    key = make_Write_handle()
    try:
        SetValueEx(key, "WriteProtect", 0, REG_DWORD, 0x1)
        print("Successfully turned ON WriteBlock")
    except:
        print("Problem has occured..")
    CloseKey(key)


def reset_value():
    key = make_Write_handle()
    try:
        SetValueEx(key, "WriteProtect", 0, REG_DWORD, 0x0)
        print("Successfully turned OFF WriteBlock")
    except:
        print("Problem has occured..")
    CloseKey(key)


def find_value():
    key = make_Access_handle()
    try:
        value, _ = QueryValueEx(key, "WriteProtect")
        if value == 1:
            print("WriteBlock is ON")
        else:
            print("WriteBlock is OFF")
    except:
        print("Problem has occured..")
    CloseKey(key)


if len(sys.argv) != 2:
    print("Please select only one option.")
    print(r"EX) on, off, status")
    sys.exit()
param = sys.argv[1]
if param == "on":
    set_value()
if param == "off":
    reset_value()
if param == "status":
    find_value()