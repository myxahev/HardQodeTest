from dataclasses import dataclass


@dataclass
class ProductStat:
    id: int
    name: str
    num_students: int
    avg_group_fill: float
    access_percentage: float
