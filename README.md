#FMN.SSE

## Install
```
sudo dnf install python python-virtualenvwrapper rabbitmq-server python-pip 
mkvirtualenv sse
workon sse
pip install -r ./requirements.txt
```

also install the requirements for dev-data and testing

```
pip install -r ./requirements-test.txt
```

## Running

```
workon sse
PYTHONPATH=. python fmn/sse/sse_webserver.py
```

## Test Data

```
workon sse
python dev-data.py
```

## Manual Testing

`sse_webserver.py` curl seems to work okay for me `curl http://localhost:8080/user/bob`

and/or

open up `sse_test_subscriber.html` in a browser and look at the JS console

## Running unittests
Unfortuanately after converting the project to fmn structure the coverage does
not work anymore.

You can still run unittests but the percentage can't be determined at the moment.

Please run in the root of the project

```
workon sse
trial tests/*.py
```

*Deprecated*

    cd to the root of the project
    ```
    workon sse
    pip install -r ./requirements-test.txt
    python run-test.py
    ```

    ------

    #### Manual way

    ```
    workon sse
    trial --coverage ./tests/test_sse_webserver.py
    ```
    Coverage results will be in root_project/_trial_temp/coverage/

### Common issues

Q: I can't connect to rabbitmq with pika

A: Make sure you are running rabbitmq `sudo systemctl start rabbitmq-server`

Q: I get the following error
```
pika.exceptions.ChannelClosed: (406, "PRECONDITION_FAILED - inequivalent arg 'x-message-ttl' for queue 'skrzepto.id.fedoraproject.org' in vhost '/': received '60000' but current is '86400000'")
```

A: You have set the queue a ttl that is not the same. You need to either match the ttl or delete the queue and retry.

Go into http://localhost:15672/  and delete the queue. Thats assuming you enabled the management plugin https://www.rabbitmq.com/management.html

Q: Nothing is being displayed on the curl

A: Wait a few more seconds, it takes a moment to display the data. If it's more
than a minute check to see if the queue has data via the web ui http://localhost:15672/

