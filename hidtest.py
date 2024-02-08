import hid
import subprocess
import time
    
print("welcome to our embedded project for 2023")
print("HID 4 key keyboard (1,2,3,4)")
print("under supervision of : DR.Hossam")

while True:

    print("1 for enter program 2 for exit")
    x=int(input("please enter 1 or 2\n"))
            # Enumerate connected HID devices
    devices = hid.enumerate()
    password="Dr.hossam"
    # Example VID and PID for the target device
    target_vid = 5824  # Replace with the target device's VID
    target_pid = 10203 # Replace with the target device's PID

    # Check if a specific device with the target VID/PID is in the list
    target_device = None
    for device in devices:
        if device['vendor_id'] == target_vid and device['product_id'] == target_pid:
            target_device = device
            break
    if x ==1:
        
        if target_device is not None:
            print("Target device found:")
            print("password:",password)
            flag = 1
        elif target_device is  None:
            flag = 0
            print("Target device not found.")  
        if flag==1:
            subprocess.run(["notepad.exe"]) 
    elif x==2:
        print("exit successfully")
        time.sleep(1)
        break