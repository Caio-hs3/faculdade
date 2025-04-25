# modulo para plotar gráficos
import matplotlib.pyplot as plt
# módulo para plotar polígonos
from matplotlib.patches import Polygon

def min_max(indice, originalpoints, transformedpoints):
    ''' retorna os valores mínimo e máximo dentre duas listas de pontos, usando as funções internas min e max.
    As listas devem estar no formato: [[x_0,y_0], [x_1, y_1], ..., [x_n, y_n]] ou [(x_0,y_0),(x_1, y_1),...,(x_n, y_n)]
    Entrada: int, list, list
    Saída: float, float '''

    # usando as funções internas min e max
    minimo = min(min(point[indice] for point in originalpoints), min(point[indice] for point in transformedpoints)) - 1
    maximo = max(max(point[indice] for point in originalpoints), max(point[indice] for point in transformedpoints)) + 1

    return minimo, maximo

def show_polygon(originalpoints, transformedpoints, title):
    '''
    Plota polígono original e o polígono transformado por uma transformação de rotação, translação ou cisalhamento no polígono original.
    Os vértices dos polígonos são dados por listas de pontos,
    as quais devem estar no formato: l = [[x_0,y_0], [x_1, y_1], ...]
    Entrada: list, list, string
    '''
    # configuração dos tamanhos das fontes da figura
    SIZE = 10
    # tamanho padrão da fonte para textos e números
    plt.rc('font', size=SIZE)
    # tamanho padrão da fonte para título dos eixos
    plt.rc('axes', titlesize=SIZE)
    # tamanho padrão da fonte para rótulos dos eixos x e y
    plt.rc('axes', labelsize=SIZE)
    # tamanho padrão da fonte da numeração do eixo x
    plt.rc('xtick', labelsize=0.75*SIZE)
    # tamanho padrão da fonte da numeração do eixo y
    plt.rc('ytick', labelsize=0.75*SIZE)
    # tamanho padrão da fonte da legenda
    plt.rc('legend', fontsize=SIZE )

    # Cria variáveis que vão definir os tamanhos máximos e mínimos da figura,
    # tanto no eixo x (indice = 0), quanto no eixo y (indice = 1),
    # usando a função min_max()
    minx, maxx = min_max(0, originalpoints, transformedpoints)
    miny, maxy = min_max(1, originalpoints, transformedpoints)

    fig, ax = plt.subplots( )
    # plot do polígono com os pontos originais
    ax.add_patch( Polygon(originalpoints, closed=True, fill=None, edgecolor='b', label = "Original", linewidth=2.0))
    # plot do polígono com os pontos transformados
    ax.add_patch( Polygon(transformedpoints, closed=True, fill=None, edgecolor='r', label = "Transformado", linewidth=2.0))

    # configurações do gráfico
    ax.set_title(title, fontsize=1.25*SIZE)
    ax.set_xlim([minx, maxx])
    ax.set_ylim([miny, maxy])
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.set_aspect('equal')
    ax.grid(True)
    ax.legend()

    # plotar o gráfico
    plt.show()