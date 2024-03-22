#!/bin/bash

# Run database initialization commands
flask init-db
flask seed-db

# Then, execute the main container command
exec "$@"