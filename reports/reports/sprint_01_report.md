# Sprint 1 Report

## Periodo

6–12 julio 2026

## Objetivo del sprint

Construir un entorno mínimo de trabajo reproducible y descargar los primeros datos históricos para empezar el laboratorio cuantitativo.

## Trabajo realizado

Durante este sprint he:

- preparado el entorno local de Python;
- creado el archivo `requirements.txt`;
- creado el archivo `.gitignore`;
- instalado las librerías básicas del proyecto;
- descargado datos históricos diarios de SPY;
- guardado los datos en formato CSV;
- creado una primera exploración de los datos;
- calculado rendimientos simples y logarítmicos;
- calculado estadísticas básicas de rendimientos;
- calculado volatilidad diaria y anualizada;
- construido una estrategia base de buy and hold;
- calculado rentabilidad total;
- calculado rentabilidad anualizada;
- calculado drawdown y máximo drawdown.

## Archivos principales creados

- `requirements.txt`
- `.gitignore`
- `notebooks/01_descarga_datos.ipynb`
- `notebooks/02_exploracion_inicial.ipynb`
- `notebooks/03_buy_and_hold.ipynb`
- `data/raw/SPY_daily.csv`
- `journal/2026-07-06.md`
- `journal/2026-07-07.md`
- `journal/2026-07-08.md`
- `journal/2026-07-09.md`
- `journal/2026-07-10.md`

## Datos utilizados

El activo estudiado ha sido SPY, un ETF que replica el S&P 500.

Se han usado datos diarios desde 1993 hasta la fecha más reciente disponible en la descarga.

La columna principal utilizada para el análisis ha sido `Adj Close`, porque incorpora ajustes por dividendos, splits y otros eventos.

## Resultados principales

La exploración inicial muestra que SPY tiene una tendencia creciente de largo plazo, pero también presenta caídas importantes durante periodos de crisis.

Los rendimientos diarios fluctúan alrededor de cero y muestran ruido considerable a escala diaria.

La media diaria de los rendimientos es pequeña en comparación con la volatilidad diaria.

La estrategia buy and hold sirve como primer benchmark del proyecto.

La curva de capital permite visualizar cuánto habría crecido una unidad monetaria invertida al inicio del periodo.

El drawdown permite observar las caídas desde máximos anteriores y muestra el riesgo temporal de mantener la inversión.

## Conceptos aprendidos

Durante este sprint he trabajado con los siguientes conceptos:

- entorno virtual de Python;
- `requirements.txt`;
- `.gitignore`;
- uso básico de GitHub Desktop;
- notebooks de Jupyter;
- descarga de datos financieros con `yfinance`;
- diferencia entre precio y rendimiento;
- rendimiento simple;
- rendimiento logarítmico;
- volatilidad diaria;
- volatilidad anualizada;
- curva de capital;
- rentabilidad total;
- rentabilidad anualizada;
- drawdown;
- máximo drawdown.

## Problemas encontrados

Durante el sprint aparecieron varios problemas técnicos:

- confusión inicial entre GitHub web, GitHub Desktop, VS Code y terminal;
- error al intentar ejecutar código Python directamente en PowerShell;
- necesidad de instalar las extensiones de Python y Jupyter en VS Code;
- problema de activación del entorno virtual en PowerShell por la política de ejecución de scripts;
- aparición de columnas jerárquicas al descargar datos con `yfinance`.

Todos estos problemas fueron resueltos durante el sprint.

## Conclusiones

El Sprint 1 ha construido la base mínima del laboratorio cuantitativo.

El proyecto ya puede:

- descargar datos históricos;
- guardarlos localmente;
- leerlos desde notebooks;
- calcular rendimientos;
- analizar una estrategia pasiva;
- medir rentabilidad y riesgo básicos.

El resultado más importante no es todavía financiero, sino metodológico: el proyecto ya tiene una estructura reproducible para seguir investigando.

## Próximo sprint

El Sprint 2 debería centrarse en construir un primer backtester simple.

El objetivo será convertir la lógica de buy and hold en una estructura más general que luego pueda reutilizarse con estrategias activas, como medias móviles.


En el notebook `03_buy_and_hold.ipynb`, la estrategia buy and hold obtuvo aproximadamente:

- rentabilidad total: 2988.6731422303774%;
- rentabilidad anualizada: 10.812041382383942%;
- volatilidad anualizada: 18.57318039553563%;
- máximo drawdown: -55.18944909837373%.

En el periodo analizado, la estrategia buy and hold sobre SPY obtuvo una rentabilidad total aproximada del 2988.67%, lo que equivale a multiplicar el capital inicial por unas 30.89 veces.

La rentabilidad anualizada fue aproximadamente del 10.81%, un resultado elevado para una estrategia pasiva de largo plazo.

La volatilidad anualizada fue del 18.57%, lo que indica una variabilidad significativa, coherente con una inversión en renta variable.

El máximo drawdown fue aproximadamente del -55.19%, lo que muestra que, aunque la estrategia fue rentable a largo plazo, el inversor habría tenido que soportar caídas temporales muy severas.

La principal conclusión es que buy and hold en SPY ha sido históricamente una estrategia muy rentable, pero no exenta de riesgo. Su dificultad no está en la implementación, sino en la capacidad de mantener la posición durante crisis profundas.