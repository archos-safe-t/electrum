from safetlib.client import proto, BaseClient, ProtocolMixin
from .clientbase import SafeTClientBase

class SafeTClient(SafeTClientBase, ProtocolMixin, BaseClient):
    def __init__(self, transport, handler, plugin):
        BaseClient.__init__(self, transport)
        ProtocolMixin.__init__(self, transport)
        SafeTClientBase.__init__(self, handler, plugin, proto)


SafeTClientBase.wrap_methods(SafeTClient)
