from pathlib import Path
from .checks import check_system_health

def system_output(system_path: Path) -> str:
    usage = check_system_health(system_path)
    percentage = usage * 100
    return f"Disk /     {percentage:.1f}%"