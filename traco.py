def calcular_insumos_chapisco(area, espessura, proporcao_cimento, proporcao_areia, capacidade_lata, peso_saco_cimento=50):
    volume_total = area * espessura
    volume_cimento_m3 = volume_total * (proporcao_cimento / (proporcao_cimento + proporcao_areia))
    volume_areia_m3 = volume_total * (proporcao_areia / (proporcao_cimento + proporcao_areia))
    volume_cimento_litros = volume_cimento_m3 * 1000
    volume_areia_litros = volume_areia_m3 * 1000
    latas_cimento = volume_cimento_litros / capacidade_lata
    latas_areia = volume_areia_litros / capacidade_lata
    sacos_cimento = latas_cimento
    return {
        "sacos_cimento": sacos_cimento,
        "latas_cimento": latas_cimento,
        "latas_areia": latas_areia
    }

def calcular_insumos_emboço(area, espessura, proporcao_cimento, proporcao_cal, proporcao_areia, capacidade_lata, peso_saco_cimento=50, peso_saco_cal=20):
    volume_total = area * espessura
    volume_cimento_m3 = volume_total * (proporcao_cimento / (proporcao_cimento + proporcao_cal + proporcao_areia))
    volume_cal_m3 = volume_total * (proporcao_cal / (proporcao_cimento + proporcao_cal + proporcao_areia))
    volume_areia_m3 = volume_total * (proporcao_areia / (proporcao_cimento + proporcao_cal + proporcao_areia))
    volume_cimento_litros = volume_cimento_m3 * 1000
    volume_cal_litros = volume_cal_m3 * 1000
    volume_areia_litros = volume_areia_m3 * 1000
    latas_cimento = volume_cimento_litros / capacidade_lata
    latas_cal = volume_cal_litros / capacidade_lata
    latas_areia = volume_areia_litros / capacidade_lata
    sacos_cimento = latas_cimento
    sacos_cal = latas_cal * (capacidade_lata / peso_saco_cal)
    return {
        "sacos_cimento": sacos_cimento,
        "sacos_cal": sacos_cal,
        "latas_cimento": latas_cimento,
        "latas_cal": latas_cal,
        "latas_areia": latas_areia
    }

def calcular_insumos_reboco(area, espessura, proporcao_cal, proporcao_areia, capacidade_lata, peso_saco_cal=20):
    volume_total = area * espessura
    volume_cal_m3 = volume_total * (proporcao_cal / (proporcao_cal + proporcao_areia))
    volume_areia_m3 = volume_total * (proporcao_areia / (proporcao_cal + proporcao_areia))
    volume_cal_litros = volume_cal_m3 * 1000
    volume_areia_litros = volume_areia_m3 * 1000
    latas_cal = volume_cal_litros / capacidade_lata
    latas_areia = volume_areia_litros / capacidade_lata
    sacos_cal = latas_cal * (capacidade_lata / peso_saco_cal)
    return {
        "sacos_cal": sacos_cal,
        "latas_cal": latas_cal,
        "latas_areia": latas_areia
    }

def main():
    print("\n ============ Argamassas para revestimento ============")

    # Solicitar o número de metros quadrados para revestimento
    area_total = float(input("Digite a área em metros quadrados para revestimento: "))

    # Solicitar a espessura do chapisco
    espessura_chapisco = float(input("Digite a espessura do chapisco em metros: "))

    # Solicitar a espessura do emboço
    espessura_emboço = float(input("Digite a espessura do emboço em metros: "))

    # Solicitar a espessura do reboco
    espessura_reboco = float(input("Digite a espessura do reboco em metros: "))

    # Definir os traços para cada tipo de argamassa
    chapisco_traco = (1, 0, 3)  # Cimento:Cal:Areia
    emboço_traco = (1, 2, 9)  # Cimento:Cal:Areia
    reboco_traco = (1, 2)  # Cal:Areia

    capacidade_lata = 36  # litros por lata

    # Calcular os materiais para chapisco
    chapisco_materiais = calcular_insumos_chapisco(area_total, espessura_chapisco, chapisco_traco[0], chapisco_traco[2], capacidade_lata)
    print("\nChapisco:")
    print(f" - Cimento: {chapisco_materiais['sacos_cimento']:.2f} sacos de 50kg")
    print(f" - Latas de cimento: {chapisco_materiais['latas_cimento']:.2f} latas de 36 litros")
    print(f" - Latas de areia: {chapisco_materiais['latas_areia']:.2f} latas de 36 litros")

    # Calcular os materiais para emboço
    emboço_materiais = calcular_insumos_emboço(area_total, espessura_emboço, emboço_traco[0], emboço_traco[1], emboço_traco[2], capacidade_lata)
    print("\nEmboço:")
    print(f" - Cimento: {emboço_materiais['sacos_cimento']:.2f} sacos de 50kg")
    print(f" - Cal: {emboço_materiais['sacos_cal']:.2f} sacos de 20kg")
    print(f" - Latas de cimento: {emboço_materiais['latas_cimento']:.2f} latas de 36 litros")
    print(f" - Latas de cal: {emboço_materiais['latas_cal']:.2f} latas de 36 litros")
    print(f" - Latas de areia: {emboço_materiais['latas_areia']:.2f} latas de 36 litros")

    # Calcular os materiais para reboco
    reboco_materiais = calcular_insumos_reboco(area_total, espessura_reboco, reboco_traco[0], reboco_traco[1], capacidade_lata)
    print("\nReboco:")
    print(f" - Cal: {reboco_materiais['sacos_cal']:.2f} sacos de 20kg")
    print(f" - Latas de cal: {reboco_materiais['latas_cal']:.2f} latas de 36 litros")
    print(f" - Latas de areia: {reboco_materiais['latas_areia']:.2f} latas de 36 litros")

if __name__ == "__main__":
    main()
