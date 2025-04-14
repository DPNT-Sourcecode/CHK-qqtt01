
class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name: str | None = None) -> str:
        if friend_name is None:
            return "Hi there!"
        return f"Hello {friend_name}!"


