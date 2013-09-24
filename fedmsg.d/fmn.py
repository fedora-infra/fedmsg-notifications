import socket
hostname = socket.gethostname().split('.')[-1]

config = {
    # Consumer stuff
    "fmn.consumer.enabled": True,
    "fmn.sqlalchemy.uri": "sqlite:////var/tmp/fmn-dev-db.sqlite",


    ## Backend stuff ##
    # Email
    "fmn.email.mailserver": "127.0.0.1:25",
    "fmn.email.from_address": "fedmsg-notifications@fedoraproject.org",

    # IRC
    "fmn.irc.network": "irc.freenode.net",
    "fmn.irc.nickname": "threebot",
    "fmn.irc.port": 6667,
    "fmn.irc.timeout": 120,

    # GCM
    "fmn.gcm.post_url": "wat",
    "fmn.gcm.api_key": "wat",


    # Generic stuff
    "endpoints": {
        "fmn.%s" % hostname: [
            "tcp://127.0.0.1:3041",
        ],
    },
    "logging": dict(
        loggers=dict(
            fmn={
                "level": "DEBUG",
                "propagate": False,
                "handlers": ["console"],
            },
        ),
    ),
}
