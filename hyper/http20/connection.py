# -*- coding: utf-8 -*-
"""
hyper/http20/connection
~~~~~~~~~~~~~~~~~~~~~~~

Objects that build hyper's connection-level HTTP/2.0 abstraction.
"""
class HTTP20Connection(object):
    """
    An object representing a single HTTP/2.0 connection to a server.

    This object behaves similarly to the Python standard library's
    HTTPConnection object, with a few critical differences.
    """
    def __init__(self, host, port=None, **kwargs):
        """
        Creates an HTTP/2.0 connection to a specific server.

        Most of the standard library's arguments to the constructor are
        irrelevant for HTTP/2.0 or not supported by hyper.
        """
        if port is None:
            try:
                self.host, self.port = host.split(':')
                self.port = int(self.port)
            except ValueError:
                self.host, self.port = host, 443
        else:
            self.host, self.port = host, port

    def request(self, method, url, body=None, headers={}):
        """
        This will send a request to the server using the HTTP request method
        ``method`` and the selector ``url``. If the ``body`` argument is
        present, it should be string or bytes object of data to send after the
        headers are finished. Strings are encoded as UTF-8. To use other
        encodings, pass a bytes object. The Content-Length header is set to the
        length of the body field.

        Returns a stream ID for the request.
        """
        pass

    def getresponse(self, stream_id=None):
        """
        Should be called after a request is sent to get a response from the
        server. If sending multiple parallel requests, pass the stream ID of
        the request whose response you want. Returns a HTTPResponse instance.
        If you pass no stream_id, you will receive the oldest HTTPResponse
        still outstanding.
        """
        pass

    def connect(self):
        """
        Connect to the server specified when the object was created.
        """
        pass

    def close(self):
        """
        Close the connection to the server.
        """
        pass

    def putrequest(self, method, selector, **kwargs):
        """
        This should be the first call for sending a given HTTP request to a
        server. It returns a stream ID for the given connection that should be
        passed to all subsequent request building calls.
        """
        pass

    def putheader(self, header, argument, stream_id=None):
        """
        Sends an HTTP header to the server, with name ``header`` and value
        ``argument``.

        Unlike the httplib version of this function, this version does not
        actually send anything when called. Instead, it queues the headers up
        to be sent when you call ``endheaders``.
        """
        pass

    def endheaders(self, message_body=None, final=False, stream_id=None):
        """
        Sends the prepared headers to the server. If the ``message_body``
        argument is provided it will also be sent to the server as the body of
        the request, and the stream will immediately be closed. If the
        ``final`` argument is set to True, the stream will also immediately
        be closed: otherwise, the stream will be left open and subsequent calls
        to ``send()`` will be required.
        """
        pass

    def send(self, data, final=False, stream_id=None):
        """
        Sends some data to the server. This data will be sent immediately
        (excluding the normal HTTP/2.0 flow control rules). If this is the last
        data that will be sent as part of this request, the ``final`` argument
        should be set to ``True``. This will cause the stream to be closed.
        """
        pass