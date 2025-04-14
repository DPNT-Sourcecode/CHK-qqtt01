from solutions.HLO.constants import DEFAULT_MESSAGE


class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name: str | None = None) -> str:
        if friend_name is not None:
            friend_name = friend_name.strip()
        if not friend_name:
            return DEFAULT_MESSAGE
        return f"Hello, {friend_name}!"



