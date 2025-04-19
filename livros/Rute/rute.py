from fpdf import FPDF

# Função para adicionar os capítulos do Livro de Rute
def adicionar_capitulo(pdf, numero_capitulo, texto_capitulo, titulo_capitulo):
    pdf.add_page()
    pdf.set_font("Arial", 'B', 26)
    pdf.cell(180, 10, f'Capítulo {numero_capitulo} - {titulo_capitulo}', ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=19)
    pdf.multi_cell(0, 10, texto_capitulo)

# Criando o título de cada capítulo
titulos_capitulos = {
    1: "O Começo da Jornada",
    2: "O Campo da Providência",
    3: "À Meia-noite na Eira",
    4: "Redenção em Belém"
}

# Criando o conteúdo com base na tradução da Bíblia (em domínio público) TB (Tradução Brasileira)
capitulos = {
    1: """
Naqueles dias, quando os juízes governavam, houve uma fome na terra, e um homem de Belém de Judá foi com sua mulher e seus dois filhos para os campos de Moabe, a fim de morar ali.
    O homem se chamava Elimeleque, e a mulher, Noemi; os seus filhos se chamavam Malom e Quiliom, e eram efrateus de Belém de Judá. Quando chegaram a Moabe, ficaram ali.
    Elimeleque, marido de Noemi, morreu, e ela ficou com seus dois filhos, os quais se casaram com mulheres moabitas; o nome de uma era Orfa, e o da outra, Rute. Depois de terem vivido ali cerca de dez anos, Malom e Quiliom também morreram, e Noemi ficou sozinha, sem os seus dois filhos e sem o marido.
    Então, Noemi resolveu voltar de Moabe, porque soubera que o Senhor tinha visitado o seu povo, dando-lhe alimento. Com as suas noras, partiu do lugar onde estivera morando e começou a seguir o caminho de volta para a terra de Judá.
    Noemi disse às suas duas noras: "Vão, voltem cada uma para a casa de sua mãe. O Senhor seja bondoso com vocês, assim como vocês foram bondosas com os que morreram e comigo.
    Que o Senhor conceda a cada uma de vocês que encontre descanso na casa de outro marido." E beijou-as. Elas, porém, levantaram a voz e choraram.
    E disseram-lhe: "De maneira nenhuma, voltaremos contigo para o teu povo."
    Mas Noemi insistiu: "Voltem, minhas filhas! Por que iriam comigo? Tenho ainda filhos no meu ventre que possam ser seus maridos?
    Voltem, minhas filhas! Pois já estou muito velha para ter outro marido. E mesmo que dissesse: 'Tenho ainda esperança', e que esta noite me casasse com um homem, e ainda tivesse filhos, esperariam vocês até que crescessem? Ficariam sem se casar por causa disso? Não, filhas minhas, porque o que mais me aflige a mim é que a mão do Senhor se levantou contra mim."
    Elas, porém, levantaram a voz e choraram novamente. Então Orfa beijou sua sogra, mas Rute ficou com ela.
    Noemi disse: "Vê, tua cunhada voltou para o seu povo e para os seus deuses; volta com ela."
    Mas Rute respondeu: "Não insistas comigo que te deixe e que não te siga, porque aonde quer que tu fores, irei; onde quer que pousares, pousarei. O teu povo será o meu povo, e o teu Deus será o meu Deus.
    Onde tu morreres, morrerei, e ali serei sepultada. Que o Senhor me faça isso e me acrescente ainda mais, se outra coisa que não seja a morte me separar de ti."
    Quando Noemi viu que Rute estava resolvida a acompanhá-la, deixou de insistir.
    Ambas seguiram, até que chegaram a Belém. Quando chegaram a Belém, toda a cidade se agitou por causa delas, e as mulheres exclamaram: "É esta Noemi?"
    Ela respondeu: "Não me chamem Noemi; chamem-me Mara, porque o Todo-Poderoso me fez muito amarga.
    Fui cheia quando saí, mas o Senhor me fez voltar vazia. Por que me chamareis Noemi, se o Senhor testificou contra mim e o Todo-Poderoso me afligiu?"
    Assim, Noemi voltou de Moabe, acompanhada de Rute, a moabita, sua nora. Chegaram a Belém no começo da colheita da cevada.
    """,
    2: """
Noemi tinha um parente por parte de seu marido, homem rico e influente da família de Elimeleque, cujo nome era Boaz.
    Rute, a moabita, disse a Noemi: "Deixe-me ir ao campo, apanhar espigas atrás daquele que me permitir." Noemi respondeu: "Vá, minha filha."
    Rute foi, entrou num campo para apanhar espigas e, por acaso, aquele campo pertencia a Boaz, que era da família de Elimeleque.
    Boaz chegou de Belém e disse aos ceifeiros: "O Senhor esteja com vocês!" Eles responderam: "O Senhor te abençoe!"
    Então Boaz perguntou ao servo encarregado dos ceifeiros: "De quem é esta moça?" O servo respondeu: "É a moça moabita que voltou com Noemi da terra de Moabe. Ela me pediu: 'Deixe-me respigar e ajuntar entre os feixes, após os ceifeiros.' Ela veio e tem estado aqui desde cedo até agora; apenas descansou um pouco no abrigo."
    Então Boaz disse a Rute: "Ouça bem, minha filha: não vá respigar em outro campo, nem se afaste daqui. Fique com minhas servas. Observe onde os homens estão ceifando e vá atrás delas. Ordenei aos servos que não te toquem. Quando tiveres sede, vá até os vasos e beba da água que os servos tiraram."
    Rute se prostrou com o rosto em terra e disse: "Por que achei favor aos teus olhos, para que te interesses por mim, sendo eu estrangeira?"
    Boaz respondeu: "Foi-me contado, com detalhes, tudo quanto fizeste por tua sogra depois da morte de teu marido, e como deixaste teu pai, tua mãe e a terra onde nasceste para vires a um povo que não conhecias antes. O Senhor te recompense pelo que fizeste; e seja tua recompensa completa da parte do Senhor, Deus de Israel, sob cujas asas vieste buscar refúgio."
    Ela respondeu: "Ache eu favor diante dos teus olhos, meu senhor, pois me consolaste e falaste ao coração de tua serva, ainda que eu não seja como uma de tuas servas."
    Na hora da refeição, Boaz lhe disse: "Aproxima-te, come do pão e molha teu bocado no vinagre." Ela se sentou junto aos ceifeiros, ele lhe deu grãos tostados, e ela comeu, ficou satisfeita e ainda sobrou.
    Ao se levantar para respigar, Boaz deu ordens a seus servos: "Deixem-na respigar também entre os feixes, sem a repreender. Tirem também algumas espigas dos feixes e deixem-nas cair para que ela apanhe, e não a censurem."
    Rute respigou no campo até à tarde. Depois debulhou o que havia colhido, e foi quase um efa de cevada.
    Ela tomou o que havia colhido, levou à cidade e mostrou a sua sogra. Também lhe deu o que sobrou depois de estar satisfeita.
    A sogra lhe perguntou: "Onde respigaste hoje? Onde trabalhaste? Bendito seja aquele que se interessou por ti!" Então Rute contou à sogra com quem tinha trabalhado e disse: "O nome do homem com quem hoje trabalhei é Boaz."
    Noemi disse à sua nora: "Bendito seja ele do Senhor, que não tem deixado de usar de bondade nem para com os vivos nem para com os mortos." E acrescentou: "Esse homem é nosso parente chegado, um dos nossos resgatadores."
    Rute, a moabita, disse: "Ele também me disse: 'Fica com os meus servos até que terminem toda a colheita.'"
    Noemi respondeu a Rute, sua nora: "É bom, minha filha, que saias com as servas dele, para que não te encontrem noutro campo."
    Assim, Rute ficou com as servas de Boaz para respigar até ao fim da colheita da cevada e do trigo. E morava com sua sogra.
    """,
    3: """
Depois disso, Noemi, sua sogra, lhe disse: "Minha filha, não hei de buscar-te um lar, para que sejas feliz?
    Ora, Boaz, com cujas servas estiveste, é nosso parente. Esta noite ele estará limpando cevada na eira.
    Lava-te, perfuma-te, põe tua melhor roupa e desce à eira. Mas não te dês a conhecer ao homem até que ele tenha acabado de comer e beber.
    Quando ele se deitar, observa o lugar onde se deita. Então vai, descobre os pés dele e deita-te ali. Ele te dirá o que deves fazer."
    Rute respondeu: "Farei tudo o que me disseres."
    Ela desceu à eira e fez conforme tudo o que sua sogra lhe havia ordenado.
    Quando Boaz comeu, bebeu e alegrou-se o coração, foi deitar-se ao pé de um monte de cereais. Rute se aproximou silenciosamente, descobriu os pés dele e deitou-se.
    No meio da noite, Boaz acordou sobressaltado e viu uma mulher deitada aos seus pés. Ele perguntou: "Quem és tu?"
    Ela respondeu: "Sou Rute, tua serva. Estende teu manto sobre tua serva, pois és resgatador."
    Boaz disse: "Bendita sejas do Senhor, minha filha! Melhor fizeste a tua última benevolência do que a primeira, pois não foste atrás de moços, nem pobres nem ricos.
    Agora, minha filha, não temas. Farei por ti tudo quanto pedires, pois toda a cidade do meu povo sabe que és mulher virtuosa.
    É verdade que sou teu resgatador; mas há ainda outro parente mais próximo do que eu.
    Fica aqui esta noite, e pela manhã, se ele quiser cumprir o dever de resgatador, que o faça. Mas, se não quiser, juro pelo Senhor que eu o farei. Fica deitada até de manhã."
    Rute ficou deitada aos pés dele até o amanhecer, mas levantou-se antes que se pudesse reconhecer alguém, pois Boaz dissera: "Ninguém saiba que esta mulher veio à eira."
    Ele lhe disse: "Traga o manto que tens sobre ti e segura-o." Ela o segurou, e ele mediu seis medidas de cevada e as pôs sobre ela. Depois Rute voltou para a cidade.
    Quando chegou à casa de sua sogra, esta lhe perguntou: "Como foi, minha filha?" Rute contou-lhe tudo o que o homem lhe fizera.
    E disse ainda: "Estas seis medidas de cevada ele me deu, dizendo: 'Não voltes para tua sogra com as mãos vazias.'"
    Então Noemi disse: "Espera, minha filha, até saberes como se resolverá o caso. Porque aquele homem não descansará enquanto não o concluir hoje."
    """,
    4: """
Boaz subiu à porta da cidade e sentou-se ali. Eis que o resgatador de quem ele havia falado passou por ali. Então Boaz o chamou: "Ó fulano, chega-te e assenta-te aqui." Ele se aproximou e sentou-se.
    Boaz tomou dez homens dos anciãos da cidade e disse: "Assentai-vos aqui." E eles se sentaram.
    Então Boaz disse ao resgatador: "Noemi, que voltou dos campos de Moabe, está vendendo a parte das terras que pertencia a nosso irmão Elimeleque. Resolvi informar-te disso e dizer-te: 'Compra diante dos que estão aqui sentados e dos anciãos do meu povo.' Se queres resgatar, resgata; mas, se não queres, declara-mo, para que eu o saiba. Pois não há outro além de ti para resgatar, e eu sou o próximo depois de ti."
    Ele respondeu: "Eu a resgatarei."
    Boaz, porém, disse: "No dia em que comprares o campo da mão de Noemi, também deverás tomar Rute, a moabita, mulher do falecido, para restaurar o nome do morto sobre a sua herança."
    Então o resgatador respondeu: "Nesse caso, não poderei resgatar por mim, para não prejudicar a minha herança. Resgata tu o que me caberia, porque eu não posso fazê-lo."
    Ora, este era o costume antigo em Israel quanto à remissão e à troca de propriedades: para confirmar qualquer negócio, um homem tirava o seu calçado e o dava ao outro; isso servia de testemunho em Israel.
    Assim, o resgatador disse a Boaz: "Compra tu mesmo", e tirou o seu calçado.
    Então Boaz disse aos anciãos e a todo o povo: "Sois hoje testemunhas de que comprei de Noemi tudo o que pertencia a Elimeleque, a Quiliom e a Malom. E também tomo por mulher Rute, a moabita, mulher de Malom, para manter o nome do falecido sobre a sua herança, para que o nome dele não seja apagado dentre seus irmãos e da porta da sua cidade. Disto sois hoje testemunhas."
    Todo o povo que estava à porta, e os anciãos, disseram: "Somos testemunhas! O Senhor faça à mulher que entra em tua casa como fez a Raquel e a Leia, que edificaram a casa de Israel. E tu, sê poderoso em Efrata e faze-te nomeado em Belém. Seja a tua casa como a de Perez, que Tamar deu a Judá, pela descendência que o Senhor te der desta jovem."
    Assim, Boaz tomou Rute, e ela tornou-se sua mulher. Ele a possuiu, e o Senhor lhe concedeu conceber, e ela deu à luz um filho.
    Então as mulheres disseram a Noemi: "Bendito seja o Senhor, que não te deixou hoje sem resgatador! Que o seu nome seja celebrado em Israel! Ele será para ti restaurador da alma e sustentador da tua velhice, pois tua nora, que te ama, o deu à luz; ela que te é melhor do que sete filhos."
    Noemi tomou o menino, colocou-o no colo e passou a cuidar dele.
    As vizinhas lhe deram um nome, dizendo: "Nasceu um filho a Noemi!" E o chamaram Obede. Este é o pai de Jessé, pai de Davi.
    Estas são as gerações de Perez: Perez gerou Hezrom; Hezrom gerou Rão; Rão gerou Aminadabe; Aminadabe gerou Naassom; Naassom gerou Salmom; Salmom gerou Boaz; Boaz gerou Obede; Obede gerou Jessé; e Jessé gerou Davi.
    """
}

# Criando o PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_left_margin(15)
pdf.set_right_margin(15)

# Cria um página
pdf.add_page()

# Define a cor de fundo preta (preenche toda a página)
pdf.set_fill_color(0, 0, 0)  # RGB preto
pdf.rect(0, 0, 210, 297, 'F')  # Tamanho padrão A4 em mm

# Adiciona fonte Arial em branco
pdf.set_text_color(255, 255, 255)  # RGB branco
pdf.set_font('Arial', 'B', 30)

# Centraliza o texto na página
pdf.set_xy(0, 140)  # Aproximadamente meio da página
pdf.cell(210, 20, 'O livro de Rute', align='C')

# Restaura cores
pdf.set_text_color(0, 0, 0)

for capitulo, texto in capitulos.items():
    adicionar_capitulo(pdf, capitulo, texto, titulos_capitulos[capitulo])

pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.multi_cell(0, 10, """
    Com base na Tradução Brasileira da Bíblia (TB)
    Versão em domínio público
    Adaptação literária e composição por Paulo Sergio
    Este trabalho foi elaborado com o propósito de tornar a leitura do Livro de Rute mais acessível, envolvente e inspiradora, preservando a essência e a integridade do texto original.
    Fonte original: Tradução Brasileira da Bíblia, publicada em 1917, atualmente em domínio público.

             Licença: Domínio Público
    Você é livre para copiar, distribuir, adaptar e utilizar este conteúdo para qualquer fim, inclusive comercial, sem necessidade de permissão ou atribuição obrigatória.

    Versão literária criada em 2025
""")

pdf.add_page()
pdf.set_fill_color(0, 0, 0)  # RGB preto
pdf.rect(0, 0, 210, 297, 'F')  # Tamanho padrão A4 em mm

# Salvando o PDF
output_pdf_path = "./Rute.pdf"
pdf.output(output_pdf_path)
