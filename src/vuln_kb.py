from __future__ import annotations
from typing import Dict, List

# Mini knowledge-base (MVP+) para "nota 10":
# 1) ameaça STRIDE por componente
# 2) exemplos de vulnerabilidades comuns
# 3) contramedidas objetivas

KB: Dict[str, Dict[str, List[str] | str]] = {
    "user": {
        "stride": ["Spoofing", "Repudiation"],
        "vulns": ["Phishing / credenciais vazadas", "Sessão sequestrada", "Requisições sem não-repúdio"],
        "controls": "MFA, OAuth/OIDC, device trust, logs e trilha de auditoria com carimbo de tempo."
    },
    "api_gateway": {
        "stride": ["Tampering", "Denial of Service", "Information Disclosure"],
        "vulns": ["BOLA/Broken Access Control", "Rate limiting ausente", "Exposição de endpoints admin"],
        "controls": "WAF/API Gateway policies, authz (RBAC/ABAC), rate limiting, schema validation, mTLS."
    },
    "load_balancer": {
        "stride": ["Denial of Service", "Tampering"],
        "vulns": ["DDoS", "TLS fraco / ciphers inseguras", "Falta de health-check"],
        "controls": "Proteção DDoS, TLS modernizado, health checks, autoscaling, circuit breaker."
    },
    "app_server": {
        "stride": ["Elevation of Privilege", "Tampering", "Repudiation"],
        "vulns": ["RCE por dependências", "Config secreta exposta", "Logs insuficientes"],
        "controls": "Hardening, secrets manager, SAST/DAST, patching, least privilege, audit logging."
    },
    "database": {
        "stride": ["Information Disclosure", "Tampering", "Denial of Service"],
        "vulns": ["SQLi", "Dump não criptografado", "Privilégios excessivos"],
        "controls": "Criptografia, RBAC, network segmentation, backups, WAF, prepared statements."
    },
    "idp_auth": {
        "stride": ["Spoofing", "Tampering"],
        "vulns": ["Tokens mal configurados", "SSO sem validação adequada"],
        "controls": "OIDC correto, validação de issuer/audience, rotação de chaves, MFA, Conditional Access."
    },
    "observability": {
        "stride": ["Repudiation", "Information Disclosure"],
        "vulns": ["Logs com PII", "Ausência de trilha de auditoria"],
        "controls": "Mascaramento/Redação de PII, acesso restrito aos logs, retenção e integridade (WORM)."
    },
    "external_system": {
        "stride": ["Spoofing", "Tampering", "Information Disclosure"],
        "vulns": ["Integração sem assinatura", "Webhooks sem validação", "Dados sensíveis expostos"],
        "controls": "mTLS, assinatura HMAC, allowlist, validação de payload, contratos e SLAs."
    },
    "waf": {
        "stride": ["Denial of Service", "Tampering"],
        "vulns": ["Regras fracas/inexistentes", "Bypass por payloads"],
        "controls": "Regras OWASP CRS, tuning de regras, proteção DDoS, bot protection."
    },
    "cdn": {
        "stride": ["Information Disclosure", "Denial of Service"],
        "vulns": ["Cache poisoning", "TLS downgrade", "Config incorreta de cache"],
        "controls": "Headers corretos, cache key hardening, TLS moderno, rate limiting e shielding."
    }
}
