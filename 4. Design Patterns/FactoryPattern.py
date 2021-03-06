import abc
class CompressionStrategy(abc.ABC):
    @abc.abstractmethod
    def compress(cls):
        pass
    @classmethod
    def createZipCompression():
        return ZipCompression()

    @classmethod
    def createRarCompression():
        return ZipCompression()

class ZipCompression(CompressionStrategy):
    def compress(cls):
        print("zip Compression")

class RarCompression(CompressionStrategy):
    def compress(cls):
        print("rar Compression")

class CompressionStrategyFactory(abc.ABC):
    @abc.abstractmethod
    def create(cls):
        pass

class ZipCompressionStrategyFactory(CompressionStrategyFactory):
    @classmethod
    def create(cls):
        return ZipCompression()

class RarCompressionStrategyFactory(CompressionStrategyFactory):
    def create(cls):
        return RarCompression()

c = ZipCompressionStrategyFactory()
c.create().compress()
r = RarCompressionStrategyFactory()
r.create().compress()