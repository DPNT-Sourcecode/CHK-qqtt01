from solutions.HLO.constants import DEFAULT_MESSAGE


class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name: str | None = None) -> str:
        if is not friend_name:
            return DEFAULT_MESSAGE
        return f"Hello {friend_name}!"
