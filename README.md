# watch_next

This project demonstrates semantic similarity analysis using spaCy.

## Prerequisites

- Python 3.11.5
- Docker (if you prefer running the script in a container)

## Installation

Clone this repository: git clone https://github.com/vdp11/watch_next.git
   cd watch

## Usage
Running the Semantic Similarity Analysis
To analyze semantic similarity between movie titles and description, run the watch_next.py script:

'''bash

python watch/watch_next.py

Running the Docker Container
Alternatively, you can run the script in a Docker container:

Build the Docker image (from the root of the repository):

'''bash

docker build -t watch_next .


And then run the Docker container:

'''bash

docker run watch_next

## Results
The script will calculate and display semantic similarity scores between movie title and description.
When run in a Docker container, the results will be shown in the container's terminal.
