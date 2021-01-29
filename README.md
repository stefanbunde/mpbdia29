# MPTBIA2910

Welcome to MPTBIA2910's documentation.


## Flask app

The purpose of the Flask app is to request another web service (`icanhazdadjoke.com`), parse the response and output dad jokes.

Currently just one endpoint is provided: `/get_jokes/<number_of_jokes>`.

This endpoint prints out `number_of_jokes` jokes. They are displayed with a numbering and with a linebreak after every joke.

Attention: No error handling is implemented, so far. You should take care, that `number_of_jokes` is greater or equals with `1`.

The Flask app sends a request to another web service for every singe joke. Because of long loading times `number_of_jokes` shouldn't be geater than 25. For me it takes about 8 seconds to load 25 jokes. If you are willing to put up with long waiting times, you can of course choose much larger numbers.


## Docker container

The Flask app is deployed into a Docker container, which can be downloaded from the Dockerhub.
To download and start the container just type

	docker run --name mptbia2901 stefanbunde/mptbia2901:latest

To figure out the ip address of your container run

	docker inspect -f '{{.NetworkSettings.IPAddress}}' mptbia2901

Now you can open your browser and go to

	<container_ip_address>:8000/get_jokes/<number_of_jokes>
