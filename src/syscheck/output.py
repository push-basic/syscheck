from pathlib import Path
from syscheck.checks import (
    check_system_health, 
    check_internet, 
    check_dns
)

def system_output(system_path: Path) -> str:
    if system_path != Path("/"):
        raise ValueError("invalid system path")
    
    health = check_system_health(system_path)
    return "\n".join([
        f"Syscheck",
        f"--------------------------",
        f"✓ Disk /    {health[0]:.2f}% used",
        f"✓ Memory    {health[1]:.2f} / {health[2]:.2f} GB",
        f"✓ Load      {health[3]:.2f}",
        f"✓ Internet  {'reachable' if check_internet() else 'unreachable'}",
        f"✓ DNS       {'resolved' if check_dns() else 'unresolved'}"
    ])


    

