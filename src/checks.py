import shutil
import psutil
import socket

from pathlib import Path

def check_system_health(system_path: Path) -> list[float]:
    dsk = shutil.disk_usage(system_path)
    disk_used = dsk.used / dsk.total

    mem = psutil.virtual_memory()
    total_memory = mem.total
    percent_memory = (total_memory - mem.available) / total_memory * 100

    tup = psutil.getloadavg()
    load = tup[0]

    return [disk_used, percent_memory, total_memory, load]

def check_internet() -> bool:
    try:
        with socket.create_connection(("8.8.8.8", 53), timeout=3):
            return True
    except OSError:
        return False

def check_dns() -> bool:
    try:
        socket.gethostbyname("https://google.com")
        return True
    except socket.gaierror:
        return False