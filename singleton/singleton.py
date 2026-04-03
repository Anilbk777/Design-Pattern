def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class DataBaseConnection:
    def __init__(self, host:str, port:int):
        self.host = host
        self.port = port
        print(f"Creating connection to {host}:{port}")


if __name__ == "__main__":
    db1 = DataBaseConnection("localhost", 5432)
    print(f"Instance 1 : {id(db1)}")

    db2 = DataBaseConnection("localhost", 5432)
    print(f"Instance 2 : {id(db2)}")

    print(f"Same instance? {db1 is db2}")
