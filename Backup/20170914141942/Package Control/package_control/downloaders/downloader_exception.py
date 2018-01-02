import sys


class DownloaderException(Exception):

    """If a downloader could not download a URL"""

    def __unicode__(self):
        return self.args[0]

    def __str__(self):
        if sys.version_info < (3,):
            return self.__bytes__()
        return self.__unicode__()

    def __bytes__(self):
        return self.__unicode__().encode('utf-8')
