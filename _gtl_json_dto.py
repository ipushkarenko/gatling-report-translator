from dataclasses import dataclass
from typing import List, Dict


@dataclass
class RequestStats:
    total: int
    ok: int
    ko: int


@dataclass
class TimeStats:
    total: int
    ok: int
    ko: int


@dataclass
class Percentile:
    total: int
    ok: int
    ko: int


@dataclass
class Group:
    name: str
    htmlName: str
    count: int
    percentage: int


@dataclass
class Request:
    type: str
    name: str
    path: str
    pathFormatted: str
    stats: Dict[str, Dict[str, int]]


@dataclass
class GroupStats:
    name: str
    numberOfRequests: RequestStats
    minResponseTime: TimeStats
    maxResponseTime: TimeStats
    meanResponseTime: TimeStats
    standardDeviation: TimeStats
    percentiles1: Percentile
    percentiles2: Percentile
    percentiles3: Percentile
    percentiles4: Percentile
    group1: Group
    group2: Group
    group3: Group
    group4: Group
    meanNumberOfRequestsPerSecond: TimeStats


@dataclass
class GatlingStatsDto:
    type: str
    name: str
    path: str
    pathFormatted: str
    stats: GroupStats
    contents: Dict[str, Request]
