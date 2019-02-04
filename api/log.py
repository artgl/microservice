import api.configuration


def post(message_id, message):
    (target, code) = api.configuration.get("target")
    if code == 200:
        return "Message '%s' logged to %s" % (message, target), 200
    else:
        return "No log target is configured", 422
