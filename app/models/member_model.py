from typing import Optional
from pydantic import BaseModel
from datetime import date
from constants import (
    Relationship,
    Gender,
    Plancode,
    State,
    DependantRelationship,
)


class Member(BaseModel):
    """Member class

    Args:
        BaseModel (): Pydantic base model
    """

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


class Dependent(Member):
    """Dependent Member class

    Args:
        Member (_type_): Inherits from Member class
    """

    relationship: DependantRelationship
    street_1: Optional[str] = ""  # Optional
    city: Optional[str] = ""  # Optional
    state: Optional[State] = ""  # Optional | Example values: "FL" or "NY"
    zipcode: Optional[str] = ""  # Optional


class PrimaryMember(BaseModel):
    """Primary Member class

    Args:
        BaseModel (_type_): Pydantic base model
    """

    member: Member


class DependentMember(BaseModel):
    """Dependent Member class

    Args:
        BaseModel (_type_): Pydantic base model
    """

    member: Dependent
