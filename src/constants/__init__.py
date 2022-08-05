from enum import Enum, unique

# Router prefix
MEMBER_PREFIX = "/v1/member"

# Tags
GET_TAG = "GET"
POST_TAG = "POST"

# urls
RETRIEVE_MEMBER_URL = "http://cratebind-challenge-api.com/memd/members/"
CREATE_PRIMARY_MEMBER_URL = "http://cratebind-challenge-api.com/memd/members"
CREATE_DEPENDENT_MEMBER_URL = (
    "http://cratebind-challenge-api.com/memd/members/"
)

# Timeout
TIMEOUT = 30

# key
ERROR = "error"
EXTERNAL_ID = "external_id"


@unique
class Relationship(Enum):
    relationship = 18


@unique
class DependantRelationship(Enum):
    relationship = 19


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
    X = ""
