# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name, greeting="Hello, <name>!"):
    ans = greeting.replace("<name>", name)
    return ans

def force(mass, body="earth"):
    body.lower()
    bodies = {'sun'     : 274,
              'jupiter' : 24.9,
              'neptune' : 11.2,
              'saturn'  : 10.4,
              'earth'   : 9.8,
              'uranus'  : 8.9,
              'venus'   : 8.9,
              'mars'    : 3.7,
              'mercury' : 3.7,
              'moon'    : 1.6,
              'pluto'   : 0.6}

    return mass*bodies[body]

def pull(m1, m2, d):
    G = 6.674*(10**-11)
    return G * ((m1*m2)/(d**2))