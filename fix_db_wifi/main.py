import argparse
import json
import os
import subprocess
import webbrowser
from ipaddress import ip_network, ip_interface


# Open DB website to authenticate again after fixing the conflict
def open_DB_URL():
    webbrowser.open('http://wifionice.de')


def temporary_mode():
    print("Running in temporary mode...")
    networks = subprocess.getoutput('docker network ls -q').split('\n')
    for network in networks:
        inspect_cmd = f'docker network inspect {network} --format "{{{{.Driver}}}} {{{{range .IPAM.Config}}}}{{{{' \
                      f'.Subnet}}}}{{{{end}}}}"'
        inspection_result = subprocess.getoutput(inspect_cmd)

        # Extract the driver and IP range from the inspection result
        driver, ip_range = inspection_result.split(" ", 1)

        # Skip if it's a pre-defined network
        if driver in ["bridge", "host", "none"]:
            continue

        # Skip if ip_range is an empty string or does not contain '/'
        if not ip_range or '/' not in ip_range:
            continue

        # Extract the first IP address from the range
        ip = ip_interface(ip_range.split('/')[0])

        # Check if the IP is within the conflicting network
        if ip in ip_network('192.168.0.0/16'):
            subprocess.run(['docker', 'network', 'rm', network])
            print(f"Removed network {network} with range {ip_range}")
    open_DB_URL()


def permanent_mode():
    print("Running in permanent mode...")
    # Check if the script is run as root
    if os.geteuid() != 0:
        exit("You need to have root privileges to run this script.\nPlease try again, using 'sudo -E fix_db_wifi'.")
    # Read the existing config
    try:
        with open('/etc/docker/daemon.json', 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        config = {}
    except json.JSONDecodeError:
        print("Existing config is not valid JSON; starting with an empty config.")
        config = {}

    # Modify the config
    config["default-address-pools"] = [{"base": "192.168.0.0/16", "size": 24}]

    # Write the modified config back to the file
    with open('/etc/docker/daemon.json', 'w') as f:
        json.dump(config, f, indent=4)

    subprocess.run(['systemctl', 'restart', 'docker'])
    print("Docker service restarted.")
    open_DB_URL()


def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Manage IP conflict resolution between DB, Ubuntu & Docker.')
    parser.add_argument('-t', '--temporary', action='store_true', default=True,
                        help='temporarily fix the connection issue by removing conflicting docker networks')
    parser.add_argument('-p', '--permanent', action='store_true',
                        help='Permanently fix the connection issue by modifying dockers default address pools.')
    args = parser.parse_args()

    # Run the correct function based on the passed arguments
    if args.permanent:
        permanent_mode()
    else:
        temporary_mode()


if __name__ == '__main__':
    main()
