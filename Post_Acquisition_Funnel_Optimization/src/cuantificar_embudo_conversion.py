import pandas as pd
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, '..', 'data', 'data.csv')

try:
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en la ruta: {file_path}")
    exit()

df.dropna(subset=['CustomerID'], inplace=True)
df['CustomerID'] = df['CustomerID'].astype(int)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
total_customers = df['CustomerID'].nunique()
total_transactions = df['InvoiceNo'].nunique()
purchase_transactions_df = df[~df['InvoiceNo'].astype(str).str.contains('C', na=False)]
total_purchases_net = purchase_transactions_df['InvoiceNo'].nunique()

customer_purchases_net = purchase_transactions_df.groupby('CustomerID')['InvoiceNo'].nunique()
loyal_customers = customer_purchases_net[customer_purchases_net >= 2].count()

funnel_data = {
    'Etapa': [
        '1. Clientes Únicos',
        '2. Total de Pedidos (Bruto)',
        '3. Pedidos Netos (Completados)',
        '4. Clientes Leales (2+ Compras Netas)'
    ],
    'Cantidad': [
        total_customers,
        total_transactions,
        total_purchases_net,
        loyal_customers
    ]
}
funnel_df = pd.DataFrame(funnel_data)

deliverables_path = os.path.join(script_dir, '..', 'deliverables', 'funnel_analysis_summary.csv')

funnel_df.to_csv(deliverables_path, index=False)

print("\n--- ÉXITO ---")
print(f"Análisis del Embudo Post-Adquisición completado y resumen guardado en:\n{deliverables_path}")
print(funnel_df)