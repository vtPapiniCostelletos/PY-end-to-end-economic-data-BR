## Flow of the project:

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

Taxa de desemprego
quad vs. quad
Crescimento do PIB

E podemos ir além
Uma análise interessante para o projeto seria verificar a Lei de Okun, que relaciona mudanças no desemprego com o crescimento econômico.

Por exemplo:

Delta Desemprego = alpha + beta cdot Crescimento_{PIB} + epsilon


# END POINTS

### Remember* 

| Symbol | Meaning |
|---|---|
| **Y** | GDP |
| **C** | Household consumption |
| **I** | Investment |
| **G** | Government expenditure |
| **X** | Exports |
| **M** | Imports |
| **U** | Unemployment rate |
| **E** | Employed population |

- **Y = C + I + G +(X-M)** 
- **& U** 
- **& E**

| Category | Source | Key Indicators |
|---|---|---|
| Economic activity | World Bank | GDP and economic growth |
| Consumption and investment | World Bank | Household consumption and gross capital formation |
| Public sector | World Bank | Government consumption expenditure |
| International trade | World Bank | Exports and imports |
| Labor market | World Bank | Unemployment rate and employed population |



#### By World Bank:

| Indicador | Código | Variável |
|---|---|---|
| GDP — Gross Domestic Product | `NY.GDP.MKTP.CD` | PIB em dólares correntes |
| Household Consumption | `NE.CON.PRVT.ZS` | Consumo das famílias (% do PIB) |
| Gross Capital Formation | `NE.GDI.TOTL.ZS` | Formação bruta de capital (% do PIB) |
| Government Consumption | `NE.CON.GOVT.ZS` | Consumo do governo (% do PIB) |
| Exports | `NE.EXP.GNFS.ZS` | Exportações (% do PIB) |
| Imports | `NE.IMP.GNFS.ZS` | Importações (% do PIB) |
| Unemployment Rate | `SL.UEM.TOTL.ZS` | Taxa de desemprego (% da força de trabalho) |
| Employment in Industry | `SL.IND.EMPL.ZS` | Emprego na indústria (% do emprego total) |
| Employment in Services | `SL.SRV.EMPL.ZS` | Emprego nos serviços (% do emprego total) |


