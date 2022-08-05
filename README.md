# challenge-memd-api-py
Python API Code challenge

### 3rd API Party Integration

### Prerequisites

- Have python 3.10 installed in your local machine
- Docker is optional

### How to use this repository

1. Download or clone this repository

```bash
git clone https://github.com/alehpineda/challenge-memd-api-py.git
```

2. Install requirements

```bash
cd challenge-memd-api-py
pip install -r requirements.txt
```

3. Run the api

```bash
# inside folder challenge-memd-api-py
cd app
uvicorn main:app --port --reload
```

4. Go to the swagger docs to test the api. You will need a bearer token.

```bash
# Uvicorn uses 8000 by default. You can change it 
localhost:8000/docs
```

5. If you have Docker installed, you can build the image and run it. In this case you can go to `localhost:80/docs` to check the swagger docs.

```bash
# inside folder challenge-memd-api-py
docker image build -t challenge_api_py .
docker container run -d -p 80:80 challenge_api_py
```

6. You can also use `docker-compose`. If you want to change the port, you can do it in the `docker-compose.yml` file.

```bash
# inside folder challenge-memd-api-py
docker-compose up -d
# If you want to stop it
docker-compose down
```


### Endpoints

#### Note: All endpoints require a bearer token

- /v1/member/primary
  - Post request - This takes the below payload and creates a Primary Member
  - Payload:

```json
      {
      "member": { 
        "external_id":    1010,
        "relationship":   18,  // Valid value:    18
        "first_name":     "Test1010",
        "last_name":      "Test1010",
        "gender":         "F",  // Valid values:   "M" or "F"
        "plancode":       "11AA22BB", // Valid value:    "11AA22BB"
        "street_1":       "742 Evergreen Terrace",
        "street_2":       "APT 123",
        "city":           "Springfield",
        "state":          "NY",  // # Example values: "FL" or "NY"
        "zipcode":        "12345",
        "dob":            "1980-01-01",
        "benefit_start":  "2022-08-01"
      }
    }
```

- /v1/member/dependant/:primary_member_id
  - Post request - This takes the below payload and creates a Dependent Member
  - Notes: The payload is identical to POST#create for primary members with this exception

```json
        {
          "relationship":   "integer",    //Valid value:    19
        }
```

  - Payload:

```json
        {
          "member": { 
            "external_id":    1011,
            "relationship":   19,
            "first_name":     "Test1011",
            "last_name":      "Test1011",
            "gender":         "F",
            "plancode":       "11AA22BB",
            "street_1":       "",
            "street_2":       "",
            "city":           "",
            "state":          "",
            "zipcode":        "",
            "dob":            "1980-01-01",
            "benefit_start":  "2022-08-01"
          }
        }

```

- /v1/member/retrieve/:member_id
  - Simply retrieves a Member via the external_id field

