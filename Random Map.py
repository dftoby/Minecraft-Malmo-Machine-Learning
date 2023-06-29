
# coding: utf-8

# In[ ]:


from __future__ import print_function
# ------------------------------------------------------------------------------------------------
# Copyright (c) 2016 Microsoft Corporation
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ------------------------------------------------------------------------------------------------

# Tutorial sample #2: Run simple mission using raw XML

from builtins import range
import malmo.MalmoPython as MalmoPython
import os
import sys
import time
import random

def random_sphere(sphere_count_min = 1, sphere_count_max = 5, sphere_size_min = 2, sphere_size_max = 10):
    # Generates random number of spheres(default: 1-5, min: 1) in random locations and random sizes(default: 10,7,4 in each layer, min: 1)
    
    # Randomize count
    sphere_count = random.randint(sphere_count_min, sphere_count_max+1)
    
    # Sphere
    record_check = []
    sphere = ''''''
    
    for _ in range(0,sphere_count):
        # Randomize max size
        random_max_size = random.randint(sphere_size_min+4, sphere_size_max+1)
        
        # Calculate randomized margine
        random_x = random.randint(-20+random_max_size, 20-random_max_size+1)
        random_y = random.randint(1+random_max_size, 41-random_max_size)
        random_z = random.randint(-20+random_max_size, 20-random_max_size+1)
        
        # Calculate sizes for each layer
        size_max = random_max_size
        size_median = random.randint(sphere_size_min+2, random_max_size-1)
        size_min = sphere_size_min
    
        # Set up new sphere string
        new_sphere = '''<DrawSphere x="''' + str(random_x) + '''" y="''' + str(random_y) + '''" z="''' + str(random_z) + '''" radius="''' + str(size_max) + '''" type="purpur_block"/>
                    <DrawSphere x="''' + str(random_x) + '''" y="''' + str(random_y) + '''" z="''' + str(random_z) + '''" radius="''' + str(size_median) + '''" type="gold_block"/>
                    <DrawSphere x="''' + str(random_x) + '''" y="''' + str(random_y) + '''" z="''' + str(random_z) + '''" radius="''' + str(size_min) + '''" type="iron_block"/>
                    <DrawSphere x="''' + str(random_x) + '''" y="''' + str(random_y) + '''" z="''' + str(random_z) + '''" radius="1" type="diamond_block"/>'''
        
        # Sphere string appending record list
        record_check.append("x,y,z: "+str(random_x)+","+str(random_y)+","+str(random_z)+" sizes: "+str(size_max)+","+str(size_median)+","+str(size_min))
        sphere += new_sphere
    
    # Debugging purpose
    print("sphere_count:", sphere_count, '\n', "record_check:", record_check)
    return sphere

if sys.version_info[0] == 2:
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately
else:
    import functools
    print = functools.partial(print, flush=True)

# More interesting generator string: "3;7,44*49,73,35:1,159:4,95:13,35:13,159:11,95:10,159:14,159:6,35:6,95:6;12;"

missionXML1 = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
            <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            
              <About>
                <Summary>Hello world!</Summary>
              </About>
              
              <ServerSection>
                <ServerInitialConditions>
                  <Time>
                    <StartTime>12000</StartTime>
                    <AllowPassageOfTime>false</AllowPassageOfTime>
                  </Time>
                  <Weather>clear</Weather>
                </ServerInitialConditions>
                <ServerHandlers>
                  <FlatWorldGenerator generatorString="3;50*7;140;"/>
                  <DrawingDecorator>
                    <DrawCuboid x1="-20" y1="42" z1="-20" x2="20" y2="50" z2="20" type="air"/>
                    <DrawCuboid x1="-20" y1="1" z1="-20" x2="20" y2="41" z2="20" type="glass"/>'''

missionXML2 = '''     <DrawCuboid x1="-20" y1="1" z1="21" x2="20" y2="50" z2="21" type="bedrock"/>
                    <DrawCuboid x1="-20" y1="1" z1="-21" x2="20" y2="50" z2="-21" type="bedrock"/>
                    <DrawCuboid x1="21" y1="1" z1="-20" x2="21" y2="50" z2="20" type="bedrock"/>
                    <DrawCuboid x1="-21" y1="1" z1="-20" x2="-21" y2="50" z2="20" type="bedrock"/>

                  </DrawingDecorator>
                  <ServerQuitWhenAnyAgentFinishes/>
                </ServerHandlers>
              </ServerSection>
              
              <AgentSection mode="Survival">
                <Name>MalmoTutorialBot</Name>
                <AgentStart>
                  <Placement x="0" y="42" z="0" yaw="0"/>
                  <Inventory>
                    <InventoryItem slot="0" type="diamond_pickaxe"/>
                  </Inventory>
                </AgentStart>
                <AgentHandlers>
                  <ObservationFromFullStats/>
                  <ContinuousMovementCommands turnSpeedDegs="180"/>
                </AgentHandlers>
              </AgentSection>
            </Mission>'''

missionXML= missionXML1 + random_sphere() + missionXML2

            

# Create default Malmo objects:

agent_host = MalmoPython.AgentHost()
try:
    agent_host.parse( sys.argv )
except RuntimeError as e:
    print('ERROR:',e)
    print(agent_host.getUsage())
    exit(1)
if agent_host.receivedArgument("help"):
    print(agent_host.getUsage())
    exit(0)

my_mission = MalmoPython.MissionSpec(missionXML, True)
my_mission_record = MalmoPython.MissionRecordSpec()

# Attempt to start a mission:
max_retries = 3
for retry in range(max_retries):
    try:
        agent_host.startMission( my_mission, my_mission_record )
        break
    except RuntimeError as e:
        if retry == max_retries - 1:
            print("Error starting mission:",e)
            exit(1)
        else:
            time.sleep(2)

# Loop until mission starts:
print("Waiting for the mission to start ", end=' ')
world_state = agent_host.getWorldState()
while not world_state.has_mission_begun:
    print(".", end="")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print("Error:",error.text)

print()
print("Mission running ", end=' ')

# Loop until mission ends:
while world_state.is_mission_running:
    print(".", end="")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print("Error:",error.text)

print()
print("Mission ended")
# Mission has ended.

