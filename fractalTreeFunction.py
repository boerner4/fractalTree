import numpy as np
import matplotlib.pyplot as plt

def branchOut(x1,y1,scale_factor,starting_angle,branch_angles,number_of_iterations,current_iteration):
    distance = scale_factor**(current_iteration)
    x2 = x1 + np.cos(np.deg2rad(starting_angle))*distance
    y2 = y1 + np.sin(np.deg2rad(starting_angle))*distance
    if current_iteration != number_of_iterations:
        plt.plot([x1,x2],[y1,y2])
    #    line([x1,x2],[y1,y2],'LineWidth',1,'Color',cols(current_iteration+1,:))

        branchOut(x2,y2,scale_factor,starting_angle+branch_angles[0],branch_angles,number_of_iterations,current_iteration+1)
        branchOut(x2,y2,scale_factor,starting_angle-branch_angles[1],branch_angles,number_of_iterations,current_iteration+1)
    #return x2

