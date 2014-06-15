
# Declare the path to the database
dbPath = "mongodb://localhost:27017/"
dbname = "clinq"

# Set the data dir
datadir = "/home/alex/fusessh"

# Set Indexing dir
IndexDir = "/tmp/clinq"


modules = [
	"indexing",
	"backend_mongo",

	"handler_mp3",

	"web-core"
]