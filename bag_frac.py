def ordena(pv):

    pvd = []

    for i in pv:
        p, v = i
        pvd.append((p, v, v/p))

    pvd.sort(key=lambda tup: tup[2], reverse=1)

    return pvd


def make_bag_frag(pv, w):
    # -----------------------------------Definir atributo dos itens-----------------------------------------------------
    # Peso
    pvd = ordena(pv)
    # valor

    # densidade
    # aqui o programa define mais na frente (não mexer)
    # ------------------------------------------------------------------------------------------------------------------

    # ---------------------------------Definir os atributos da mochila--------------------------------------------------
    # Peso máximo
    p_maximo = w  # Definir aqui o peso da mochila
    # peso ocupado
    p_ocupado = 0
    # valor guardado
    v_ocupado = 0
    # peso do item guardado
    inside_peso = []
    # valor do item guardado
    inside_valor = []
    # peso necessário para atingir o peso máximo da mochila
    p_frac = 0
    # valor de item fracionado
    v_frac = 0
    # variavel de checagem
    check = 0
    # -------------------------------------------organiza a mochila-----------------------------------------------------
    for item in pvd:
        peso, valor, densidade = item
        check += peso
        if check <= p_maximo:  # checa se o item + o atual da mochila não extrapolam o limite
            inside_peso.append(peso)
            inside_valor.append(valor)
            p_ocupado += peso
            v_ocupado += valor
            check = p_ocupado
        elif p_ocupado == p_maximo:  # checa se a mochila ja está cheia
            break
        else:  # vai vir pra cá quando o elemento inteiro extrapola o limite da mochila
              # e esta ainda contém espaço, nesse caso fracionar
            p_frac = p_maximo - p_ocupado
            v_frac = p_frac * densidade
            inside_peso.append(p_frac)
            inside_valor.append(v_frac)
            p_ocupado += p_frac
            v_ocupado += v_frac
            break
    # ------------------------------------------------------------------------------------------------------------------

    print('peso dos itens', inside_peso)
    print('valor dos itens', inside_valor)
    print('peso total dentro da mochila', p_ocupado)
    print('valor total dentros da mochila', v_ocupado)
    return 0
