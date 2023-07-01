# Inspiration
The inspirations for this website were seeing the amount of pets that need to be adopted in the world, these are typically posted on various websites throughout the UK. The inspiration is to get more pets in their forever homes.

# What it does
Hosts animals from all over the UK, where people can easily find out about the animal, how to adopt them and where to adopt them. It runs a flask API in a docker container with a /pets endpoint consumed on the frontend. The data comes from bluecross, a pet adoption website for the UK.

# How we built it
The backend calls all the scrapers at once asyncly (just 1 for now but it's built to be easily extensible). Each scraper calls all the pages of data at once. It collects all the data together in one big list and returns it to the frontend, These are sent to the frontend for display so users can easily browse through all the animals available across these websites. The API runs in a docker container with poetry as a package manager. There are 2 make targets to easily build and run the container for the backend.

# Challenges we ran into
Building multiples scrapers for multiple sites. Due to time constraints we started with 1 site for proof-of-concept.
Making a responsive UI across all screen-types.
TIMEZONES

# Accomplishments that we're proud of
We built a full-stack application from scratch within 24-hours!

# Technologies
1. API
2. ReactJS
3. docker
4. flask
5. poetry
6. python

# See more 
    https://devpost.com/software/adopt-stop

# Adopt Spot - Client

### Install
` bash
    npm i
    npm install
    yarn install
`

### Start client
` bash 
    npm run start
    yarn start
`

### Using react-responsive 
- Download here or use yarn install
- `https://www.npmjs.com/package/react-responsive`

# Adopt Spot - Server

### Get page of pets
#### `/pets`
```json
{
    "results": [
        {
            "age":"10 and 1 month(s)",
            "breed": "",
            "color":"Tan",
            "contact":"",
            "description":"",
            "location":"West Midlands: Bromsgrove rehoming centre",
            "name":"Duke",
            "pic":"https://www.bluecross.org.uk//sites/default/files/d8/722322.jpg",
            "sex":"Male",
            "species":"dog",
            "url":"https://www.bluecross.org.uk/pet/duke-1138958"
        },
    ],
}
```

## Running the backend Flask API
See the README in adopt-spot-backend for more info.
### With docker
- Ensure that docker is installed (docker desktop works)
- `cd Adopt Spot - Server`
- `make build-docker`
- `make run-docker`
- By default, the API is exposed on localhost:8000. Call it with
  
  `curl localhost:8000/pets`
### Without docker
- Install [poetry](https://python-poetry.org/)
- `cd Adopt Spot - Server`
- `make start-api`
- `curl localhost:8000/pets`

<!-- ### Get a specific pet
#### `/pet/{id}`
```
{
    "age":"10 and 1 month(s)",
    "breed":null,
    "color":"Tan",
    "contact":"",
    "description":"",
    "location":"West Midlands: Bromsgrove rehoming centre",
    "name":"Duke",
    "pic":"https://www.bluecross.org.uk//sites/default/files/d8/722322.jpg",
    "sex":"Male",
    "species":"dog",
    "url":"https://www.bluecross.org.uk/pet/duke-1138958",
},
``` -->

# Credits
## This project was created by: 

[Gtoutin: gtoutin](https://github.com/gtoutin)

[Nandini: nandini92](https://github.com/nandini92)

[Becki: Beckibuzz93](https://github.com/Beckibuzz93)

[Jatin: jatin-dua](https://github.com/jatin-dua)

