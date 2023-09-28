# import uvicorn


async def read_body(receive):
    """
    Read and return the entire body from an incoming ASGI message.
    """
    # body = b""
    blippy = b""
    # more_body = True
    more_blippody = True

    while more_blippody:
        message = await receive()
        print(f"received msg {message.get('body', b'')}")
        blippy += message.get("body", b"") + b" "
        more_blippody = message.get(
            "more_body", False
        )  # checks if the request is done sending messages

    return blippy


async def app(scope, receive, send):
    assert scope["type"] == "http"

    body = await read_body(receive)

    await send(
        {
            "type": "http.response.start",
            "status": 200,
            "headers": [
                [b"content-type", b"text/plain"],
            ],
        }
    )

    await send(
        {
            "type": "http.response.body",
            "body": body,
        }
    )
    print(f"Full request message: {body}")


# if __name__ == "__main__":
#     uvicorn.run("stream_eventloop:app", host='127.0.0.1', port='9000', log_level="info")
