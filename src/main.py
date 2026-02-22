from __future__ import annotations

import argparse
from pathlib import Path

from src.diagram_extractor import extract_components
from src.stride_mapper import map_stride
from src.report_generator import build_report, save_reports

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Threat Modeling STRIDE a partir de diagrama (imagem) - MVP Nota 10 (YOLO padrão)")
    p.add_argument("--image", required=True, help="Caminho da imagem do diagrama.")
    p.add_argument("--model", default="model/yolov8_custom.pt", help="Modelo YOLOv8 (custom). Se vazio, usa yolov8n.pt automaticamente.")
    p.add_argument("--out", default="reports", help="Pasta de saída (txt + json).")
    return p.parse_args()


def main() -> None:
    args = parse_args()

    components = extract_components(args.image, model_path=args.model)
    stride = map_stride(components)
    report = build_report(components, stride)
    save_reports(args.out, report)

    print(f"[OK] Componentes detectados: {components}")
    print(f"[OK] Relatórios gerados em: {Path(args.out).resolve()}")


if __name__ == "__main__":
    main()
