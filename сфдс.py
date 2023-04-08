from py2neo import Graph, Node, Relationship

graph = Graph("http://127.0.0.1:7687", auth=("username", "password"))

# Создайте узел, представляющий изображение
image_node = Node("Image", name="filename.png")
graph.create(image_node)

# Создайте узел, представляющий GDSII-файл
gdsii_node = Node("GDSII", name="4004.gds")
graph.create(gdsii_node)

# Создайте отношение между узлами изображения и GDSII-файла
rel = Relationship(image_node, "GENERATED_FROM", gdsii_node)
graph.create(rel)
