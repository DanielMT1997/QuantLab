# Sprint 2 Report

## Periodo

13–19 julio 2026

## Objetivo del sprint

Construir un primer backtester simple y reutilizable para evaluar estrategias cuantitativas de forma ordenada.

El objetivo no era encontrar una estrategia rentable, sino separar claramente los elementos fundamentales de un backtest:

- datos;
- precios;
- rendimientos;
- posiciones;
- rendimientos de estrategia;
- curva de capital;
- métricas de rendimiento y riesgo.

## Idea central

La idea central del sprint ha sido que una estrategia no captura automáticamente todos los rendimientos del activo.

Una estrategia captura el rendimiento del activo solo cuando está posicionada.

Por eso hemos separado:

```python
returns           # rendimientos diarios del activo
position          # exposición de la estrategia
strategy_returns  # rendimientos capturados por la estrategia