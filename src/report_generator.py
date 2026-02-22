from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Any
import json

from src.vuln_kb import KB

def build_report(components: List[str], stride: Dict[str, List[str]]) -> Dict[str, Any]:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    items = []
    for c in components:
        meta = KB.get(c, {})
        items.append({
            "component": c,
            "stride": stride.get(c, []),
            "common_vulnerabilities": meta.get("vulns", []),
            "countermeasures": meta.get("controls", ""),
        })
    return {
        "generated_at": now,
        "components_detected": components,
        "items": items,
    }


def render_txt(report: Dict[str, Any]) -> str:
    lines: List[str] = []
    lines.append("RELATÓRIO DE MODELAGEM DE AMEAÇAS (STRIDE)")
    lines.append(f"Gerado em: {report['generated_at']}")
    lines.append("")
    lines.append(f"Componentes detectados: {', '.join(report['components_detected']) or '(nenhum)'}")
    lines.append("")

    for it in report["items"]:
        lines.append(f"Componente: {it['component']}")
        for t in it["stride"]:
            lines.append(f" - Ameaça (STRIDE): {t}")
        if it["common_vulnerabilities"]:
            lines.append(" - Vulnerabilidades comuns:")
            for v in it["common_vulnerabilities"]:
                lines.append(f"   • {v}")
        if it["countermeasures"]:
            lines.append(f" - Contramedidas: {it['countermeasures']}")
        lines.append("")

    return "\n".join(lines)


def save_reports(out_dir: str, report: Dict[str, Any]) -> None:
    from pathlib import Path
    p = Path(out_dir)
    p.mkdir(parents=True, exist_ok=True)

    (p / "threat_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    (p / "threat_report.txt").write_text(render_txt(report), encoding="utf-8")
