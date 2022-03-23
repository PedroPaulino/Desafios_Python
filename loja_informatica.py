def create_report():
    componentes_verificados = set(['Caixas de som','cooler','dissipador de calor','cpu','hd','estabilizador','gabinete','hub','impressora','joystick','memoria ram','microfone','modem','monitor','mouse','noBreak','placa de video','placa de captura','placa de som','placa mãe','scanner','teclado','webcam'])

    componentes_com_defeito = set(['hd','monitor','placa de som','scanner'])

    qtde_componentes_verificados = len(componentes_verificados)
    qtde_componentes_com_defeito = len(componentes_com_defeito)

    componentes_ok = componentes_verificados.difference(componentes_com_defeito) # -

    print(f"Foram verificados {qtde_componentes_verificados} componentes. \n")
    print(f"{qtde_componentes_com_defeito} componentes que apresentaram defeito. \n")

    print(f"Os componentes que podem ser vendidos são:")

    for item in componentes_ok:
        print(item)
        
    print(f"Quantidade de componentes ok: {len(componentes_ok)}")

create_report()