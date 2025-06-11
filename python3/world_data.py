# Game world data and constants for ashtree.py

# Constants
DESC = 'desc'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
UP = 'up'
DOWN = 'down'
NORTHDESC = 'northdesc'
SOUTHDESC = 'southdesc'
EASTDESC = 'eastdesc'
WESTDESC = 'westdesc'
UPDESC = 'updesc'
DOWNDESC = 'downdesc'
GROUND = 'ground'
SHOP = 'shop'
GROUNDDESC = 'grounddesc'
SHORTDESC = 'shortdesc'
LONGDESC = 'longdesc'
TAKEABLE = 'takeable'
EDIBLE = 'edible'
OPENABLE = 'openable'
DESCWORDS = 'descwords'

# World positions dictionary
worldPositions = {
    # Room 1
    '100': {
        DESC: 'Ash colored walls block your way on the West and North side.',
        EAST: ('110', 'You make out a still shape in the darkness'),
        SOUTH: ('101', 'The darkness stares back at you'),
        GROUND: []},
    '110': {
        DESC: 'The exit comes into focus. You wonder if more horrors lay ahead.',
        NORTH: ('224', 'Exit'),
        EAST: ('120', 'The darkness stares back at you'),
        SOUTH: ('111', 'The darkness stares back at you'),
        WEST: ('100', 'The darkness stares back at you'),
        GROUND: ['Wooden Door']},
    '120': {
        DESC: 'Ash colored walls block your way on the North and East side.',
        SOUTH: ('121', 'The darkness stares back at you'),
        WEST: ('110', 'You make out a still shape in the darkness'),
        GROUND: []},
    '101': {
        DESC: 'An Ash colored walls blocks your way on the West side',
        NORTH: ('100', 'The darkness stares back at you'),
        EAST: ('111', 'The darkness stares back at you'),
        SOUTH: ('102', 'The darkness stares back at you'),
        GROUND: []},
    '111': {
        DESC: 'Cold silence surrounds you.',
        NORTH: ('110', 'You make out a still shape in the darkness'),
        EAST: ('121', 'The darkness stares back at you'),
        SOUTH: ('112', 'The darkness stares back at you'),
        WEST: ('101', 'The darkness stares back at you'),
        GROUND: []},
    '121': {
        DESC: 'An Ash colored wall blocks your way on the East side.',
        NORTH: ('120', 'The darkness stares back at you'),
        SOUTH: ('122', 'The darkness stares back at you'),
        WEST: ('111', 'The darkness stares back at you'),
        GROUND: []},
    '102': {
        DESC: 'Ash colored walls block your way on the South and West side.',
        NORTH: ('101', 'The darkness stares back at you'),
        EAST: ('112', 'The darkness stares back at you'),
        GROUND: []},
    '112': {
        DESC: "There's nothing to do but venture into the darkness.",
        NORTH: ('111', 'The darkness stares back at you'),
        EAST: ('122', 'The darkness stares back at you'),
        WEST: ('102', 'The darkness stares back at you'),
        GROUND: []},
    '122': {
        DESC: 'Ash colored walls block your way on the South and East side.',
        NORTH: ('121', 'The darkness stares back at you'),
        WEST: ('112', 'The darkness stares back at you'),
        GROUND: []},
    # Room 2
    '200': {
        DESC: 'Ash colored walls block your way on the North and West side.',
        EAST: ('210', 'The darkness stares back at you.'),
        SOUTH: ('201', 'The darkness stares back at you.'),
        GROUND: []},
    '210': {
        DESC: 'An Ash colored wall blocks your way on the North side.',
        EAST: ('220', 'You make out a still shape in the darkness'),
        SOUTH: ('211', 'The darkness stares back at you.'),
        WEST: ('200', 'The darkness stares back at you.'),
        GROUND: []},
    '220': {
        DESC: 'The exit comes into focus. You wonder if more horrors lay ahead.',
        NORTH: ('323', 'Exit'),
        EAST: ('230', 'The darkness stares back at you.'),
        SOUTH: ('221', 'The darkness stares back at you.'),
        WEST: ('210', 'The darkness stares back at you.'),
        GROUND: []},
    '230': {
        DESC: 'An Ash colored wall blocks your way on the North side.',
        EAST: ('240', 'The darkness stares back at you.'),
        SOUTH: ('231', 'The darkness stares back at you.'),
        WEST: ('220', 'You make out a still shape in the darkness'),
        GROUND: []},
    '240': {
        DESC: 'Ash colored walls block your way on the North and East side.',
        SOUTH: ('241', 'The darkness stares back at you.'),
        WEST: ('230', 'The darkness stares back at you.'),
        GROUND: []},
    '201': {
        DESC: 'An Ash colored wall blocks your way on the West side.',
        NORTH: ('200', 'The darkness stares back at you.'),
        EAST: ('211', 'The darkness stares back at you.'),
        SOUTH: ('202', 'The darkness stares back at you.'),
        GROUND: []},
    '211': {
        DESC: 'Cold silence surrounds you.',
        NORTH: ('210', 'The darkness stares back at you.'),
        EAST: ('221', 'The darkness stares back at you.'),
        SOUTH: ('212','The darkness stares back at you.'),
        WEST: ('201', 'The darkness stares back at you.'),
        GROUND: []},
    '221': {
        DESC: 'Cold silence surrounds you.',
        NORTH: ('220', 'You make out a still shape in the darkness'),
        EAST: ('231', 'The darkness stares back at you.'),
        SOUTH: ('222', 'The darkness stares back at you.'),
        WEST: ('211', 'The darkness stares back at you.'),
        GROUND: []},
    '231': {
        DESC: 'Cold silence surrounds you.',
        NORTH: ('223', 'The darkness stares back at you.'),
        EAST: ('241', 'The darkness stares back at you.'),
        SOUTH: ('232','The darkness stares back at you.'),
        WEST: ('221', 'The darkness stares back at you.'),
        GROUND: []},
    '241': {
        DESC: 'An Ash colored wall blocks your way on the East side.',
        NORTH: ('240', 'The darkness stares back at you.'),
        SOUTH: ('242', 'The darkness stares back at you.'),
        WEST: ('231', 'The darkness stares back at you.'),
        GROUND: []},
    '202': {
        DESC: 'An Ash colored wall blocks your way on the West side.',
        NORTH: ('201', 'The darkness stares back at you.'),
        EAST: ('212', 'The darkness stares back at you.'),
        SOUTH: ('203', 'The darkness stares back at you.'),
        GROUND: []},
    '212': {
        DESC: 'Cold silence surrounds you.',
        NORTH: ('212', 'The darkness stares back at you.'),
        EAST: ('222', 'The darkness stares back at you.'),
        SOUTH: ('213', 'The darkness stares back at you.'),
        WEST: ('202', 'The darkness stares back at you.'),
        GROUND: []},
    '222': {
        DESC: 'Cold silence surrounds you.',
        NORTH: ('221', 'The darkness stares back at you.'),
        EAST: ('232', 'The darkness stares back at you.'),
        SOUTH: ('223', 'The darkness stares back at you.'),
        WEST: ('212', 'The darkness stares back at you.'),
        GROUND: []},
    '232': {
        DESC: 'Cold silence surrounds you.',
        NORTH: ('231', 'The darkness stares back at you.'),
        EAST: ('242', 'The darkness stares back at you.'),
        SOUTH: ('232','The darkness stares back at you.'),
        WEST: ('222', 'The darkness stares back at you.'),
        GROUND: []},
    '242': {
        DESC: 'An Ash colored wall blocks your way on the East side.',
        NORTH: ('241', 'The darkness stares back at you.'),
        SOUTH: ('243', 'The darkness stares back at you.'),
        WEST: ('232', 'The darkness stares back at you.'),
        GROUND: []},
    '203': {
        DESC: 'An Ash colored wall blocks your way on the West side.',
        NORTH: ('202', 'The darkness stares back at you.'),
        EAST: ('213', 'The darkness stares back at you.'),
        SOUTH: ('204','The darkness stares back at you.'),
        GROUND: []},
    '213': {
        DESC: 'Cold silence surrounds you.',
        NORTH: ('212', 'The darkness stares back at you.'),
        EAST: ('223', 'The darkness stares back at you.'),
        SOUTH: ('214', 'The darkness stares back at you.'),
        WEST: ('203', 'The darkness stares back at you.'),
        GROUND: []},
    '223': {
        DESC: 'Cold silence surrounds you.',
        NORTH: ('222', 'The darkness stares back at you.'),
        EAST: ('233', 'The darkness stares back at you.'),
        SOUTH: ('224','The darkness stares back at you.'),
        WEST: ('213', 'The darkness stares back at you.'),
        GROUND: []},
    '233': {
        DESC: 'Cold silence surrounds you.',
        NORTH: ('232', 'The darkness stares back at you.'),
        EAST: ('243', 'The darkness stares back at you.'),
        SOUTH: ('234', 'The darkness stares back at you.'),
        WEST: ('223', 'The darkness stares back at you.'),
        GROUND: []},
    '243': {
        DESC: 'An Ash colored wall blocks your way on the East side.',
        NORTH: ('242', 'The darkness stares back at you.'),
        WEST: ('233', 'The darkness stares back at you.'),
        SOUTH: ('244', 'The darkness stares back at you.'),
        GROUND: []},
    '204': {
        DESC: 'Ash colored walls block your way on the South and West side.',
        NORTH: ('203', 'The darkness stares back at you.'),
        EAST: ('214', 'The darkness stares back at you.'),
        GROUND: []},
    '214': {
        DESC: 'An Ash colored wall blocks your way on the South side.',
        NORTH: ('213', 'The darkness stares back at you.'),
        EAST: ('224', 'The darkness stares back at you.'),
        WEST: ('204', 'The darkness stares back at you.'),
        GROUND: []},
    '224': {
        DESC: 'You walk through the door to find yourself in a room that feels exactly the same as the previous. However, the sound of your footsteps seem to take longer to reflect off of the walls',
        NORTH: ('223', 'The darkness stares back at you.'),
        EAST: ('234', 'The darkness stares back at you.'),
        WEST: ('214', 'The darkness stares back at you.'),
        GROUND: ['Apple']},
    '234': {
        DESC: 'An Ash colored wall blocks your way on the South side.',
        NORTH: ('233', 'The darkness stares back at you.'),
        EAST: ('244', 'The darkness stares back at you.'),
        WEST: ('224', 'The darkness stares back at you.'),
        GROUND: []},
    '244': {
        DESC: 'Ash colored walls block your way on the South and East side.',
        NORTH: ('243', 'The darkness stares back at you.'),
        WEST: ('234', 'The darkness stares back at you.'),
        GROUND: []},
}

# World items dictionary
worldItems = {
    'Wooden Door': {
        GROUNDDESC: 'A deteriorated wooden door looks back at you from the north wall.',
        SHORTDESC: 'a wooden door',
        LONGDESC: 'The hinges on the door are rusted and barely keeping the door on the wall. You breathe in deeply and wonder how such a dry environment could cause this.',
        TAKEABLE: False,
        OPENABLE: True,
        DESCWORDS: ['door', 'wooden door', 'deteriorated wooden door']},
    'Apple': {
        GROUNDDESC: 'An apple sits on the floor.',
        SHORTDESC: 'an apple.',
        LONGDESC: 'You notice the apple already has a bit taken out of it, The apple flesh has turned slightly brown.',
        EDIBLE: True,
        DESCWORDS: ['apple']},
    'Note #1': {
        GROUNDDESC: 'A piece of paper lays on the ground',
        SHORTDESC: 'a piece of paper',
        LONGDESC: "You bring the note close to your face and begin to read.. \n\n I don't know for sure if anyone will ever find this. I don't even know where I am. I just had to write something down before I went crazy from the dark silence. My sweet Lucy, why didn't you listen to me? Why  did you go through the door?",
        DESCWORDS: ['note', 'paper', 'piece of paper']}
}
