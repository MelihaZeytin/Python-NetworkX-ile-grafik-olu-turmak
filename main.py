# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import networkx as nx
import matplotlib.pyplot as plt
# Press the green button in the gutter to run the script.
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import networkx as nx
import matplotlib.pyplot as plt
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    G = nx.DiGraph()  # graph

    # nodelar grapha eklenir
    G.add_node(1)
    G.add_node(0)
    G.add_node(4)
    G.add_node(3)
    G.add_node(2)

    # köşeler grapha eklenir
    G.add_edge(0, 1, weight=5)
    G.add_edge(0, 2, weight=3)
    G.add_edge(0, 4, weight=2)
    G.add_edge(1, 2, weight=2)
    G.add_edge(1, 3, weight=6)
    G.add_edge(2, 1, weight=1)
    G.add_edge(2, 3, weight=2)
    G.add_edge(4, 1, weight=6)
    G.add_edge(4, 2, weight=10)
    G.add_edge(4, 3, weight=4)

    pos = nx.circular_layout(G) # Düğümler bir daire üzerinde konumlandırılır

    nx.draw(G, pos, with_labels=True, font_weight='bold', connectionstyle="arc3,rad=0.01")
    edge_weight = nx.get_edge_attributes(G, 'weight')  # dictionary
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight, label_pos=0.3)

    plt.show()

    for node in sorted(G.nodes):  # 4 düğümünün tüm nodelar auzaklığını bulmak için tüm nodelarda dönülür
        toplamYol = 0
        digerNode = node
        try:
            liste = nx.dijkstra_path(G, 4, digerNode, "weight")  # shortest path
            print("4 numaralı düğümün " + str(digerNode) + " düğümüne olan en kısa yol uzunluğu: ")
            for i in range(len(liste) - 1):
                for key, value in edge_weight.items(): # dict
                    if key[0] == liste[i] and key[1] == liste[i+1]:
                        toplamYol += value
            print(toplamYol) # toplam yol yazdırılır
        except: # eğer yol yoksa except bloğuna girilir
            print("4 numaralı düğümden " + str(digerNode) + " düğümüne yol yoktur ")
        print()


    G.remove_node(1) # node 1 graphdan çıkarılır

    nx.draw(G, pos, with_labels=True, font_weight='bold' ,connectionstyle='arc3, rad = 0.01')
    edge_weight = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight)
    plt.show() # çıkarılmış hali yazdırılır