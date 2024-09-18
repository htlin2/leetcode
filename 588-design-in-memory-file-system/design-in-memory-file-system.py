class TrieNode:
    def __init__(self):
        self.children = {}
        self.content = ''

class FileSystem:
    def __init__(self):
        self.root = TrieNode()        

    def create_file_path(self, path):
        node = self.root
        paths = path.split('/')
        for p in paths[1:]:
            if p == '': continue
            if not p in node.children:
                node.children[p] = TrieNode()
            node = node.children[p]
        return node

    def ls(self, path: str) -> List[str]:
        node = self.root
        paths = path.split('/')
        for p in paths[1:]:
            if p == '': continue
            if not p in node.children:
                return []
            node = node.children[p]
        if node.content:
            return [paths[-1]]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        node = self.create_file_path(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.create_file_path(filePath)
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self.create_file_path(filePath)
        return node.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
"""
["FileSystem"
"mkdir"
"ls"
"mkdir"
"ls"
"ls"
"ls"
"addContentToFile"
"ls"
"ls" / => ["dycete","m","w"]
"ls" /dycete => ["dycete"]
]

"""