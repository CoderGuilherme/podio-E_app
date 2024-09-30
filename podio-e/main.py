from flet import *
from custom_checkbox import CustomCheckBox

def main(page: Page):
    DT = "#F7EA3D"
    FG = "#212121"
    BG = "#111111"
    TX_COLOR = "WHITE"

    challenges = [
        {
            "categoria": "Sustainability",
            "cor": "#72A170",
            "desafio": "Redução de Resíduos Plásticos",
            "descricao": "Implementar práticas para reduzir o uso de plásticos descartáveis e promover a reciclagem."
        },
        {
            "categoria": "Sustainability",
            "cor": "#72A170",
            "desafio": "Transição para Energias Renováveis",
            "descricao": "Aumentar o uso de energias renováveis, como solar e eólica, reduzindo a dependência de combustíveis fósseis."
        },
        {
            "categoria": "Sustainability",
            "cor": "#72A170",
            "desafio": "Eficiência Energética",
            "descricao": "Melhorar a eficiência energética em edifícios e processos industriais para reduzir emissões de gases de efeito estufa."
        },
        {
            "categoria": "Sustainability",
            "cor": "#72A170",
            "desafio": "Conservação da Água",
            "descricao": "Implementar estratégias para economizar água e promover o uso sustentável dos recursos hídricos."
        },
        {
            "categoria": "Sustainability",
            "cor": "#72A170",
            "desafio": "Agricultura Sustentável",
            "descricao": "Promover práticas agrícolas que conservem o solo e reduzam o impacto ambiental da produção de alimentos."
        },
        {
            "categoria": "Physical Activity",
            "cor": "#C5A662",
            "desafio": "Aumento da Atividade Física Diária",
            "descricao": "Incentivar as pessoas a se moverem mais, promovendo caminhadas, corridas e atividades físicas regulares."
        },
        {
            "categoria": "Physical Activity",
            "cor": "#C5A662",
            "desafio": "Promoção de Ciclovias Urbanas",
            "descricao": "Desenvolver infraestruturas urbanas para ciclistas, promovendo o uso de bicicletas como transporte sustentável."
        },
        {
            "categoria": "Physical Activity",
            "cor": "#C5A662",
            "desafio": "Atividades Físicas para Crianças",
            "descricao": "Incentivar crianças a participarem de esportes e atividades físicas para melhorar a saúde e o bem-estar."
        },
        {
            "categoria": "Formula E",
            "cor": "#19376D",
            "desafio": "Desenvolvimento de Tecnologias de Veículos Elétricos",
            "descricao": "Avançar na pesquisa e desenvolvimento de carros elétricos para melhorar eficiência e reduzir emissões."
        },
        {
            "categoria": "Formula E",
            "cor": "#19376D",
            "desafio": "Promoção de Competições Ecológicas",
            "descricao": "Organizar corridas de carros elétricos que promovam sustentabilidade e conscientizem sobre energia limpa."
        },
    ]
    tasks = Column(
    height=300,
    scroll='auto',)

    for i,item in enumerate(challenges):
        tasks.controls.append(
        Container(
        height=120,
        expand= True,
        bgcolor=FG,
        border_radius=25,padding=padding.only(
            left=20,top=25,
        ),
        content= Column(
            controls=[
                CustomCheckBox(
                    color=item['cor'],
                    checked_color= item["cor"],
                    label=item['desafio']),
                Text(value = f"{item['descricao']}",color=TX_COLOR)]
        ))
      
      
    )  
    # Criação dos cards de categoria
    categories_card = Row(
        spacing=10,  # Espaçamento entre os cards
        alignment=MainAxisAlignment.START,  # Alinha os cards ao início da linha
    )
    
    categories = [
    {
        "nome": "Sustainability",
        "cor": "#72A170"  # Cor de fundo para Sustentabilidade
    },
    {
        "nome": "Physical Activity",
        "cor": "#C5A662"  # Cor de fundo para Atividade Física
    },
    {
        "nome": "Formula E",
        "cor": "#19376D"  # Cor de fundo para Formula E
    }
]


    for i, category in enumerate(categories):
        categories_card.controls.append(
        Container(
            bgcolor=category["cor"],
            expand= True,
            height=100,
            padding=15,
            border_radius=20,  # Adiciona bordas arredondadas
            margin=margin.all(15),# Adiciona uma margem para espaçamento
            content=Column(alignment=MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                Text('40 Challends',color= TX_COLOR,size=16),
                Text(category["nome"],color= TX_COLOR,size=20),
                Container(
                width=200,
                height=8,
                bgcolor='BLACK',
                border_radius=20,
                padding=padding.only(right=i*30),
                content=Container(
                bgcolor=DT,
                ),
                
                )
            ]

            )
        )
        )
    # Conteúdo da primeira página
    first_page_contents = Container(
        padding=padding.all(20),
        content=Column(
            controls=[
                Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        Container(content=Icon(icons.MENU)),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.WALLET)
                            ]
                        )
                    ]
                ),
                Container(height=20),
                Text(value="PODIO-E TASKS!", style=TextStyle(size=24, color=TX_COLOR)),
                Text(value="CATEGORIES", style=TextStyle(size=20, color=TX_COLOR)),
                Container(
                    padding=padding.only(top=10, bottom=20),
                    content=categories_card
                ),

                 Text("TODAY'S CHALLENDS"),
                 Stack(
                    controls=[tasks]
        )
            ],
        ),
    )

    # Container para a segunda página
    page_2 = Container(
        expand= True,  # Ajusta a largura para ser 80% da largura da tela
        height=page.height * 0.9,  # Ajusta a altura para ser 90% da altura da tela
        bgcolor=BG,
        padding=padding.only(top=30, left=20, right=20, bottom=5),
        content=first_page_contents
    )

    # Container principal
    container = Container(
        expand=True, 
        height=page.height * 0.9,  # Ajusta a altura para ser 90% da altura da tela
        bgcolor=BG,
        border_radius=30,
        content=Stack(
            controls=[
                page_2
            ]
        )
    )

    # Configura o alinhamento da página
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.padding = padding.all(20)  # Remove o padding da página
    page.margin = margin.all(0)    # Remove a margem da página (se disponível)
    page.add(container)
    page.update()

app(target=main)
