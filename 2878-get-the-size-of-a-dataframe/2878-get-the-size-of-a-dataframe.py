import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)
    # return [players.shape[0], players.shape[1]]