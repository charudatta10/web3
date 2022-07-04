from cryptography.hazmat.primitives import hashes
import uuid
import logging
import os
from environs import Env

env = Env()
# Read .env into os.environ
env.read_env()

LOG_FILE = env("log_file")

logging.basicConfig(
    filename=LOG_FILE,
    filemode="a+",
    format="%(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)


class data_block:
    def __init__(self, data_trxn: str):
        self.trxn = data_trxn

    def __str__(self):
        return str(self.__dict__)


class genesys_block:
    def __init__(self):
        self.data = data_block(data_trxn="GAN0")


class meta_block:
    def __init__(self, data: data_block, prev_data: data_block):
        self.uuid = uuid.uuid1()
        self.hash = self._get_hash(data.__str__())
        self.link = self._get_hash(prev_data.__str__())

    def _get_hash(self, data: str):
        digest = hashes.Hash(hashes.SHA256())
        digest.update(data.encode("utf-8"))
        return digest.finalize()


class block:
    def __init__(self, trxn: str, prev_block):
        self.data = data_block(data_trxn=trxn)
        self.meta = meta_block(data=self.data, prev_data=prev_block.data)


if __name__ == "__main__":
    gb = genesys_block()
    # logging.debug(f"Module : block :: Class : - :: Method : __main__ :: property : genesys_block :: value : {gb.data.__str__()}")
    b0 = block(trxn="GAN1", prev_block=gb)
    print(f"ID : {b0.meta.uuid}\nHash : {b0.meta.hash}\nLink : {b0.meta.link}\n")
    b1 = block(trxn="GAN2", prev_block=b0)
    print(f"ID : {b1.meta.uuid}\nHash : {b1.meta.hash}\nLink : {b1.meta.link}\n")
    b2 = block(trxn="GAN3", prev_block=b1)
    print(f"ID : {b2.meta.uuid}\nHash : {b2.meta.hash}\nLink : {b2.meta.link}\n")
