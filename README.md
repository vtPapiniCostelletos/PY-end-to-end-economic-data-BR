This is the flow of the project:

            API ────> Apache Airflow
                             │
                             ▼
                           Python
                      Extração das APIs
                             │
                             ▼
                        RustFS — RAW
                      Dados originais
                             │
                             ▼
                       Apache Spark
                  Limpeza e transformação
                             │
                             ▼
                      RustFS — Parquet
                     Dados processados
                             │
                             ▼
                         PostgreSQL
                      Data Warehouse
                             │
                             ▼
                            dbt
                  Modelagem SQL analítica
                   ┌─────────┴─────────┐
                   ▼                   ▼
             Tabelas fato       Tabelas dimensão
                   └─────────┬─────────┘
                             ▼
                          Power BI
                       Visualização

Goal Visualization: Analise and compare the differents types of the index of unaployment from BRAZIL.

                 Economic Data
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
        Y          C + I + G           X - M
        │               │                │
        └───────────────┼────────────────┘
                        ▼
DEMONSTRATING   Economic activity
                        vs
CONSULTING      Unaployment types


Y_{calculado}=C+I+G+(X-M)

e comparar com o PIB oficial:

Y_{oficial}

Depois analisar:

Taxa\ de\ desemprego
\quad \text{vs.} \quad
Crescimento\ do\ PIB

E podemos ir além
Uma análise interessante para o projeto seria verificar a Lei de Okun, que relaciona mudanças no desemprego com o crescimento econômico.

Por exemplo:

\Delta Desemprego = \alpha + \beta \cdot Crescimento_{PIB} + \epsilon

