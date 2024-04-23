from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from typing import List

@dataclass()
class GeologyModel:
    soil_name : str
    layer_thick : float
    unit_weight : float
    friction_angle : float
    effective_cohesion : float

@dataclass()
class UdlModel:
    magnitude : float
    offset_from_crest : float
    load_len : float

@dataclass()
class PointLoadModel:
    magnitude : float
    offset_from_crest : float


class LandModel(BaseModel):
    slope_height : float
    slope_len : float
    water_depth : float
    geology : List[GeologyModel]
    udl : List[UdlModel]
    point_load : List[PointLoadModel]