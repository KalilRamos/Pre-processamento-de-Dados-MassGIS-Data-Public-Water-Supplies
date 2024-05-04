import numpy as np


print(dados[:5])
print(dados.shape)
print(dados.dtype)
print(np.isnan(dados).sum())

dados_sem_nan = np.nan_to_num(dados, nan=np.nanmean(dados, axis=0))

def min_max_normalization(data):
    min_val = np.min(data)
    max_val = np.max(data)
    normalized_data = (data - min_val) / (max_val - min_val)
    return normalized_data

dados_normalizados = min_max_normalization(dados)


def z_score_normalization(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    normalized_data = (data - mean) / std_dev
    return normalized_data

dados_normalizados_z_score = z_score_normalization(dados)

