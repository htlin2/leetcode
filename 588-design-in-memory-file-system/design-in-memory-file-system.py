class TrieNode:
    def __init__(self):
        self.content = ''
        self.children = {}
        self.is_file = False

class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        node = self.root
        paths = path.split('/')
        for p in paths[1:]:
            if p in node.children:
                node = node.children[p]
        if node.is_file:
            return [paths[-1]]
        return sorted(node.children.keys())


    def createDir(self, path):
        node = self.root
        paths = path.split('/')
        for p in paths[1:]:
            if not p in node.children:
                node.children[p] = TrieNode()
            node = node.children[p]
        return node

    def mkdir(self, path: str) -> None:
        self.createDir(path=path)


    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.createDir(path=filePath)
        node.content += content
        node.is_file = True

    def readContentFromFile(self, filePath: str) -> str:
        node = self.createDir(path=filePath)
        return node.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)