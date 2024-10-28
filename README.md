# CLI utility to access database of planetary systems
The database is based on 2 tables: **planetary_systems** and **planets**. They have the following structure:
- planetary_systems
```
id |     name
```
- planets
```
name     | planetary_system_id | equatorial_diameter |  mass   | semi_major_axis | orbital_period | inclination_to_suns_equator | orbital_eccentricity | rotation_period | confirmed_moons | axial_tilt | rings | atmosphere
```

Available commands:
- ps-cli: command to interact with planetary systems
- planets-cli: command to interact with planets

## Deployment
The Python modules specified in the _requirements.txt_ file need to be installed into the working environment in order to run the scripts. This requires to previously install the dependencies for **psycopg2**. This depends on the Linux flavor the project will be deployed on. For example:
- For **Ubuntu/Debian**:
```
sudo apt-get update
sudo apt-get install libpq-dev python3-dev build-essential
```
- For **CentOS/RHEL**:
```
sudo yum install postgresql-devel python3-devel gcc
```

A Postgres database instance is required to store and manage the data. The project has a _docker-compose.yml_ file to create an instance of a Postgres database in Docker. Here is the command to deploy it: 
```
docker-compose build && docker-compose up -d
```

An _.env_ file needs to be created in the main directory of the project to access the database. It requires the following parameters:
```
DATABASE_HOSTNAME=
DATABASE_PORT=
DATABASE_NAME=
DATABASE_USERNAME=
DATABASE_PASSWORD=
```

## Usage
The command should be called pointing to the python script:
```
python app\ps-cli.py
python app\planets-cli.py
```

Further information on how to use the commands can be checked using the _-h_ flag. For example:
```
>python app\planets-cli.py -h
usage: planets-cli [-h] {get,add,addCSV,update,delete} ...

options:
  -h, --help            show this help message and exit

Available options:
  {get,add,addCSV,update,delete}
                        Available planet methods to interact with database
    get                 get planet from database
    add                 add planet to database. Values must be added separated by a space additionally with the planetary_system_id at the end
    addCSV              add planets from CSV file
    update              update planet's value in database
    delete              delete planet from database
```

The same flag can also be used for each one of the arguments of the commands. For example:
```
>python app\planets-cli.py update -h
usage: planets-cli update [-h] planet_name parameter value

positional arguments:
  planet_name
  parameter
  value


options:
  -h, --help   show this help message and exit
```

A test.py file is present in the project to test if the commands are working as expected after setting up the environment. Here is the command to execute it:
```
python -m pytest app\test.py -vv
```
