from pathlib import Path
from .checks import check_system_health, check_internet, check_dns

def system_output(system_path: Path):
    if not system_path:
        return f"invalid system path"
    health = check_system_health(system_path)
    print(
        f"✓ Disk /    {health[0]} used",
        f"✓ Memory    {health[1]} / {health[2]} GB",
        f"✓ Load      {health[3]}",
        f"✓ Internet  {'reachable' if check_internet() else 'unreachable'}",
        f"✓ DNS       {'working' if check_dns() else 'down'}",
        sep="\n"

    )

    

