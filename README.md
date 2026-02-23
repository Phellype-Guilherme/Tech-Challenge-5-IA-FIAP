# 🧠 Tech Challenge – Modelagem de Ameaças com IA (Visão Computacional)

Este projeto foi desenvolvido como parte do **Tech Challenge da FIAP (Fase 5 – Software Security e Inteligência Artificial)** e tem como objetivo a criação de uma **aplicação de análise automática de diagramas de arquitetura de software**, utilizando técnicas de **Visão Computacional, Deep Learning e Threat Modeling**.

A aplicação é capaz de:

- Identificar automaticamente componentes em diagramas de arquitetura
- Interpretar visualmente elementos como usuários, APIs, servidores, bancos de dados e sistemas externos
- Aplicar a metodologia **STRIDE** para identificação de ameaças
- Identificar vulnerabilidades associadas a cada componente
- Gerar automaticamente um relatório estruturado de modelagem de ameaças com contramedidas recomendadas

---

## 🎯 Objetivo do Projeto

Aplicar na prática os conhecimentos adquiridos ao longo da fase, integrando técnicas de **Visão Computacional e Inteligência Artificial** para realizar a **modelagem automática de ameaças em sistemas**, simulando cenários reais baseados em arquiteturas modernas.

A solução demonstra como a IA pode auxiliar arquitetos e desenvolvedores na identificação proativa de riscos de segurança ainda na fase de design do sistema.

---

## 📁 Estrutura do Projeto

```
Tech-Challenge-5-IA-FIAP/
│
├── data/
│   ├── raw/
│   │   ├── arch1.png
│   │   └── arch2.png
│   │
│   ├── labeled/
│   │
│   └── test/
│       ├── arch1.png
│       └── arch2.png
│
├── model/
│   └── yolov8_custom.pt
│
├── reports/
│   ├── aws/
│   └── azure/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── diagram_extractor.py
│   ├── yolo_detector.py
│   ├── stride_mapper.py
│   ├── vuln_kb.py
│   ├── report_generator.py
│   └── utils/
│       ├── __init__.py
│       └── image_hash.py
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Como Executar

### 1) Criar ambiente virtual

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -U pip
```

---

### 2) Instalar dependências

```powershell
pip install -r requirements.txt
```

---

### 3) Executar o sistema arquitetura AWS e AZURE

```powershell
python -m src.main --image "data/test/arch1.png" --out "reports/aws"

python -m src.main --image "data/test/arch2.png" --out "reports/azure"
```

---

## 📊 Saídas Geradas

Após a execução, o sistema gera automaticamente os seguintes arquivos:

---

### 📄 threat_report.txt

Relatório detalhado contendo:

- Componentes identificados na arquitetura
- Ameaças classificadas utilizando a metodologia STRIDE
- Vulnerabilidades associadas a cada componente
- Contramedidas recomendadas

Este arquivo é utilizado como documento principal de análise de segurança.

---

### 📄 threat_report.json

Arquivo estruturado contendo:

- Lista completa de componentes detectados
- Classificação STRIDE
- Vulnerabilidades
- Contramedidas

Este formato permite integração com outras ferramentas e auditoria automatizada.

---

## 🧠 Técnicas Utilizadas

### 1) Detecção de Componentes Arquiteturais

- **YOLOv8 (Ultralytics)** para identificação de regiões relevantes no diagrama
- Extração visual de elementos arquiteturais

---

### 2) Interpretação Semântica

- **OCR (Reconhecimento Óptico de Caracteres)** para leitura dos rótulos
- Normalização e classificação dos componentes detectados

---

### 3) Modelagem de Ameaças

Aplicação da metodologia **STRIDE**, que classifica ameaças em:

- Spoofing
- Tampering
- Repudiation
- Information Disclosure
- Denial of Service
- Elevation of Privilege

---

### 4) Base de Conhecimento de Segurança

O sistema consulta uma base contendo:

- Vulnerabilidades comuns
- Controles de segurança recomendados
- Contramedidas específicas por tipo de componente

---

## 📚 Bibliotecas Principais

- **ultralytics** – Implementação do YOLOv8
- **opencv-python** – Processamento de imagens
- **pytesseract** – Reconhecimento de texto em imagens
- **numpy** – Operações numéricas
- **pandas** – Estruturação de dados
- **matplotlib** – Suporte a visualização
- **pillow** – Manipulação de imagens

---

## 👨‍💻 Autor

**Phellype Guilherme Pereira da Silva**  
**RM:** 361625  
**Projeto:** Pós Tech FIAP – Inteligência Artificial  
**Instituição:** FIAP – Faculdade de Informática e Administração Paulista
