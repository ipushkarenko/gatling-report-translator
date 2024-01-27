import glob
import json
from typing import List

# Assume DTO classes and mapping functions (map_to_dto, etc.) are already defined
from _gtl_json_dto import GatlingStatsDto, RequestStats, TimeStats, Percentile, Request, Group, GroupStats


# Define your DTO classes here (as shown in the previous message)


def _map_to_dto(data: dict) -> GatlingStatsDto:
    # Map the main attributes
    root = GatlingStatsDto(
        type=data['type'],
        name=data['name'],
        path=data['path'],
        pathFormatted=data['pathFormatted'],
        stats=_map_group_stats(data['stats']),
        contents={key: _map_request(val) for key, val in data['contents'].items()}
    )
    return root


def _map_group_stats(data: dict) -> GatlingStatsDto:
    # Map the GroupStats attributes
    return GroupStats(
        name=data['name'],
        numberOfRequests=RequestStats(**data['numberOfRequests']),
        minResponseTime=TimeStats(**data['minResponseTime']),
        maxResponseTime=TimeStats(**data['maxResponseTime']),
        meanResponseTime=TimeStats(**data['meanResponseTime']),
        standardDeviation=TimeStats(**data['standardDeviation']),
        percentiles1=Percentile(**data['percentiles1']),
        percentiles2=Percentile(**data['percentiles2']),
        percentiles3=Percentile(**data['percentiles3']),
        percentiles4=Percentile(**data['percentiles4']),
        group1=Group(**data['group1']),
        group2=Group(**data['group2']),
        group3=Group(**data['group3']),
        group4=Group(**data['group4']),
        meanNumberOfRequestsPerSecond=TimeStats(**data['meanNumberOfRequestsPerSecond'])
    )


def _map_request(data: dict) -> Request:
    # Map the Request attributes
    return Request(
        type=data['type'],
        name=data['name'],
        path=data['path'],
        pathFormatted=data['pathFormatted'],
        stats={k: v for k, v in data['stats'].items()}
    )


def _read_json_file(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        return json.load(file)


def download_gtl_statistic(directory: str) -> List[GatlingStatsDto]:
    # Create a list of all .json files in the directory
    file_paths = glob.glob(f'{directory}/*.json')

    # Create DTOs from the .json files
    dtos = []
    for file_path in file_paths:
        data_dict = _read_json_file(file_path)
        dto = _map_to_dto(data_dict)
        dtos.append(dto)

    return dtos

