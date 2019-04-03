import bpy
import csv 
import random

#Global variables:
# Must have a file names 'trialInfo' in with 7 columms representing the
#following parameters for each trial:
trialNumber = [] # each trial in trialInfo should be labeled from 1 to n
left_right = [] # Describes whether the correct choice is on left or right
trialType = [] # Describes the trial type
green_Left = [] #Number of green on left
purple_Left = []#Number of purple on left
green_Right = []#number of green on right
purple_Right = []#number of purple on right
#set this for minimum distance between balls
checkDistance = 1.2
#set size of balls
smallScale = [0.6,0.6,0.6]
bigScale = [0.6,0.6,0.6]
#set bin limits
#left side
z = 2.3
bin1_yTop = 6
bin1_yBottom = -6
bin1_xLeft = -11
bin1_xRight =-2
#right side
bin2_yTop = 6
bin2_yBottom = -6
bin2_xLeft = 1.9
bin2_xRight = 11.75

#define materials
def makeMaterial(name, diffuse, specular, alpha):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = diffuse
    mat.diffuse_shader = 'LAMBERT' 
    mat.diffuse_intensity = 1.0 
    mat.specular_color = specular
    mat.specular_shader = 'COOKTORR'
    mat.specular_intensity = 0.5
    mat.alpha = alpha
    mat.ambient = 1
    return mat

def setMaterial(ob, mat):
    me = ob.data
    me.materials.append(mat)
 
def readMyFile(filename):
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            trialNumber.append(row[0])
            left_right.append(row[1])
            trialType.append(row[2])
            green_Left.append(row[3])
            purple_Left.append(row[4])
            green_Right.append(row[5])
            purple_Right.append(row[6])
    
grey = makeMaterial('grey', (0.35,0.35,0.35), (1,1,1), 1)
green = makeMaterial('green', (0, 2.5, 0), (1,1,1), 1)
purple = makeMaterial('purple', (2.5, 0, 2.5), (1,1,1), 1)

## Read in trial specifications 
readMyFile('/Users/shaunogrady/Desktop/Blender_animations/LPGP/NewColors/trialInfo.csv') 

# for loop to iterate through all of the trial variables and render each image:
#for trial in range(0,len(trialNumber))
for trial in range(48,(len(trialNumber))):
    #Erase all old marbles:
    #tracks the total number of red and white for bin 1 (this will change with each image)
    #subtract 1 from green marble counts
    bin1_green = green_Left[trial]
    bin1_purple = purple_Left[trial]
    #tracks the total number of red and white for bin 2 (this will change with each image)
    bin2_green = green_Right[trial]
    bin2_purple = purple_Right[trial]
    #get ready for distance comparison:
    xPositions = []
    yPositions = []
    sizes = []
    distance = 0
    #place first marble in the left bin
    x = random.randrange((bin1_xLeft*100),(bin1_xRight*100))/100
    y = random.randrange((bin1_yBottom * 100),(bin1_yTop * 100))/100
    z = 1
    xPositions.append(x)
    yPositions.append(y)
    sizes.append('S')
    bpy.ops.mesh.primitive_uv_sphere_add(location =(x,y,z))
    bpy.context.object.scale = (smallScale)
    bpy.ops.object.modifier_add(type='SUBSURF')
    setMaterial(bpy.context.object, green)
    bpy.ops.object.shade_smooth()
    ### the following code adds additional marbles
    #variable for iterating within the upcoming for loop
    for numRed in range(0, (int(bin1_green)-1)):
        #place second marble
        x = random.randrange((bin1_xLeft*100),(bin1_xRight*100))/100
        y = random.randrange((bin1_yBottom * 100),(bin1_yTop * 100))/100
        z = 1
        size = 'S'
        marble = 0
        while marble < len(xPositions):
            distance = sqrt((abs(x - xPositions[marble]) * abs(x - xPositions[marble])) + (abs(y - yPositions[marble]) * abs(y - yPositions[marble])))
            #this loop ensures that the marbles do not touch or overlap.)
            while distance < checkDistance:
                x = random.randrange((bin1_xLeft*100),(bin1_xRight*100))/100
                y = random.randrange((bin1_yBottom * 100),(bin1_yTop * 100))/100
                marble = -1
                distance = 1200
            marble = marble+1  
        xPositions.append(x)
        yPositions.append(y)
        sizes.append('S')
        bpy.ops.mesh.primitive_uv_sphere_add(location =(x,y,z))
        bpy.context.object.scale = (smallScale)
        bpy.ops.object.modifier_add(type='SUBSURF')
        setMaterial(bpy.context.object, green)
        bpy.ops.object.shade_smooth()
    for numWhite in range(0, int(bin1_purple)):
        #place second marble
        x = random.randrange((bin1_xLeft*100),(bin1_xRight*100))/100
        y = random.randrange((bin1_yBottom * 100),(bin1_yTop * 100))/100
        z = 1
        size = 'B'
        marble = 0
        while marble < len(xPositions):
            distance = sqrt((abs(x - xPositions[marble]) * abs(x - xPositions[marble])) + (abs(y - yPositions[marble]) * abs(y - yPositions[marble])))
            #this loop ensures that the distance is always greater than the radius of both of the marbles (the marbles
            #do not touch or overlap.)
            while distance < checkDistance:
                x = random.randrange((bin1_xLeft*100),(bin1_xRight*100))/100
                y = random.randrange((bin1_yBottom * 100),(bin1_yTop * 100))/100
                marble = -1
                distance = 1200
            marble = marble+1  
        xPositions.append(x)
        yPositions.append(y)
        sizes.append('B')
        bpy.ops.mesh.primitive_uv_sphere_add(location =(x,y,z))
        bpy.context.object.scale = (bigScale)
        bpy.ops.object.modifier_add(type='SUBSURF')
        setMaterial(bpy.context.object, purple)
        bpy.ops.object.shade_smooth()
    ##### This marks the change to bin 2
    #place first marble in the right bin
    x = random.randrange((bin2_xLeft*100),(bin2_xRight*100))/100
    y = random.randrange((bin2_yBottom * 100),(bin2_yTop * 100))/100
    z = 1
    xPositions.append(x)
    yPositions.append(y)
    sizes.append('B')
    bpy.ops.mesh.primitive_uv_sphere_add(location =(x,y,z))
    bpy.context.object.scale = (bigScale)
    bpy.ops.object.modifier_add(type='SUBSURF')
    setMaterial(bpy.context.object, purple)
    bpy.ops.object.shade_smooth()
    ### the following code adds additional marbles
    #variable for iterating within the upcoming for loop
    for numRed in range(0, (int(bin2_green)-1)):
        #place second marble
        x = random.randrange((bin2_xLeft*100),(bin2_xRight*100))/100
        y = random.randrange((bin2_yBottom * 100),(bin2_yTop * 100))/100
        z = 1
        size = 'B'
        marble = 0
        while marble < len(xPositions):
            distance = sqrt((abs(x - xPositions[marble]) * abs(x - xPositions[marble])) + (abs(y - yPositions[marble]) * abs(y - yPositions[marble])))
            #this loop ensures that the distance is always greater than the radius of both of the marbles (the marbles
            #do not touch or overlap.)
            while distance < checkDistance:
                x = random.randrange((bin2_xLeft*100),(bin2_xRight*100))/100
                y = random.randrange((bin2_yBottom * 100),(bin2_yTop * 100))/100
                marble = -1
                distance = 1200
            marble = marble+1  
        xPositions.append(x)
        yPositions.append(y)
        sizes.append('B')
        bpy.ops.mesh.primitive_uv_sphere_add(location =(x,y,z))
        bpy.context.object.scale = (bigScale)
        bpy.ops.object.modifier_add(type='SUBSURF')
        setMaterial(bpy.context.object, green)
        bpy.ops.object.shade_smooth()  
    for numWhite in range(0, int(bin2_purple)):
        #place second marble
        x = random.randrange((bin2_xLeft*100),(bin2_xRight*100))/100
        y = random.randrange((bin2_yBottom * 100),(bin2_yTop * 100))/100
        z = 1
        size = 'S'
        marble = 0
        while marble < len(xPositions):
            distance = sqrt((abs(x - xPositions[marble]) * abs(x - xPositions[marble])) + (abs(y - yPositions[marble]) * abs(y - yPositions[marble])))
            #this loop ensures that the distance is always greater than the radius of both of the marbles (the marbles
            #do not touch or overlap.)
            while distance < checkDistance:
                x = random.randrange((bin2_xLeft*100),(bin2_xRight*100))/100
                y = random.randrange((bin2_yBottom * 100),(bin2_yTop * 100))/100
                marble = -1
                distance = 1200
            marble = marble+1  
        xPositions.append(x)
        yPositions.append(y)
        sizes.append('S')
        bpy.ops.mesh.primitive_uv_sphere_add(location =(x,y,z))
        bpy.context.object.scale = (smallScale)
        bpy.ops.object.modifier_add(type='SUBSURF')
        setMaterial(bpy.context.object, purple)
        bpy.ops.object.shade_smooth()
    fileName= 'Purple_'+trialType[trial]+'_' +green_Left[trial] +'_'+purple_Left[trial] +'_' +green_Right[trial] +'_'+purple_Right[trial]+'_'+left_right[trial]+'.jpg'
    scene = bpy.context.scene 
    scene.render.filepath = 'Users/shaunogrady/Desktop/Blender_animations/LPGP/NewColors/AutomatedBuilds/' + fileName  
    fp = scene.render.filepath # get existing output path
    scene.frame_set(0)
    scene.render.image_settings.file_format = 'JPEG' # set output format to .png
    bpy.ops.render.render(write_still=True) 
    scene = bpy.context.scene
    for ob in scene.objects:
        if ob.type == 'MESH' and ob.name.startswith("Sphere"):
            ob.select = True
        else: 
            ob.select = False
    bpy.ops.object.delete()
