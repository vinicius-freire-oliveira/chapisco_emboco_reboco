def calcular_insumos_chapisco(area, rendimento_cimento, rendimento_areia, rendimento_area, capacidade_lata=18):
    fator_rendimento = area / rendimento_area
    quantidade_cimento = rendimento_cimento * fator_rendimento
    quantidade_areia = rendimento_areia * fator_rendimento
    latas_cimento = quantidade_cimento / capacidade_lata
    latas_areia = quantidade_areia / capacidade_lata

    return {
        "latas_cimento": latas_cimento,
        "latas_areia": latas_areia,
    }

def calcular_insumos_emboço(area, rendimento_cimento, rendimento_cal, rendimento_areia, rendimento_area, capacidade_lata=18):
    fator_rendimento = area / rendimento_area
    quantidade_cimento = rendimento_cimento * fator_rendimento
    quantidade_cal = rendimento_cal * fator_rendimento
    quantidade_areia = rendimento_areia * fator_rendimento
    latas_cimento = quantidade_cimento / capacidade_lata
    latas_cal = quantidade_cal / capacidade_lata
    latas_areia = quantidade_areia / capacidade_lata

    return {
        "latas_cimento": latas_cimento,
        "latas_cal": latas_cal,
        "latas_areia": latas_areia
    }

def calcular_insumos_reboco(area, rendimento_cal, rendimento_areia, rendimento_area, capacidade_lata=18):
    fator_rendimento = area / rendimento_area
    quantidade_cal = rendimento_cal * fator_rendimento
    quantidade_areia = rendimento_areia * fator_rendimento
    latas_cal = quantidade_cal / capacidade_lata
    latas_areia = quantidade_areia / capacidade_lata

    return {
        "latas_cal": latas_cal,
        "latas_areia": latas_areia
    }

def main():
    print("\n===== Cálculo de Insumos para Chapisco, Emboço e Reboco =====")

    # Definir os parâmetros de rendimento para chapisco
    rendimento_cimento_chapisco = 1 * 18  # 1 lata de 18 litros de cimento
    rendimento_areia_chapisco = 3 * 18  # 3 latas de 18 litros de areia grossa
    rendimento_area_chapisco = 30  # Rendimento para 30 m²

    # Definir os parâmetros de rendimento para emboço
    rendimento_cimento_emboço = 1 * 18  # 1 lata de 18 litros de cimento
    rendimento_cal_emboço = 2 * 18  # 2 latas de 18 litros de cal hidratada
    rendimento_areia_emboço = 9 * 18  # 9 latas de 18 litros de areia
    rendimento_area_emboço = 17  # Rendimento para 17 m²

    # Definir os parâmetros de rendimento para reboco
    rendimento_cal_reboco = 1 * 18  # 1 lata de 18 litros de cal hidratada
    rendimento_areia_reboco = 2 * 18  # 2 latas de 18 litros de areia
    rendimento_area_reboco = 35  # Rendimento para 35 m²

    # Definir a área total a ser revestida
    area_total = 80  # m²

    # Calcular os insumos necessários para chapisco
    insumos_chapisco = calcular_insumos_chapisco(area_total, rendimento_cimento_chapisco, rendimento_areia_chapisco, rendimento_area_chapisco)

    # Calcular os insumos necessários para emboço
    insumos_emboço = calcular_insumos_emboço(area_total, rendimento_cimento_emboço, rendimento_cal_emboço, rendimento_areia_emboço, rendimento_area_emboço)

    # Calcular os insumos necessários para reboco
    insumos_reboco = calcular_insumos_reboco(area_total, rendimento_cal_reboco, rendimento_areia_reboco, rendimento_area_reboco)

    # Imprimir os resultados para chapisco
    print(f"\nPara chapiscar {area_total} m² de parede:")
    print(f" - Latas de cimento: {insumos_chapisco['latas_cimento']:.2f} latas de 18 litros")
    print(f" - Latas de areia grossa: {insumos_chapisco['latas_areia']:.2f} latas de 18 litros")

    # Imprimir os resultados para emboço
    print(f"\nPara emboçar {area_total} m² de parede:")
    print(f" - Latas de cimento: {insumos_emboço['latas_cimento']:.2f} latas de 18 litros")
    print(f" - Latas de cal hidratada: {insumos_emboço['latas_cal']:.2f} latas de 18 litros")
    print(f" - Latas de areia: {insumos_emboço['latas_areia']:.2f} latas de 18 litros")

    # Imprimir os resultados para reboco
    print(f"\nPara rebocar {area_total} m² de parede:")
    print(f" - Latas de cal hidratada: {insumos_reboco['latas_cal']:.2f} latas de 18 litros")
    print(f" - Latas de areia: {insumos_reboco['latas_areia']:.2f} latas de 18 litros")

if __name__ == "__main__":
    main()
