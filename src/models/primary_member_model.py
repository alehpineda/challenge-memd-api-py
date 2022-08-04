from typing import Optional
from pydantic import BaseModel
from datetime import date
from enum import Enum, unique


@unique
class Relationship(Enum):
    relationship = 18


@unique
class Gender(Enum):
    Male = "M"
    Female = "F"


@unique
class Plancode(Enum):
    plancode = "11AA22BB"


@unique
class State(Enum):
    Alabama = "AL"
    Alaska = "AK"
    Arizona = "AZ"
    Arkansas = "AR"
    California = "CA"
    Colorado = "CO"
    Connecticut = "CT"
    Delaware = "DE"
    Florida = "FL"
    Georgia = "GA"
    Hawaii = "HI"
    Idaho = "ID"
    Illinois = "IL"
    Indiana = "IN"
    Iowa = "IA"
    Kansas = "KS"
    Kentucky = "KY"
    Louisiana = "LA"
    Maine = "ME"
    Maryland = "MD"
    Massachusetts = "MA"
    Michigan = "MI"
    Minnesota = "MN"
    Mississippi = "MS"
    Missouri = "MO"
    Montana = "MT"
    Nebraska = "NE"
    Nevada = "NV"
    New_Hampshire = "NH"
    New_Jersey = "NJ"
    New_Mexico = "NM"
    New_York = "NY"
    North_Carolina = "NC"
    North_Dakota = "ND"
    Ohio = "OH"
    Oklahoma = "OK"
    Oregon = "OR"
    Pennsylvania = "PA"
    Rhode_Island = "RI"
    South_Carolina = "SC"
    South_Dakota = "SD"
    Tennessee = "TN"
    Texas = "TX"
    Utah = "UT"
    Vermont = "VT"
    Virginia = "VA"
    Washington = "WA"
    West_Virginia = "WV"
    Wisconsin = "WI"
    Wyoming = "WY"


class Member(BaseModel):
    external_id: int
    relationship: Relationship  # Valid value: 18
    first_name: str
    last_name: str
    gender: Gender  # Valid values: "M" or "F"
    plancode: Plancode  # Valid value: "11AA22BB"
    street_1: str
    street_2: Optional[str] = None  # Optional
    city: str
    state: State  # Example values: "FL" or "NY"
    zipcode: str
    dob: date
    benefit_start: date


class PrimaryMember(BaseModel):
    member: Member
