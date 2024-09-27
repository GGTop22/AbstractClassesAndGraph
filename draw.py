import random
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

from GraphCoordCalculator import RandomXYCalculator, SimpleXYCalculator, AutoScaleXYCalculator
from GraphWithCoordinatesLoader import GraphWithCoordinatesLoader
from Loader import GraphFileLoader
from PathFinder import Path_Finder
from DijkstraPathFinder import DijkstrapathFinder
from BFSPathFinder import BFSPathFinder
from AstarPathFinder import AstarPathFinder  # Импортируем новый класс A*
from node import Node
from nodeXY import NodeXY


class GraphDrawer:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=1200, height=800)
        self.canvas.pack()
        self.nodes = {}
        self.edges = []
        self.graph = None
        self.selected_nodes = []  # Список для хранения выбранных узлов

        # Интерфейс
        self.frame = tk.Frame(root)
        self.frame.pack()

        self.file_entry = tk.Entry(self.frame)
        self.file_entry.insert(0, "roads")
        self.file_entry.pack(side=tk.LEFT)

        # Добавляем выпадающий список для выбора загрузчика
        self.loader_var = tk.StringVar(self.frame)
        self.loader_var.set("Фаил с координатами")  # Значение по умолчанию

        self.loader_menu = tk.OptionMenu(self.frame, self.loader_var, "Обычный заргузчик", "Фаил с координатами",
                                         command=self.LoaderMenu_SelectionEvent)
        self.loader_menu.pack(side=tk.LEFT)

        self.load_button = tk.Button(self.frame, text="Загрузить граф", command=self.load_graph)
        self.load_button.pack(side=tk.LEFT)

        self.route_button = tk.Button(self.frame, text="Построить маршрут", command=self.build_route)
        self.route_button.pack(side=tk.LEFT)

        # Добавляем выпадающий список для выбора алгоритма
        self.algorithm_var = tk.StringVar(self.frame)
        self.algorithm_var.set("Dijkstra")  # Значение по умолчанию

        self.algorithm_menu = tk.OptionMenu(self.frame, self.algorithm_var, "Dijkstra", "BFS", "A*",
                                            command=self.OptionMenu_SelectionEvent)
        self.algorithm_menu.pack(side=tk.LEFT)

        # Изначально выбираем алгоритм Дейкстры
        self.pathfinder = DijkstrapathFinder()
        self.loader = GraphFileLoader("roads")

        self.current_path_items = []

    def run(self):
        self.root.mainloop()

    def OptionMenu_SelectionEvent(self, event):
        algorithm = self.algorithm_var.get()
        if algorithm == "Dijkstra":
            self.pathfinder = DijkstrapathFinder()
        elif algorithm == "BFS":
            self.pathfinder = BFSPathFinder()
        elif algorithm == "A*":
            self.pathfinder = AstarPathFinder()
        else:
            messagebox.showerror("Ошибка", "Неизвестный алгоритм")

    def LoaderMenu_SelectionEvent(self, event):
        s = self.loader_var.get()
        q = self.file_entry.get()
        if s == "Обычный заргузчик":
            self.loader = GraphFileLoader(q)
        elif s == "Фаил с координатами":
            self.loader = GraphWithCoordinatesLoader(q)
        else:
            messagebox.showerror("Ошибка", "Неизвестный загрузчик")

    def left_click(self, event, name: str):
        print("Нажат узел", name)
        if len(self.selected_nodes) == 0:
            x, y = self.nodes[name]
            self.current_path_items.append(
                self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="orange", width=2)
            )
        elif len(self.selected_nodes) == 1:
            self.clear_previous_route()

        if len(self.selected_nodes) < 2:
            self.selected_nodes.append(name)
            if len(self.selected_nodes) == 2:
                self.build_route_with_selected_nodes()

    def clear_previous_route(self):
        for item in self.current_path_items:
            self.canvas.delete(item)
        self.current_path_items.clear()

    def build_route_with_selected_nodes(self):
        self.start_node_name = self.selected_nodes[0]
        self.end_node_name = self.selected_nodes[1]
        self.build_route()

    def load_graph(self):
        self.clear_canvas()
        s = self.file_entry.get()

        # Выбираем загрузчик на основе выбранного переключателя
        if self.loader_var.get() == "Обычный заргузчик":
            loader = GraphFileLoader(s)
        elif self.loader_var.get() == "Фаил с координатами":
            loader = GraphWithCoordinatesLoader(s)

        self.graph = loader.getGraph()

        # Выбираем способ получения координат
        #if self.loader_type_var.get() == "Standard":
            #coordinates = self.random_calculator.calculate_coordinates(self.graph)
        #else:
           # coordinates = self.auto_scaling_calculator.calculate_coordinates(self.graph)
        #xyCalculator=RandomXYCalculator(self.canvas.winfo_width(),self.canvas.winfo_height())
        xyCalculator=AutoScaleXYCalculator(self.canvas.winfo_width(),self.canvas.winfo_height(),self.graph)
        # Добавляем узлы и ребра на холст
        for node in self.graph.get_all_nodes():
            x,y=xyCalculator.calculate_xy(node)
            self.add_node(node.name, x, y)

        for from_node in self.graph.get_all_nodes():
            for to_node in self.graph.get_reachable_nodes(z=from_node):
                self.add_edge(from_node.name, to_node.name)



    def clear_canvas(self):
        self.canvas.delete("all")
        self.nodes.clear()
        self.edges.clear()
        self.selected_nodes.clear()  # Очищаем выбранные узлы при перезагрузке графа

    def add_node(self, name: str, x: int, y: int):
        self.nodes[name] = (x, y)
        self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="blue", tags="blue_node" + name)
        self.canvas.create_text(x, y, text=name, fill="red", tags="blue_node" + name)
        self.canvas.tag_bind("blue_node" + name, '<Button-1>', lambda event: self.left_click(event, name=name))

    def build_route_with_selected_nodes(self):
        # Очищаем предыдущий маршрут перед построением нового
        self.clear_previous_route()
        self.start_node_name = self.selected_nodes[0]
        self.end_node_name = self.selected_nodes[1]
        self.build_route()

    def add_edge(self, from_node, to_node):
        if from_node in self.nodes and to_node in self.nodes:
            x1, y1 = self.nodes[from_node]
            x2, y2 = self.nodes[to_node]
            self.edges.append((from_node, to_node))
            self.canvas.create_line(x1, y1, x2, y2)

    def build_route(self):
        print(self.start_node_name, self.end_node_name)
        if self.start_node_name and self.end_node_name:
            start_node = self.get_node_by_name(self.start_node_name)
            end_node = self.get_node_by_name(self.end_node_name)
            if start_node and end_node:
                path = self.pathfinder.getPath(self.graph, start_node, end_node)
                print(path)

                if path:
                    path_names = [node.name for node in path.get_node_list()]
                    self.highlight_path(path_names)
                else:
                    messagebox.showinfo("Путь не найден", "Не удалось найти путь между указанными узлами.")
        self.selected_nodes.clear()  # Очищаем выбранные узлы после построения маршрута

    def get_node_by_name(self, name):
        for node in self.graph.graph.keys():
            if node.name == name:
                return node
        return None

    def LoaderMenu_SelectionEvent(self, event):
        s = self.loader_var.get()
        q = self.file_entry.get()
        if s == "Обычный заргузчик":
            self.loader = GraphFileLoader(q)
        elif s == "Фаил с координатами":
            self.loader = GraphWithCoordinatesLoader(q)
        else:
            messagebox.showerror("Ошибка", "Неизвестный загрузчик")


    def highlight_path(self, path: list[str]):
        if len(path) < 2:
            return
        for i in range(len(path) - 1):
            from_node = path[i]
            to_node = path[i + 1]
            if (from_node, to_node) in self.edges or (to_node, from_node) in self.edges:
                x1, y1 = self.nodes[from_node]
                x2, y2 = self.nodes[to_node]
                self.current_path_items.append(
                    self.canvas.create_line(x1, y1, x2, y2, fill="red", width=3)
                )

        first_node_name = path[0]
        xf, yf = self.nodes[first_node_name]
        self.current_path_items.append(
            self.canvas.create_oval(xf - 10, yf - 10, xf + 10, yf + 10, fill="orange", width=2)
        )

        last_node_name = path[-1]
        xf, yf = self.nodes[last_node_name]
        self.current_path_items.append(
            self.canvas.create_oval(xf - 10, yf - 10, xf + 10, yf + 10, fill="pink", width=2))

    # Определяем границы графа для автоматического масштабирования
    # min_x = min(node.x for node in self.graph.keys())
    # max_x = max(node.x for node in self.graph.keys())
    # min_y = min(node.y for node in self.graph.keys())
    # max_y = max(node.y for node in self.graph.keys())

    # canvas_width = self.canvas.winfo_width()
    # canvas_height = self.canvas.winfo_height()

    # x_scale = (canvas_width - 40) / (max_x - min_x) if max_x - min_x > 0 else 1


# y_scale = (canvas_height - 40) / (max_y - min_y) if max_y - min_y > 0 else 1

# scale = min(x_scale, y_scale)

# offset_x = (canvas_width - (max_x - min_x) * scale) / 2 - min_x * scale
# offset_y = (canvas_height - (max_y - min_y) * scale) / 2 - min_y * scale


root = tk.Tk()
root.title("Рисовалка графов")
app = GraphDrawer(root)
app.run()
