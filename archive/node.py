import uuid


class miner:
    pass


class validator:
    pass


class user:
    pass


class admin:
    pass


class node:
    def __init__(self, role=user()):
        self.role = role
        self.id = uuid.uuid1()


if __name__ == "__main__":
    n = node(admin())
    print(f"{n.role}:{n.id}")
