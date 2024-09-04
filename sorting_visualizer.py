import matplotlib.pyplot as plt
import random
import time

# Função para desenhar o gráfico
def draw_data(data, color_array):
    plt.bar(range(len(data)), data, color=color_array)
    plt.pause(0.05)
    plt.clf()

# Implementação do Bubble Sort
def bubble_sort(data, draw_data):
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(data, ['green' if x == j or x == j + 1 else 'blue' for x in range(len(data))])
    draw_data(data, ['green' for _ in range(len(data))])

# Função principal
if __name__ == "__main__":
    data = [random.randint(1, 100) for _ in range(20)]
    draw_data(data, ['blue' for _ in range(len(data))])
    time.sleep(1)
    bubble_sort(data, draw_data)
    plt.show()
