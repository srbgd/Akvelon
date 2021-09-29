from dataclasses import dataclass


@dataclass
class Request:
    method: str
    data: dict
