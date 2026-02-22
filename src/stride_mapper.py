from __future__ import annotations
from typing import Dict, List
from src.vuln_kb import KB

def map_stride(components: List[str]) -> Dict[str, List[str]]:
    out: Dict[str, List[str]] = {}
    for c in components:
        out[c] = list(KB.get(c, {}).get("stride", []))  # type: ignore[arg-type]
    return out
