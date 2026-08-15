from pathlib import Path
from src.checks import (
    check_system_health, 
    check_internet, 
    check_dns
)

def system_output(system_path: Path) -> str:
    if system_path != Path("/"):
        raise ValueError("invalid system path")
    
    health = check_system_health(system_path)
    return ( 
        f"✓ Disk /    {health[0]}% used\n",
        f"✓ Memory    {health[1]} / {health[2]} GB\n",
        f"✓ Load      {health[3]}\n",
        f"✓ Internet  {'resolved' if check_internet() else 'unresolved'}\n",
        f"✓ DNS       {'working' if check_dns() else 'down'}",
    )


    

