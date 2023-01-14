import logging

formatString = "%(asctime)s in %(name)s > %(message)s"
fo = logging.Formatter(formatString)
sh = logging.StreamHandler()
sh.setFormatter(fo)
l = logging.getLogger(__name__)
l.setLevel(logging.DEBUG)
l.addHandler(sh)

