# Current State

## Proyecto

QuantLab

## Estado actual

Sprint 2 cerrado.

## Último sprint completado

Sprint 2 — Backtester simple y reutilizable

## Resultado principal

El proyecto ya tiene un primer backtester básico validado.

Se han creado funciones reutilizables para:

- calcular métricas de rendimiento y riesgo;
- calcular rendimientos de estrategia;
- construir curvas de capital;
- ejecutar backtests simples;
- comparar curvas de capital.

## Archivos principales

- `src/metrics.py`
- `src/backtester.py`
- `notebooks/04_backtester_basico.ipynb`
- `notebooks/05_validacion_backtester.ipynb`
- `reports/sprint_02_report.md`

## Conceptos consolidados

- rendimiento diario;
- posición;
- exposición;
- rendimientos de estrategia;
- curva de capital;
- drawdown;
- máximo drawdown;
- rentabilidad anualizada;
- volatilidad anualizada;
- look-ahead bias;
- `position.shift(1)`;
- validación de backtester.

## Próximo sprint

Sprint 3 — Primera estrategia activa: cruce de medias móviles.

## Próximo objetivo

Implementar una estrategia sencilla de medias móviles y compararla contra buy and hold usando el backtester creado en el Sprint 2.
