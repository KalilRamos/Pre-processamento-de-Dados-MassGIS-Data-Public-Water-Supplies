import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo (substitua pelos seus dados reais)
capacidade = np.random.normal(1000, 300, 100)  # Capacidade de produção de água em unidades

# Criar histograma da capacidade de produção de água
plt.figure(figsize=(8, 6))
plt.hist(capacidade, bins=20, color='skyblue', edgecolor='black')
plt.title('Distribuição da Capacidade de Produção de Água')
plt.xlabel('Capacidade de Produção (unidades)')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

