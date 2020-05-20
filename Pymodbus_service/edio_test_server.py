import select
import event_driven_i_o as edio


def event_loop(handlers):
    while True:
        wants_recv = [h for h in handlers if h.wants_to_receive()]
        wants_send = [h for h in handlers if h.wants_to_send()]
        can_recv, can_send, _ = select.select(wants_recv, wants_send, [])
        for h in can_recv:
            h.handle_receive()
        for h in can_send:
            h.handle_send()


if __name__ == '__main__':
    handlers = []
    # For Infolite EDD instead of EchoClient handler below, can add a handler
    # that receives the data from DBserver client monitoring FTPShare dispatch info,
    # and then kicks off writing the recieved data to RTU
    handlers.append(edio.TCPServer(('', 16000), edio.TCPEchoClient, handlers))
    event_loop(handlers)
