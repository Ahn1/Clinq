import logging
import hashlib


def GetPathHash(app,path):
	if path.startswith(app.config.datadir):
		path = path[len(app.config.datadir):]

	pathHash = hashlib.md5(path).hexdigest()

	logging.debug("Generating hash from '%s': '%s'", path, pathHash)

	return pathHash