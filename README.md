# BirdWatch
BirdWatch uses a list of aircraft associated with Northern California law enforcement agencies to warn drivers when potential aircraft speed traps may exist on local freeways and roads. 

### Goals
The goal of this project is not to make it easier to hide from law enforcement agencies or make it easier to commit crime, but rather to extend the functionality of speed trap warnings that are now common in applications such as Apple Maps, Google Maps, and Waze. Currently, drivers have the ability to report ground-based speed traps in these applications to other drivers who will then receive warnings to slow down in a particular area. As the goal of most speed traps are to encourage drivers to drive more safely through the threat of enforcement, it only makes sense to include warnings in areas where law enforcement aircraft have been identified. 

### How it Works
A list of registration numbers associated with Northern California law enforcement aircraft was created using publicly available data provided by the California Highway Patrol, as well as monitoring flight tracking websites such as FlightRadar24. Modern day aircraft utilize a technology called ADS-B (Automatic Dependent Surveillance–Broadcast) to broadcast their current location, and other pertinent information such as their registration numbers to other aircraft and air traffic control. Across the entire world, hobbyists and professionals maintain a network of receivers that monitor these ADS-B signals in order to deliver them to websites such as FlightRadar24, ADSBexchange, and Airplanes.live, the latter of which offers an API for hobbyists to "create something exciting". 

Utilizing the list of aircraft registration numbers, we are able to determine whether or not specific aircraft are airborne as well as their current location using the airplanes.live API. We can then use the reverse_geocoder library to determine the closest City, County, and State that these aircraft may be near to mimic the warning that many map applications provide. 

### Requirements
Python with Pandas and reverse_geocoder library. Additionally, if you would like to add airplane registration numbers of your own, you will need a spreadsheet editor such as Excel, Google Sheets, or Numbers to edit the Registrations.csv file.

### How to Use
Download the files titled “Plane Reg Csv.py” and “Registrations.csv”. Ensure both of these files are in the same folder as one another before running the script in “Plane Reg Csv.py”. Running the script will print the contents of the .csv file, and then check each registration number one by one with results indicating the location of the aircraft, or a message stating “Not Airborne” for aircraft that are not currently in the air. 

### Future Goals
- Mobile application and desktop GUI application
- Ability to determine relative distance between the user and the aircraft
