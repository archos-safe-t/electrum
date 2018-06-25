from .plugin import SafeTCompatiblePlugin, SafeTCompatibleKeyStore


class SafeTKeyStore(SafeTCompatibleKeyStore):
    hw_type = 'safe_t'
    device = 'Safe-T mini'

class SafeTPlugin(SafeTCompatiblePlugin):
    firmware_URL = 'https://safe-t.io'
    libraries_URL = 'https://github.com/archos-safe-t/python-safet'
    minimum_firmware = (1, 0, 0)
    keystore_class = SafeTKeyStore

    def __init__(self, *args):
        try:
            from . import client
            import safetlib
            import safetlib.ckd_public
            import safetlib.transport_hid
            import safetlib.messages
            self.client_class = client.SafeTClient
            self.ckd_public = safetlib.ckd_public
            self.types = safetlib.messages
            self.DEVICE_IDS = (safetlib.transport_hid.DEV_SAFE_T_MINI_BOOTLOADER, safetlib.transport_hid.DEV_SAFE_T_MINI)
            self.libraries_available = True
        except ImportError:
            self.libraries_available = False
        SafeTCompatiblePlugin.__init__(self, *args)

    def hid_transport(self, device):
        from safetlib.transport_hid import HidTransport
        return HidTransport.find_by_path(device.path)

    def bridge_transport(self, d):
        from safetlib.transport_bridge import BridgeTransport
        return BridgeTransport(d)
