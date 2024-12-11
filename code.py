import tkinter as tk


class Point:
    """Класс Точки"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, canvas, size=6, color="black"):
        """Создание точки"""
        canvas.create_oval(
            self.x - size // 2, self.y - size // 2,
            self.x + size // 2, self.y + size // 2,
            fill=color, outline=color
        )


class Line:
    """Класс Линии"""
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def draw(self, canvas, width=3, color="blue"):
        """Создание линии"""
        canvas.create_line(
            self.start_point.x, self.start_point.y,
            self.end_point.x, self.end_point.y,
            width=width, fill=color
        )


class GraphicEditorApp:
    """Класс всего приложения"""
    def __init__(self, root):
        self.root = root
        self.root.title("Графический редактор")

        # Режим Рисование
        self.drawing_mode = "points_and_lines"  # "points_and_lines" или "free_draw"

        # Кнопки для управления
        self.clear_button = tk.Button(self.root, text="Очистить", command=self.clear_canvas)
        self.clear_button.pack(side=tk.TOP, padx=5, pady=5)

        self.points_lines_button = tk.Button(self.root, text="Точки и линии", command=self.set_points_and_lines_mode)
        self.points_lines_button.pack(side=tk.TOP, padx=5, pady=5)

        self.free_draw_button = tk.Button(self.root, text="Рисование", command=self.set_free_draw_mode)
        self.free_draw_button.pack(side=tk.TOP, padx=5, pady=5)

        # Создание Канваса (холста)
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Перечень точек
        self.points = []

        # События на канвасе
        self.canvas.bind("<Button-1>", self.on_mouse_click)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)

        # Последняя позиция мыши
        self.last_x, self.last_y = None, None

    def set_points_and_lines_mode(self):
        """Режим 'Точки и линии'"""
        self.drawing_mode = "points_and_lines"

    def set_free_draw_mode(self):
        """Режим 'Рисование'"""
        self.drawing_mode = "free_draw"

    def on_mouse_click(self, event):
        """ЛКМ - нажатие"""
        if self.drawing_mode == "points_and_lines":
            self.add_point(event)

    def on_mouse_drag(self, event):
        """Движение Мыши с зажатой ЛКМ"""
        if self.drawing_mode == "free_draw":
            self.free_draw(event)

    def add_point(self, event):
        """Точка и соединение с линией"""
        new_point = Point(event.x, event.y)
        new_point.draw(self.canvas)

        if self.points:
            # Соединение линией с последней точкой
            previous_point = self.points[-1]
            line = Line(previous_point, new_point)
            line.draw(self.canvas)

        self.points.append(new_point)

    def free_draw(self, event):
        """Свободное рисование"""
        if self.last_x is not None and self.last_y is not None:
            self.canvas.create_line(
                self.last_x, self.last_y, event.x, event.y,
                width=2, fill="red"
            )
        self.last_x, self.last_y = event.x, event.y

    def clear_canvas(self):
        """Очищает холст полностью"""
        self.canvas.delete("all")
        self.points = []
        self.last_x, self.last_y = None, None


if __name__ == "__main__":
    root = tk.Tk()
    app = GraphicEditorApp(root)
    root.mainloop()