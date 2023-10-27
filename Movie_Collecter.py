class TreeNode:
    def __init__(self, title):
        self.title = title
        self.left = None
        self.right = None

class MovieCollection:
    def __init__(self):
        self.root = None

    def insert(self, title):
        if self.root is None:
            self.root = TreeNode(title)
        else:
            result = self.check_insert(self.root, title)
            if result is False:
                print(f"Error: Movie '{title}' already exists in the collection.")
            else:
                self.save_to_file(title)  

    def check_insert(self, node, title):
        if title == node.title:
            return False
        elif title < node.title:
            if node.left is None:
                node.left = TreeNode(title)
            else:
                return self.check_insert(node.left, title)
        else:
            if node.right is None:
                node.right = TreeNode(title)
            else:
                return self.check_insert(node.right, title)

        return True

    def search(self, title):
        return self.check_search(self.root, title)

    def check_search(self, node, title):
        if node is None:
            return False
        if title == node.title:
            return True
        elif title < node.title:
            return self.check_search(node.left, title)
        else:
            return self.check_search(node.right, title)

    def delete(self, title):
        self.root = self.check_delete(self.root, title)
        self.delete_from_file(title)  

    def check_delete(self, node, title):
        if node is None:
            return node

        if title < node.title:
            node.left = self.check_delete(node.left, title)
        elif title > node.title:
            node.right = self.check_delete(node.right, title)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._find_min(node.right)
            node.title = temp.title
            node.right = self._delete(node.right, temp.title)

        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def create(self, movie_list):
        for movie in movie_list:
            self.insert(movie)

    def display_tree(self):
        self._display_tree(self.root, 0)

    def _display_tree(self, node, level):
        if node is not None:
            self._display_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.title)
            self._display_tree(node.left, level + 1)

    def display_formatted_tree(self):
        self._display_formatted_tree(self.root, 0)

    def _display_formatted_tree(self, node, level):
        if node is not None:
            print('    ' * level, end='')
            print('->', node.title)
            if node.left is not None or node.right is not None:
                self._display_formatted_tree(node.left, level + 1)
                self._display_formatted_tree(node.right, level + 1)

    def save_to_file(self, title):
        with open('movie_collection.txt', 'r') as file:
            lines = file.readlines()
            if title in [line.strip() for line in lines]:
                print(f"Error: Movie '{title}' already exists in the collection.")
                return

        with open('movie_collection.txt', 'a') as file:
            file.write(title + '\n')

    def delete_from_file(self, title):
        with open('movie_collection.txt', 'r') as file:
            lines = file.readlines()
        with open('movie_collection.txt', 'w') as file:
            for line in lines:
                if line.strip() != title:
                    file.write(line)

    def load_from_file(self):
        try:
            with open('movie_collection.txt', 'r') as file:
                movies = file.readlines()
                self.create([movie.strip() for movie in movies])
        except FileNotFoundError:
            pass

#Setting
movie_collection = MovieCollection()
movie_collection.load_from_file()
movies = []
movie_collection.create(movies)

def display_list():
    with open('movie_collection.txt', 'r') as file:
        print("\nMovies in file:")
        print(file.read())

def main_menu():
    print("")
    print("Welcome to Movie Collecter")
    print("")
    print("1 - Insert or Add")
    print("2 - Delete")
    print("3 - Search and view")
    print("")
    ans = input("")
    if(ans == "1"):
        add_menu()
    elif(ans == "2"):
        delete_menu()
    elif(ans == "3"):
        search_menu()
    else:
        print("Invalid Value")
        main_menu()

def add_menu():
    print("")
    print("Into Add Page")
    print("")
    print("Which Movie toy want to add")
    ans = input("")
    movie_collection.insert(ans)
    main_menu()

def delete_menu():
    print("")
    print("Delete Add Page")
    print("")
    display_list()
    print("Which Movie you want to delete")
    ans = input("")
    movie_collection.delete(ans)
    print(f" {ans} has been delete")
    main_menu()

def search_menu():
    print("")
    print("Search Add Page")
    print("")
    print("1 - Print List")
    print("2 - Print Tree")
    print("3 - Search")
    print("")
    ans = input("")
    if(ans == "1"):
        display_list()
        main_menu()
    if(ans == "2"):
        print("Which tree do u prefer")
        print("1 - Root at the center")
        print("2 - Root on top Left")
        ans2 = input("")
        if(ans2 == "1"):
            movie_collection.display_tree()
            main_menu()
        elif(ans2 == "2"):
            movie_collection.display_formatted_tree()
            main_menu()
    if(ans == "3"):
        print("What name of the movie that you want to search")
        ans3 = input("")
        if(movie_collection.search(ans3)):
            print("Movie found")
            main_menu()
        else:
            print("Movie not found")
            main_menu()
