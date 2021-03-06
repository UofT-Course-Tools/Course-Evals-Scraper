"""
This type stub file was generated by pyright.
"""

from .status_codes import codes
from typing import Any, Optional

"""
This type stub file was generated by pyright.
"""
REDIRECT_STATI = (codes.moved, codes.found, codes.other, codes.temporary_redirect, codes.permanent_redirect)
DEFAULT_REDIRECT_LIMIT = 30
CONTENT_CHUNK_SIZE = 10 * 1024
ITER_CHUNK_SIZE = 512
class RequestEncodingMixin(object):
    @property
    def path_url(self):
        """Build the path URL to use."""
        ...
    
    @staticmethod
    def _encode_params(data):
        """Encode parameters in a piece of data.

        Will successfully encode parameters when passed as a dict or a list of
        2-tuples. Order is retained if data is a list of 2-tuples but arbitrary
        if parameters are supplied as a dict.
        """
        ...
    
    @staticmethod
    def _encode_files(files, data):
        """Build the body for a multipart/form-data request.

        Will successfully encode files when passed as a dict or a list of
        tuples. Order is retained if data is a list of tuples but arbitrary
        if parameters are supplied as a dict.
        The tuples may be 2-tuples (filename, fileobj), 3-tuples (filename, fileobj, contentype)
        or 4-tuples (filename, fileobj, contentype, custom_headers).
        """
        ...
    


class RequestHooksMixin(object):
    def register_hook(self, event, hook):
        """Properly register a hook."""
        ...
    
    def deregister_hook(self, event, hook):
        """Deregister a previously registered hook.
        Returns True if the hook existed, False if not.
        """
        ...
    


class Request(RequestHooksMixin):
    """A user-created :class:`Request <Request>` object.

    Used to prepare a :class:`PreparedRequest <PreparedRequest>`, which is sent to the server.

    :param method: HTTP method to use.
    :param url: URL to send.
    :param headers: dictionary of headers to send.
    :param files: dictionary of {filename: fileobject} files to multipart upload.
    :param data: the body to attach to the request. If a dictionary or
        list of tuples ``[(key, value)]`` is provided, form-encoding will
        take place.
    :param json: json for the body to attach to the request (if files or data is not specified).
    :param params: URL parameters to append to the URL. If a dictionary or
        list of tuples ``[(key, value)]`` is provided, form-encoding will
        take place.
    :param auth: Auth handler or (user, pass) tuple.
    :param cookies: dictionary or CookieJar of cookies to attach to this request.
    :param hooks: dictionary of callback hooks, for internal usage.

    Usage::

      >>> import requests
      >>> req = requests.Request('GET', 'https://httpbin.org/get')
      >>> req.prepare()
      <PreparedRequest [GET]>
    """
    def __init__(self, method: Optional[Any] = ..., url: Optional[Any] = ..., headers: Optional[Any] = ..., files: Optional[Any] = ..., data: Optional[Any] = ..., params: Optional[Any] = ..., auth: Optional[Any] = ..., cookies: Optional[Any] = ..., hooks: Optional[Any] = ..., json: Optional[Any] = ...):
        self.hooks = ...
        self.method = ...
        self.url = ...
        self.headers = ...
        self.files = ...
        self.data = ...
        self.json = ...
        self.params = ...
        self.auth = ...
        self.cookies = ...
    
    def __repr__(self):
        ...
    
    def prepare(self):
        """Constructs a :class:`PreparedRequest <PreparedRequest>` for transmission and returns it."""
        ...
    


class PreparedRequest(RequestEncodingMixin, RequestHooksMixin):
    """The fully mutable :class:`PreparedRequest <PreparedRequest>` object,
    containing the exact bytes that will be sent to the server.

    Generated from either a :class:`Request <Request>` object or manually.

    Usage::

      >>> import requests
      >>> req = requests.Request('GET', 'https://httpbin.org/get')
      >>> r = req.prepare()
      <PreparedRequest [GET]>

      >>> s = requests.Session()
      >>> s.send(r)
      <Response [200]>
    """
    def __init__(self):
        self.method = ...
        self.url = ...
        self.headers = ...
        self.body = ...
        self.hooks = ...
    
    def prepare(self, method: Optional[Any] = ..., url: Optional[Any] = ..., headers: Optional[Any] = ..., files: Optional[Any] = ..., data: Optional[Any] = ..., params: Optional[Any] = ..., auth: Optional[Any] = ..., cookies: Optional[Any] = ..., hooks: Optional[Any] = ..., json: Optional[Any] = ...):
        """Prepares the entire request with the given parameters."""
        ...
    
    def __repr__(self):
        ...
    
    def copy(self):
        ...
    
    def prepare_method(self, method):
        """Prepares the given HTTP method."""
        self.method = ...
    
    @staticmethod
    def _get_idna_encoded_host(host):
        ...
    
    def prepare_url(self, url, params):
        """Prepares the given HTTP URL."""
        self.url = ...
    
    def prepare_headers(self, headers):
        """Prepares the given HTTP headers."""
        self.headers = ...
    
    def prepare_body(self, data, files, json: Optional[Any] = ...):
        """Prepares the given HTTP body data."""
        self.body = ...
    
    def prepare_content_length(self, body):
        """Prepare Content-Length header based on request method and body"""
        ...
    
    def prepare_auth(self, auth, url=...):
        """Prepares the given HTTP auth data."""
        ...
    
    def prepare_cookies(self, cookies):
        """Prepares the given HTTP cookie data.

        This function eventually generates a ``Cookie`` header from the
        given cookies using cookielib. Due to cookielib's design, the header
        will not be regenerated if it already exists, meaning this function
        can only be called once for the life of the
        :class:`PreparedRequest <PreparedRequest>` object. Any subsequent calls
        to ``prepare_cookies`` will have no actual effect, unless the "Cookie"
        header is removed beforehand.
        """
        ...
    
    def prepare_hooks(self, hooks):
        """Prepares the given hooks."""
        ...
    


class Response(object):
    """The :class:`Response <Response>` object, which contains a
    server's response to an HTTP request.
    """
    __attrs__ = ...
    def __init__(self):
        self.status_code = ...
        self.headers = ...
        self.raw = ...
        self.url = ...
        self.encoding = ...
        self.history = ...
        self.reason = ...
        self.cookies = ...
        self.elapsed = ...
        self.request = ...
    
    def __enter__(self):
        ...
    
    def __exit__(self, *args):
        ...
    
    def __getstate__(self):
        ...
    
    def __setstate__(self, state):
        ...
    
    def __repr__(self):
        ...
    
    def __bool__(self):
        """Returns True if :attr:`status_code` is less than 400.

        This attribute checks if the status code of the response is between
        400 and 600 to see if there was a client error or a server error. If
        the status code, is between 200 and 400, this will return True. This
        is **not** a check to see if the response code is ``200 OK``.
        """
        ...
    
    def __nonzero__(self):
        """Returns True if :attr:`status_code` is less than 400.

        This attribute checks if the status code of the response is between
        400 and 600 to see if there was a client error or a server error. If
        the status code, is between 200 and 400, this will return True. This
        is **not** a check to see if the response code is ``200 OK``.
        """
        ...
    
    def __iter__(self):
        """Allows you to use a response as an iterator."""
        ...
    
    @property
    def ok(self):
        """Returns True if :attr:`status_code` is less than 400, False if not.

        This attribute checks if the status code of the response is between
        400 and 600 to see if there was a client error or a server error. If
        the status code is between 200 and 400, this will return True. This
        is **not** a check to see if the response code is ``200 OK``.
        """
        ...
    
    @property
    def is_redirect(self):
        """True if this Response is a well-formed HTTP redirect that could have
        been processed automatically (by :meth:`Session.resolve_redirects`).
        """
        ...
    
    @property
    def is_permanent_redirect(self):
        """True if this Response one of the permanent versions of redirect."""
        ...
    
    @property
    def next(self):
        """Returns a PreparedRequest for the next request in a redirect chain, if there is one."""
        ...
    
    @property
    def apparent_encoding(self):
        """The apparent encoding, provided by the chardet library."""
        ...
    
    def iter_content(self, chunk_size=..., decode_unicode: bool = ...):
        """Iterates over the response data.  When stream=True is set on the
        request, this avoids reading the content at once into memory for
        large responses.  The chunk size is the number of bytes it should
        read into memory.  This is not necessarily the length of each item
        returned as decoding can take place.

        chunk_size must be of type int or None. A value of None will
        function differently depending on the value of `stream`.
        stream=True will read data as it arrives in whatever size the
        chunks are received. If stream=False, data is returned as
        a single chunk.

        If decode_unicode is True, content will be decoded using the best
        available encoding based on the response.
        """
        ...
    
    def iter_lines(self, chunk_size=..., decode_unicode: bool = ..., delimiter: Optional[Any] = ...):
        """Iterates over the response data, one line at a time.  When
        stream=True is set on the request, this avoids reading the
        content at once into memory for large responses.

        .. note:: This method is not reentrant safe.
        """
        ...
    
    @property
    def content(self):
        """Content of the response, in bytes."""
        ...
    
    @property
    def text(self):
        """Content of the response, in unicode.

        If Response.encoding is None, encoding will be guessed using
        ``chardet``.

        The encoding of the response content is determined based solely on HTTP
        headers, following RFC 2616 to the letter. If you can take advantage of
        non-HTTP knowledge to make a better guess at the encoding, you should
        set ``r.encoding`` appropriately before accessing this property.
        """
        ...
    
    def json(self, **kwargs):
        r"""Returns the json-encoded content of a response, if any.

        :param \*\*kwargs: Optional arguments that ``json.loads`` takes.
        :raises ValueError: If the response body does not contain valid json.
        """
        ...
    
    @property
    def links(self):
        """Returns the parsed header links of the response, if any."""
        ...
    
    def raise_for_status(self):
        """Raises stored :class:`HTTPError`, if one occurred."""
        ...
    
    def close(self):
        """Releases the connection back to the pool. Once this method has been
        called the underlying ``raw`` object must not be accessed again.

        *Note: Should not normally need to be called explicitly.*
        """
        ...
    


