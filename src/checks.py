import shutil
import psutil
import socket

from pathlib import Path

def check_system_health(system_path: Path) -> list[float]:
    if not system_path:
        return f"Error: invalid system path"
    
    results = []

    dsk = shutil.disk_usage(system_path)
    results.append(dsk.used / dsk.total)

    mem = psutil.virtual_memory()
    results.append(mem.total - mem.available) / mem.total * 100
    results.append(mem.total)

    tup = psutil.getloadavg()
    results.append(tup[0])

    return results

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