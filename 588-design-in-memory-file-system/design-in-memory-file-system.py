class TrieNode:
    def __init__(self):
        self.children = {}
        self.content = ''

class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        # if file, return file's name
        # if directory, return files and directory names
            # The answer should in lexicographic order.
        node = self.root
        paths = path.split('/')
        for path in paths[1:]:
            if path in node.children:
                node = node.children[path]
        if node.content:
            return [paths[-1]]
        return sorted(node.children.keys())

    def createDire(self, path):
        node = self.root
        paths = path.split('/')
        for path in paths[1:]:
            if not path in node.children:
                node.children[path] = TrieNode()
            node = node.children[path]
        return node

    def mkdir(self, path: str) -> None:
        self.createDire(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.createDire(filePath)
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self.createDire(filePath)
        return node.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
"""
{
    children: {
        a: {
            children: {
                b: {
                    children: {}
                }
            }
        }
    }
    content: ''
}
"""