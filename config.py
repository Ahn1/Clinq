
# Declare the path to the database
dbPath = "mongodb://localhost:27017/"
dbname = "clinq"

# Set the data dir
datadir = "/home/alex/Schreibtisch/dota"

# Set Indexing dir
IndexDir = "/tmp/clinq"


modules = [
	"indexing",
	"backend_mongo",

	"handler_mp3"
]