from vpython import *
#Web VPython 3.2
# A simulation of orbital motion in the solar system. Included are Sun, Venus, Earth, Moon, Mars, Jupiter, Saturn, and the Voyager spacecraft.
# Voyager 1 spacecraft reached Jupiter march 5, 1979, using a gravitational assist from Jupiter continue to Saturn.
# We want to recreate this event in the simulation. 


# Note that exponents are indicated by a double asterisk (**). Using a caret 
# symbol (^) will cause the program to behave unpredictably.

# Some VPython functions that might be helpful are:
# "norm(a)" or "hat(a)"  is a unit vector with the same direction as the vector "a"
# "mag(a)"   is a scalar that is the magnitude of the vector "a"

# All constants and initial quantities in standard metric units (Kilogram, meter, second)

G = 6.67384e-11             # universal gravitational constant
AU = 1.496e11               # Astronomical unit (avg. dist from Sun to Earth--for length scale purposes)
msun = 1.989e30             # mass of Sol (sun)
mearth = 5.97219e24         # mass of Earth
mmars = 6.4185e23           # mass of Mars
mvoyager = 815              # mass of Voyager spacecraft
mvenus = 4.8685E+24         # mass of Venus
mjupiter = 1.8982E+27       # mass of Jupiter
msaturn = 5.6834E+26        # mass of Saturn
mluna = 7.349E+22           # mass of Luna (Earth's moon)

# time step, the resolution of the model. Sensitive parameter that affects speed and accuracy of simulation 
dt = 60
#Initial vectors from NASA Horizons ephemeris data, Sept 6 1977 13:00. Simulation begins 1 day after Voyager launch.
#Initial position and velocity vectors, Earth, Mars, Venus, Jupiter, Saturn, voyager, Moon

riearth = vector(1.453772460850194E+11,-4.188128638126862E+10,-1.049844311424159E+07)                   
viearth = vector(7.685373623370066E+03,2.854217926154849E+04,1.441747784824088E+00)                     

rimars = vector(1.311259442841889E+11,1.782717788104251E+11,5.164557769179419E+08)                      
vimars = vector(-1.862193631368309E+04,1.635542359189090E+04,8.010713347487091E+02)                     

rivenus = vector(1.745148750269540E+10,1.057139445350288E+11,4.506034456248209E+08)                     
vivenus = vector(-3.468345075326985E+04,5.380727415589974E+03,2.076250549599925E+03)                    

rijupiter = vector(1.044507860746725E+11,7.548163902854463E+11,-5.448224996495664E+09)              
vijupiter = vector(-1.309471243625975E+04,2.393712938947750E+03,2.834368342603271E+02)                  

risaturn = vector(-1.076107914948705E+12,8.528108281220677E+11,2.784667371219224E+10)                   
visaturn = vector(-6.519480517094538E+03,-7.595970096499721E+03,3.922772920332944E+02)                  

rivoyager = vector(1.456911900862323E+11,-4.107332890637343E+10,4.986705377534777E+07)                   
vivoyager = vector(1.129755179965272E+04,3.815884387540470E+04,7.225642699714125E+02)

riluna = vector(1.454170767229446E+11,-4.148087083480877E+10,-4.459194824394584E+07)
viluna = vector(6.721493043723685E+03,2.862363163817391E+04,-3.001725289865398E+01)

risun = vector(3.558528683239765E+08,-6.578548612220812E+08,-9.597645654994354E+06)
visun = vector(1.397038759032587E+01,7.525957403809233E-02,-3.805145854507691E-01)

#set up the display window
scene = display(width=1280, height=720, userspin=True, userzoom=True)                                 

#create the objects and assign their properties
#new objects created for venus, jupiter, saturn

sun = sphere(pos=risun, radius=0.1*AU, color=color.yellow) 
sun.vel = visun

earth = sphere(pos=riearth, radius=0.03*AU, color=color.blue)                                           
earthtrail = attach_trail(earth, radius=0.2*earth.radius, trail_type="points", interval=2, retain=1000)
earth.vel = viearth

mars = sphere(pos=rimars, radius=0.03*AU, color=color.red)
marstrail = attach_trail(mars, radius=0.2*mars.radius, trail_type="points", interval=2, retain=1000)
mars.vel = vimars

voyager = sphere(pos=rivoyager, radius=0.02*AU, color=color.white)
voyagertrail = attach_trail(voyager, radius=0.2*voyager.radius, trail_type="points", interval=2, retain=10000)
voyager.vel = vivoyager

venus = sphere(pos=rivenus, radius = 0.03*AU, color=color.green)
venustrail = attach_trail(venus, radius=0.2*venus.radius, trail_type="points", interval=2, retain=1000)
venus.vel = vivenus

jupiter = sphere(pos=rijupiter, radius = 0.08*AU, color=color.orange)
jupitertrail = attach_trail(jupiter, radius=0.2*jupiter.radius, trail_type="points", interval=2, retain=10000)
jupiter.vel = vijupiter

saturn = sphere(pos=risaturn, radius = 0.08*AU, color=color.magenta)
saturntrail = attach_trail(saturn, radius=0.2*saturn.radius, trail_type="points", interval=2, retain=10000)
saturn.vel = visaturn

luna = sphere(pos=riluna, radius = 0.03*AU, color=color.white)
lunatrail = attach_trail(luna, radius=0.2*luna.radius, trail_type="points", interval=2, retain=1000)
luna.vel = viluna

# draw an arrow to show direction of initial velocity of Voyager
voyagerarrow1 = arrow(pos=voyager.pos, axis=(sun.radius*2)*norm(vivoyager), color=color.white)


#set the scene
scene.range=1.4*mag(jupiter.pos)

#create display for timing information
tstr="Time: {:.0f} days".format(0)
tlabel=label(pos=vector(0,1.2*mag(jupiter.pos),0), text=tstr)

# new display for speed information
sstr="Speed: {:.0f} m/s".format(0)
slabel=label(pos=vector(0,1.1*mag(jupiter.pos),0), text=sstr, color=color.white)

# new display for gravity assist
astr="GRAVITY ASSIST"
alabel=label(pos=vector(0,1.3*mag(jupiter.pos),0), text=astr, color=color.black)

# new display for Launch Date
launchstr="Starting Date: 19770906 13:00 UDT. (one day after Voyager launch)"   
launchlabel=label(pos=vector(0,-0.4*mag(jupiter.pos),0), text=launchstr)

a=0 # a flag variable to break the loop

t=0

while (a == 0):
    
   
    rate(1000000) # updates per second
    
    
    if 47520000 < t < 47520090 : # march 10, 1979, velocity vector modified to simulate added thrust
        #voyager.pos = vector(-4.919480022904942E+11,6.228361442269497E+11,8.722905222204804E+09) 
        voyager.vel = vector(-2.240198145889407E+04,-1.104216433938528E+04,1.119880153007128E+03)
    
    
    # earth
    # equations to model Earth's motion
    earth.gravf = (G*mearth*msun)/(mag(earth.pos)**2)*norm(earth.pos)

    # Calculate net force on the Earth
    earth.netf = -earth.gravf
    
    # calculate Earth acceleration
    earth.acc = earth.netf/mearth
    # update Earth velocity
    earth.vel = earth.vel + earth.acc*dt 
    
    # update Earth position    
    earth.pos = earth.pos + earth.vel*dt 
    
    
    # Moon
    # equations to model Moon's motion
    luna.gravf = (G*mluna*msun)/(mag(luna.pos)**2)*norm(luna.pos)
    luna.gravfe = ((G*mluna*mearth)/(mag(luna.pos-earth.pos)**2)*norm(luna.pos-earth.pos))
    
    # Calculate net force on the Moon
    luna.netf = -luna.gravf -luna.gravfe
    
    # calculate Moon acceleration
    luna.acc = luna.netf/mluna
    # update Moon velocity
    luna.vel = luna.vel + luna.acc*dt 
    
    # update Moon position    
    luna.pos = luna.pos + luna.vel*dt 
    
    
    
    
    
    # mars
    # equations to model Mars's motion
    # Calculate gravitational force on the Mars
    mars.gravf = ((G*mmars*msun)/(mag(mars.pos)**2)*norm(mars.pos))
    
    # Calculate net force on the Mars
    mars.netf = -mars.gravf 
    
    # calculate Mars acceleration
    mars.acc = mars.netf/mmars
    
    # update Mars velocity
    mars.vel = mars.vel + mars.acc*dt
    
    # update Mars position    
    mars.pos = mars.pos + mars.vel*dt   
    
    
    
    # venus
    # equations to model venus's motion
    # Calculate gravitational force on the venus
    venus.gravf = ((G*mvenus*msun)/(mag(venus.pos)**2)*norm(venus.pos))
    
    # Calculate net force on the venus
    venus.netf = -venus.gravf
    
    # calculate venus acceleration
    venus.acc = venus.netf/mvenus     
    
    # update venus velocity
    venus.vel = venus.vel + venus.acc*dt      
    
    # update venus position    
    venus.pos = venus.pos + venus.vel*dt        
    
    
    
    # jupiter
    # equations to model jupiter's motion
    # Calculate gravitational force on the jupiter
    jupiter.gravf = ((G*mjupiter*msun)/(mag(jupiter.pos)**2)*norm(jupiter.pos))
    
    # Calculate net force on the jupiter
    jupiter.netf = -jupiter.gravf    
    
    # calculate jupiter acceleration
    jupiter.acc = jupiter.netf/mjupiter    
    
    # update jupiter velocity
    jupiter.vel = jupiter.vel + jupiter.acc*dt      
    
    # update jupiter position - moved
    #jupiter.pos = jupiter.pos + jupiter.vel*dt     
    
    
    # saturn
    # equations to model saturn's motion
    # Calculate gravitational force on the saturn
    saturn.gravf = ((G*msaturn*msun)/(mag(saturn.pos)**2)*norm(saturn.pos))
    
    # Calculate net force on the saturn
    saturn.netf = -saturn.gravf
    
    # calculate saturn acceleration
    saturn.acc = saturn.netf/msaturn
    
    # update saturn velocity
    saturn.vel = saturn.vel + saturn.acc*dt
    
    # update saturn position    - moved 
    #saturn.pos = saturn.pos + saturn.vel*dt 
    
    
    # Voyager
    # equations to model Voyager's motion
    # gravitational forces on Voyager
    voyager.gravf = ((G*mvoyager*msun)/(mag(voyager.pos)**2)*norm(voyager.pos))
    voyager.gravfe = ((G*mvoyager*mearth)/(mag(voyager.pos-earth.pos)**2)*norm(voyager.pos-earth.pos))
    voyager.gravfj = ((G*mvoyager*mjupiter)/(mag(voyager.pos-jupiter.pos)**2)*norm(voyager.pos-jupiter.pos))
    voyager.gravfs = ((G*mvoyager*msaturn)/(mag(voyager.pos-saturn.pos)**2)*norm(voyager.pos-saturn.pos))
    voyager.gravfl = ((G*mvoyager*mluna)/(mag(voyager.pos-luna.pos)**2)*norm(voyager.pos-luna.pos))
    
    # net force on the voyager including sun, earth, jupiter, saturn
    voyager.netf = -voyager.gravf -voyager.gravfe -voyager.gravfj -voyager.gravfs -voyager.gravfl
    
    # update acceleration vector of the voyager
    voyager.acc = voyager.netf/mvoyager
    
    # the if block makes the gravitational assist text visible
    if mag(voyager.vel + voyager.acc*dt) > mag(voyager.vel) : 
        alabel.color=color.green
        slabel.color=color.green
    
    else :
        alabel.color=color.black
        slabel.color=color.white
        
    # update velocity vector of voyager    
    voyager.vel = voyager.vel + voyager.acc*dt
    
    # Breaks the while loop and ends the simulation if voyager is at its closest approach to saturn
    # comment out these lines to disable the saturn approach
    if mag(voyager.pos-saturn.pos) < mag((voyager.pos + voyager.vel*dt) - (saturn.pos + saturn.vel*dt)) :
        a=1
    
    # Breaks the while loop and ends the simulation if voyager is at its closest approach to Jupiter
    # comment out these lines to disable the jupiter approach
    #if mag(voyager.pos-jupiter.pos) < mag((voyager.pos + voyager.vel*dt) - (jupiter.pos + jupiter.vel*dt)) :
    #   a=1
    
    # Update position vectors of Rocket, Saturn, Jupiter
    voyager.pos = voyager.pos + voyager.vel*dt     
    saturn.pos = saturn.pos + saturn.vel*dt      
    jupiter.pos = jupiter.pos + jupiter.vel*dt  
    
    # Update time step, update date and speed displays
    t=t+dt
    
        
    tstr="Time: {:.0f} days".format(t/(24*3600))
    tlabel.text=tstr
    
    sstr="Speed: {:.0f} m/s".format(mag(voyager.vel))
    slabel.text=sstr



    # keeps the camera centered on the voyager - comment out for presentation 
    #scene.camera.follow(voyager)

# Create a display at the end of the program run to show distance to saturn at closest approach

#sastr="Closest Approach to Jupiter : {:.0f} kilometers".format((mag(voyager.pos - jupiter.pos)/1000))
#salabel=label(pos=saturn.pos, text=sastr, color=color.white)

#jupiterdistancestr="Distance from Earth to Jupiter at closest approach : {:.0f} kilometers".format((mag(jupiter.pos - earth.pos)/1000))
#jupiterdistancelabel=label(pos=vector(0,-0.1*mag(saturn.pos),0), text=jupiterdistancestr, color=color.white)

#voyagerdistancestr="Distance from Earth to Voyager at closest approach to Jupiter : {:.0f} kilometers".format((mag(voyager.pos)/1000))
#voyagerrdistancelabel=label(pos=vector(0,-0.1*mag(saturn.pos),0), text=voyagerdistancestr, color=color.white)



#sastr="Distance to Saturn at Closest Approach to Saturn : {:.0f}km".format((mag(saturn.pos)/1000))
#salabel=label(pos=saturn.pos, text=sastr, color=color.white)