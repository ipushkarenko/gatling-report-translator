from typing import List
from _gtl_json_dto import GatlingStatsDto
import pandas as pd


def create_dataframe_from_dtos(dtos: List[GatlingStatsDto]) -> pd.DataFrame:
    """
    Creates a pandas DataFrame from a list of GatlingStatsDto objects.

    :param dtos: List of GatlingStatsDto DTOs.
    :return: pandas DataFrame with the extracted data.
    """

    data = []
    for dto in dtos:
        for name, req in dto.contents.items():
            data.append({
                "Name": req.name,
                "Total requests": req.stats['numberOfRequests']['total'],
                "OK": req.stats['numberOfRequests']['ok'],
                "KO": req.stats['numberOfRequests']['ko'],
                "MRT[ms]": req.stats['meanResponseTime']['total']
            })

    return pd.DataFrame(data)


