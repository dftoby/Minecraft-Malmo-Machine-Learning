
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


from builtins import range
import malmo.MalmoPython as MalmoPython
import os
import sys
import time
import random

def limited_sphere():
    # Generates a limited map with only one set of sphere
    # Calculate randomized margine
    random_x = random.randint(0, 7)
    random_z = random.randint(0, 7)
    # Set up new sphere string
    new_sphere = '''<DrawSphere x="''' + str(random_x)+ '''" y="10" z="''' + str(random_z) + '''" radius="7" type="purpur_block"/>
                    <DrawSphere x="''' + str(random_x)+ '''" y="10" z="''' + str(random_z) + '''" radius="5" type="gold_block"/>
                    <DrawSphere x="''' + str(random_x)+ '''" y="10" z="''' + str(random_z) + '''" radius="3" type="iron_block"/>
                    <DrawSphere x="''' + str(random_x)+ '''" y="10" z="''' + str(random_z) + '''" radius="1" type="diamond_block"/>'''
    
    return new_sphere

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
                    <DrawCuboid x1="-100" y1="1" z1="-100" x2="100" y2="100" z2="100" type="air"/>
                    <DrawCuboid x1="-10" y1="1" z1="-10" x2="10" y2="20" z2="10" type="glass"/>'''

missionXML2 = '''     <DrawCuboid x1="-10" y1="1" z1="11" x2="10" y2="22" z2="11" type="bedrock"/>
                    <DrawCuboid x1="-10" y1="1" z1="-11" x2="10" y2="22" z2="-11" type="bedrock"/>
                    <DrawCuboid x1="11" y1="1" z1="-10" x2="11" y2="22" z2="10" type="bedrock"/>
                    <DrawCuboid x1="-11" y1="1" z1="-10" x2="-11" y2="22" z2="10" type="bedrock"/>

                  </DrawingDecorator>
                  <ServerQuitWhenAnyAgentFinishes/>
                  <Gamerule gamerule="allowCheats" value="true"/>
                </ServerHandlers>
              </ServerSection>
              
              <AgentSection mode="Survival">
                <Name>MalmoTutorialBot</Name>
                <AgentStart>
                  <Placement x="0.5" y="21" z="0.5" yaw="0"/>
                  <Inventory>
                    <InventoryItem slot="0" type="diamond_pickaxe"/>
                  </Inventory>
                </AgentStart>
                <AgentHandlers>
                  <DiscreteMovementCommands/>
                  <ObservationFromHotBar/>
                  <InventoryCommands/>
                  <ObservationFromFullStats/>
                  <ObservationFromGrid>
                      <Grid name="floor3x3x4">
                        <min x="-1" y="-1" z="-1"/>
                        <max x="1" y="2" z="1"/>
                      </Grid>
                  </ObservationFromGrid>
                </AgentHandlers>
              </AgentSection>
            </Mission>'''

missionXML= missionXML1 + limited_sphere() + missionXML2

