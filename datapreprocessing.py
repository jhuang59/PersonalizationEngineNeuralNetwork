import pandas as pd
class preprocessor():
    def __init__(self,path:str) -> None:
        self.data=pd.read_csv(path)