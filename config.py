
# Declare the path to the database
dbPath = "mongodb://localhost:27017/"
dbname = "clinq"

# Set the data dir, where clinq will search for media
datadir = "/home/alex/fusessh"


tmpDir = "/tmp/clinq"


modules = [
	"indexing",
	"backend_mongo",

	"handler_mp3",

	"web-core", "web-main", "web-modinfo"
]