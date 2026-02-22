from __future__ import annotations

import argparse
from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Treino YOLOv8 (opcional) para componentes de arquitetura.")
    p.add_argument("--data", default="dataset.yaml", help="Arquivo dataset.yaml (formato Ultralytics).")
    p.add_argument("--epochs", type=int, default=30)
    p.add_argument("--imgsz", type=int, default=640)
    p.add_argument("--model", default="yolov8n.pt", help="Checkpoint base.")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    model = YOLO(args.model)
    model.train(data=args.data, epochs=args.epochs, imgsz=args.imgsz)
    # O melhor peso vai para runs/detect/train/weights/best.pt
    print("[OK] Treino finalizado. Copie best.pt para model/yolov8_custom.pt")


if __name__ == "__main__":
    main()
