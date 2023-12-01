import subprocess
import signal

def start_airodump(interface):
    try:
        subprocess.run(['airodump-ng', interface], check=True)
    except subprocess.CalledProcessError:
        pass  # Ignore error when interrupted by CTRL+C

def stop_airodump():
    subprocess.run(['pkill', 'airodump-ng'])

def capture_data(bssid, filename, channel, interface):
    subprocess.run(['airodump-ng', '-w', filename, '-c', channel, '--bssid', bssid, interface])

def main():
    interface = input("Enter the wireless interface in monitor mode (e.g., wlan1mon): ")

    try:
        print("Press CTRL+C to stop scanning.")
        start_airodump(interface)
    except KeyboardInterrupt:
        print("Scanning stopped.")

    bssid = input("Enter the BSSID (MAC address): ")
    channel = input("Enter the channel: ")
    filename = input("Enter the filename for the captured data: ")

    stop_airodump()
    capture_data(bssid, filename, channel, interface)

if __name__ == "__main__":
    main()

