from __future__ import annotations

from pathlib import Path
from typing import List, Tuple, Dict

from ultralytics import YOLO


# Componente alvo do MVP (treino supervisionado)
TARGET_CLASSES = ["user", "api_gateway", "load_balancer", "app_server", "database", "waf", "cdn", "observability", "idp_auth", "external_system"]


def _load_model(model_path: str) -> YOLO:
    p = Path(model_path)
    if p.exists() and p.stat().st_size > 0:
        return YOLO(str(p))
    # Padrão: YOLOv8n pré-treinado (sempre usado) – pode não detectar ícones de arquitetura,
    # mas mantém o requisito de pipeline com YOLO como etapa principal.
    return YOLO("yolov8n.pt")


def detect_regions(image_path: str, model_path: str) -> List[Tuple[int,int,int,int]]:
    """Usa YOLOv8 para propor regiões (bboxes) no diagrama.
    Retorna lista de (x1,y1,x2,y2)."""
    model = _load_model(model_path)
    results = model(image_path, verbose=False)

    boxes = []
    if len(results) == 0:
        return boxes

    for b in results[0].boxes:
        x1, y1, x2, y2 = b.xyxy[0].tolist()
        boxes.append((int(x1), int(y1), int(x2), int(y2)))

    return boxes
