from pathlib import Path
from .checks import check_system_health, check_internet, check_dns

def system_output(system_path: Path):
    if not system_path:
        return "not a valid path"
    health = check_system_health(system_path)
    internet = check_internet
    dns = check_dns
    

