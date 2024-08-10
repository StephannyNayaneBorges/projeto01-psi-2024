from django.shortcuts import render

def index(request):
    return render(request, "index.html", "img/perfil.jpg", "img/fundador.jpg", "img/centro de partida.jpg")

def jogadores(request):
    jogadores = [{"nome":"Renan Bragança", "idade":"26","posicao": "Goleiro", "nascimento": "Porto Alegre (RS)", "foto": "renan.jpg"},
                 {"nome": "Guilherme Guedes", "idade":"24","posição": "Lateral", "nascimento": "Porto Alegre (RS)", "foto": "guilherme.jpg"},
                 {"nome": "Alan Ferreira", "idade":"23","posição": "Zagueiro", "nascimento": "Maceió (AL)", "foto": "alan.jpg"},
                 {"nome": "Souza", "idade":"35","posição": "Meio-Campista", "nascimento": "Posse (GO)", "foto": "souza.jpg"},
                 {"nome": "Antônio", "idade":"20","posição": "Meio-Campista", "nascimento": "Duque de Caxias (RJ)", "foto": "antonio.jpg"},
                 {"nome": "Rodriguinho", "idade":"29","posição": "Meio-Campista", "nascimento": "Goiânia (GO)", "foto": "rodriguinho.jpg"},
                 {"nome": "Vinicius Guedes", "idade":"24","posição": "Meio-Campista", "nascimento": "Tapera (RS)", "foto": "vinicius.jpg"},                   
                 {"nome": "Lucas Gabriel", "idade":"23","posição": "Meio-Campista", "nascimento": "Rio de Janeiro (RJ)", "foto": "lucas gabriel.jpg"},
                 {"nome": "Rafael Diniz", "idade":"31","posição": "Atacante", "nascimento": "Alumínio (SP)", "foto": "rafael.jpg"},
                 {"nome": "Gustavo Ramos", "idade":"27","posição": "Atacante", "nascimento": "Crixás (GO)", "foto": "gustavo.jpg"},
                 {"nome": "Mahteus Ferreira", "idade":"30","posição": "Meio-Campista", "nascimento": "Divinópolis (MG)", "foto": "mahteus.jpg"},                   
                 {"nome": "Henrique César", "idade":"18","posição": "Meio-Campista", "nascimento": "Natal (RN)", "foto": "henrique.jpg"},

    ]
    context = {
        "jogadores": jogadores,
    }
    return render(request, "jogadores.html", context)
def sobre(request):
    return render(request, "sobre.html")
