import networkx as nx
import matplotlib.pyplot as plt

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read().strip().split('\n\n')
    listas_adjacencia = []
    for grafo in conteudo:
        linhas = grafo.strip().split('\n')
        lista = {}
        for linha in linhas:
            vertice, vizinhos = linha.split('=')
            vertice = vertice.strip()
            if vizinhos != '<>':
                vizinhos = vizinhos.strip('<>').split(', ') 
            else:
                vizinhos = []
            lista[vertice] = vizinhos
        listas_adjacencia.append(lista)
    return listas_adjacencia

def plotar_grafo(grafo, grafo_numero):
    nome_arquivo= f"digrafo_{grafo_numero}"
    G = nx.DiGraph()
        
    for vertice, vizinhos in grafo.items():
        G.add_node(vertice)  
        for vizinho in vizinhos:
            G.add_edge(vertice, vizinho)

    pos = nx.spring_layout(G)
        
    plt.figure(figsize=(7, 7))

    nx.draw(
        G, pos, with_labels=True, node_size=1000, node_color='lightblue',
        font_size=12, font_weight='bold', edge_color='gray', arrowsize=20
    )

    plt.title("Dígrafo {numero}")

    plt.savefig(f"{nome_arquivo}.png", format="PNG")

    plt.show()

def plotar_arvore_busca(arvore_busca, vertice_raiz):
    G = nx.DiGraph()  

    
    G.add_edges_from(arvore_busca)

    
    pos = gerar_posicao_hierarquica(G, vertice_raiz)


    plt.figure(figsize=(12, 8))
    nx.draw(
        G, pos, with_labels=True, node_size=2000, node_color='lightgreen',
        font_size=12, font_weight='bold', edge_color='gray', arrowsize=20
    )

    plt.title("Árvore de Busca em Profundidade (DFS) em Forma de Árvore")
    plt.show()

def gerar_posicao_hierarquica(G, vertice_raiz, largura_nivel=1.0):
    """
    Gera uma posição hierárquica dos nós para plotar em forma de árvore,
    garantindo que todos os nós tenham posições.
    """

    def posicionar(v, nivel=0, pos=None, largura=1, visitados=None):
        if pos is None:
            pos = {}  # Inicializa o dicionário de posições
        if visitados is None:
            visitados = set()  # Inicializa o conjunto de visitados

        # Adiciona o vértice atual à lista de visitados
        visitados.add(v)

        # Define a posição do vértice no layout hierárquico
        pos[v] = (nivel, -largura)

        # Obtém os filhos do vértice v (sucessores no grafo)
        filhos = list(G.successors(v))

        if filhos:
            # Define a largura para distribuir os filhos uniformemente
            largura_por_filho = largura_nivel / len(filhos)
            for i, filho in enumerate(filhos):
                if filho not in visitados:  # Evita ciclos
                    posicionar(filho, nivel + 1, pos, largura_por_filho * (i + 1), visitados)

        return pos

    pos = posicionar(vertice_raiz)

    # Verifica se todos os nós têm posição. Se não, adiciona nós isolados.
    for vertice in G.nodes():
        if vertice not in pos:
            pos[vertice] = (0, 0)  # Atribui posição padrão para nós desconectados

    return pos

def dfs(grafo, vertice_raiz):
    arvore_busca = []  
    vertices_visitados = set()
    arestas_visitadas = set()  
    pilha = []

    def explorar(vertice):
        vertices_visitados.add(vertice)
        pilha.append(vertice)

        for vizinho in grafo[vertice]:
            if (vertice, vizinho) not in arestas_visitadas:
                arestas_visitadas.add((vertice, vizinho))
                arvore_busca.append((vertice, vizinho))
            if vizinho not in vertices_visitados:
                explorar(vizinho)

        pilha.pop() 

    explorar(vertice_raiz)

    for vertice in grafo:
        if vertice not in vertices_visitados:
            explorar(vertice) 
            
    print("\nÁrvore de Busca em Profundidade:")
    for aresta in arvore_busca:
        print(f"{aresta[0]} -> {aresta[1]}")
        
    return arvore_busca, vertices_visitados
        
def main():
    listas = ler_arquivo("digrafos.txt")
    n = len(listas)
    if n == 0:
        print("Nenhum dígrafo encontrado no arquivo.")
        return
    while True:
        print(f"\nExistem {n} lista(s) de adjacência.")
        print("\nDigite a Opção Desejada:")
        print("1 - Selecionar qual digrafo deseja manipular")
        print("2 - Mostrar Digrafo")
        print("3 - Aplicar Busca em Profundidade")
        print("0 - Sair")
        opcao = input()
        
        if opcao == '0':
            break
        elif opcao == '1':
            print(f"Selecione um entre 1 e {n}:")
            numero = int(input())
            if 1 <= numero <= n:
                grafo_selecionado = listas[numero - 1]
                print(f"Dígrafo {numero} selecionado!")
            else:
                print("Opção inválida.")
        elif opcao == '2':
            if grafo_selecionado is not None:
                plotar_grafo(grafo_selecionado, numero)
            else:
                print("Nenhum dígrafo selecionado.")
        elif opcao == '3':
            if grafo_selecionado is not None:
                raiz = input(f"Escolha o vértice raiz da busca (opções: {', '.join(grafo_selecionado.keys())}): ")
                if raiz in grafo_selecionado:
                    plotar_arvore_busca(dfs(grafo_selecionado, raiz)[0], raiz)
                else:
                    print("Vértice inválido.")
            else:
                print("Nenhum dígrafo selecionado.")
        else:
            print("Opção inválida. Tente novamente.")
            
main()
