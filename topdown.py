import numpy as np
import matplotlib.pyplot as plt
import json


with open('JsonStructure.json', 'r') as openfile:
        # Reading from json file
        json_object1 = json.load(openfile)
        cameraConfig1=json_object1['cameraConfig']
cameraConfig2=[i.replace('Default\\', '') for i in cameraConfig1]
# Plot
fig, ax = plt.subplots(constrained_layout=True)
cmap = plt.get_cmap('viridis')
colors = cmap(np.linspace(0, 1, len(cameraConfig2)))
for i in cameraConfig2:
    with open(i, 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    c=np.random.rand(3,)
    ax.scatter(json_object['Data']['Eye'][0], json_object['Data']['Eye'][2], label=json_object['Data']['Name'], color=c)
    # Draw camera direction arrow
    ax.quiver(json_object['Data']['Eye'][0], json_object['Data']['Eye'][2],
          -json_object['Data']['Eye'][0]+json_object['Data']['Lookat'][0], -json_object['Data']['Eye'][2]+json_object['Data']['Lookat'][2],
          angles='xy', scale_units='xy', scale=0.001,
          color=c)
ax.plot([-341.4/16, (15/16)*341.4], [0,0], c='blue', label='Target (origin)')

ax.set_xlabel('X')
ax.set_ylabel('Z')
ax.set_title('Top-Down View (XY Plane)')
ax.legend(bbox_to_anchor=(0, -0.5, 1, 1), loc='lower left',
                      ncols=5, mode="expand", borderaxespad=0.)
ax.grid(True)

plt.show()
