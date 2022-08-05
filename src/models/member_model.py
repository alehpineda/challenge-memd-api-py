from typing import Optional
from pydantic import BaseModel
from datetime import date
from src.constants import (
    Relationship,
    Gender,
    Plancode,
    State,
    DependantRelationship,
)


class Member(BaseModel):
    external_id: int
    relationship: Relationship  # Valid value: 18
    first_name: str
    last_name: str
    gender: Gender  # Valid values: "M" or "F"
    plancode: Plancode  # Valid value: "11AA22BB"
    street_1: str
    street_2: Optional[str] = ""  # Optional
    city: str
    state: State  # Example values: "FL" or "NY"
    zipcode: str
    dob: date
    benefit_start: date


class Dependant(Member):
    relationship: DependantRelationship
    street_1: Optional[str] = ""  # Optional
    city: Optional[str] = ""  # Optional
    state: Optional[State] = ""  # Optional | Example values: "FL" or "NY"
    zipcode: Optional[str] = ""  # Optional


class PrimaryMember(BaseModel):
    member: Member


class DependentMember(BaseModel):
    member: Dependant
