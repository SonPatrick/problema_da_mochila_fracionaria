def make_bag_frag(p, v, w):
    #Definir atributo dos itens
    #Peso
    p = p
    #valor
    v = v
    #densidade
    d = [] #aqui o programa define mais na frente (não mexer)
    #-------------------------

    #Definir os atributos da mochila
    #Peso máximo
    p_maximo = w #Definir aqui o peso da mochila
    #peso ocupado
    p_ocupado = 0
    #valor guardado
    v_ocupado = 0
    #peso do item guardado
    inside_peso = []
    #valor do item guardado
    inside_valor = []
    #peso necessário para atingir o peso máximo da mochila
    p_frac = 0
    #valor de item fracionado
    v_frac = 0
    #variavel de checagem
    check = 0
    #-------------------------------

    #calcular a densidade dos itens
    n = len(p)
    for i in range(0, n, 1):
        d.append(v[i]/p[i])
    d.sort(reverse = 1)
    #------------------------------
    #organiza os itens com suas respectivas densidades em ordem decrescente
    for i in range(0, n, 1):
        pivot = d[i]
        for j in range(0, n, 1):
            if pivot == v[j]/p[j]:
                pivot_v = v[i]
                pivot_p = p[i]
                v[i] = v[j]
                p[i] = p[j]
                v[j] = pivot_v
                p[j] = pivot_p
                break
    #---------------------------------------------------------------------

    #organiza a mochila
    for i in range(0, n, 1):
        check += p[i]
        if check <= p_maximo:
            inside_peso.append(p[i])
            inside_valor.append(v[i])
            p_ocupado += p[i]
            v_ocupado += v[i]
            check = p_ocupado
        else:
            p_frac = p_maximo - p_ocupado
            v_frac = p_frac * d[i]
            inside_peso.append(p_frac)
            inside_valor.append(v_frac)
            p_ocupado += p_frac
            v_ocupado += v_frac

    print('peso dos itens', inside_peso)
    print('valor dos itens', inside_valor)
    print('peso total dentro da mochila', p_ocupado)
    print('valor total dentros da mochila', v_ocupado)
    return 0