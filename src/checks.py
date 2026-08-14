import shutil
from pathlib import Path

def check_system_health(system_path: Path) -> float:
    disk_usage = shutil.disk_usage(system_path)
    usage = disk_usage.used / disk_usage.total
    return usage