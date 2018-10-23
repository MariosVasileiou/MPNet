"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

import lcmtypes.region_3d_t

class environment_t(object):
    __slots__ = ["operating", "goal", "num_obstacles", "obstacles"]

    def __init__(self):
        self.operating = lcmtypes.region_3d_t()
        self.goal = lcmtypes.region_3d_t()
        self.num_obstacles = 0
        self.obstacles = []

    def encode(self):
        buf = BytesIO()
        buf.write(environment_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        assert self.operating._get_packed_fingerprint() == lcmtypes.region_3d_t._get_packed_fingerprint()
        self.operating._encode_one(buf)
        assert self.goal._get_packed_fingerprint() == lcmtypes.region_3d_t._get_packed_fingerprint()
        self.goal._encode_one(buf)
        buf.write(struct.pack(">i", self.num_obstacles))
        for i0 in range(self.num_obstacles):
            assert self.obstacles[i0]._get_packed_fingerprint() == lcmtypes.region_3d_t._get_packed_fingerprint()
            self.obstacles[i0]._encode_one(buf)

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != environment_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return environment_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = environment_t()
        self.operating = lcmtypes.region_3d_t._decode_one(buf)
        self.goal = lcmtypes.region_3d_t._decode_one(buf)
        self.num_obstacles = struct.unpack(">i", buf.read(4))[0]
        self.obstacles = []
        for i0 in range(self.num_obstacles):
            self.obstacles.append(lcmtypes.region_3d_t._decode_one(buf))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if environment_t in parents: return 0
        newparents = parents + [environment_t]
        tmphash = (0x8caabc2a2ba0f9c7+ lcmtypes.region_3d_t._get_hash_recursive(newparents)+ lcmtypes.region_3d_t._get_hash_recursive(newparents)+ lcmtypes.region_3d_t._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if environment_t._packed_fingerprint is None:
            environment_t._packed_fingerprint = struct.pack(">Q", environment_t._get_hash_recursive([]))
        return environment_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
