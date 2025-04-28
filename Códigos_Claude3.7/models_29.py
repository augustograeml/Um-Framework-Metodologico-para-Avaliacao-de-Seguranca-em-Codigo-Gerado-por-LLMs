class Repository:
    def __init__(self, name, url, description):
        self.name = name
        self.url = url
        self.description = description

    def __repr__(self):
        return f"Repository(name={self.name}, url={self.url}, description={self.description})"