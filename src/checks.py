import shutil
import psutil
import socket

from pathlib import Path

def check_system_health(system_path: Path) -> list[float]:
    if system_path != Path("/"):
        raise ValueError("invalid system path")
    
    results = []

    dsk = shutil.disk_usage(system_path)
    results.append(dsk.used / dsk.total * 100)

    mem = psutil.virtual_memory()
    results.append((mem.total - mem.available) / (1024 ** 3))
    results.append(mem.total / (1024 ** 3))

    load = psutil.getloadavg()
    results.append(float(load[0]))

    return results

def check_internet() -> bool:
    try:
        with socket.create_connection(("8.8.8.8", 53), timeout=3):
            return True
    except OSError:
        return False

def check_dns() -> bool:
    try:
        socket.gethostbyname("google.com")
        return True
    except socket.gaierror:
        return False