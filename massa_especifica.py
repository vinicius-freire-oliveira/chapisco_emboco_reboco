def calcular_consumo_cimento(traco, massas_especificas, relacao_ac):
    # Extrair as proporções do traço
    proporcao_cimento, proporcao_cal, proporcao_areia = traco
    massa_especifica_cimento, massa_especifica_cal, massa_especifica_areia = massas_especificas

    # Dividir cada massa específica por 1000
    massa_especifica_cimento /= 1000
    massa_especifica_cal /= 1000
    massa_especifica_areia /= 1000

    # Cálculo do consumo de cimento (C)
    # Fórmula: C = 1000 / (proporcao_cimento/massa_especifica_cimento + proporcao_cal/massa_especifica_cal + proporcao_areia/massa_especifica_areia + relacao_ac)
    C = 1000 / (proporcao_cimento/massa_especifica_cimento + proporcao_cal/massa_especifica_cal + proporcao_areia/massa_especifica_areia + relacao_ac)

    return C

def main():
    # Definir o traço da argamassa (proporção cimento:cal:areia)
    traco = (1, 2, 8)  # Cimento:Cal:Areia

    # Definir as massas específicas dos materiais (em kg/m³)
    massa_especifica_cimento = 3100  # kg/m³
    massa_especifica_cal = 2500      # kg/m³
    massa_especifica_areia = 2700    # kg/m³
    massas_especificas = (massa_especifica_cimento, massa_especifica_cal, massa_especifica_areia)

    # Definir a relação água/cimento
    relacao_ac = 1.8

    # Calcular o consumo de cimento
    consumo_cimento = calcular_consumo_cimento(traco, massas_especificas, relacao_ac)

    # Exibir apresentação
    print("\n============ Cálculo de cimento em kg ============")
    # Exibir o resultado
    print(f"Consumo de cimento por m³ de argamassa: {consumo_cimento:.2f} kg")

if __name__ == "__main__":
    main()
