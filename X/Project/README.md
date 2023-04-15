# GOOGLE
GOOd GLobal Extented-horizon path planning.

The video URL is: https://youtu.be/0sbfT9YQop4

Autonomous Underwater Vehicles (AUVs) have been used extensively to investigate different oceanographic phenomena.
One benefit of AUV exploration is fast deployment and the ability to guide the in-situ sampling without much human involvement. By bridging statistical modeling, embedded computing, and sensor technology, one can conduct AUV missions using adaptive sampling, which has gained more interest in oceanographic surveying. Adaptive sampling entails that the AUV updates its trajectory on the fly. The updated trajectory is expected to give higher rewards in some way. This reward could be defined via reduced uncertainty of a variable of interest or by identifying hot-spots in the field. Of course, low rewards or very high costs should be assigned to collisions or neglected time constraints.
Adaptive sampling has shown beneficial when exploring uncertain phenomena such as plumes or oceanfronts, where one can gain significantly by adjusting course and trajectory based on what is sampled at earlier stages. We will focus on river plume characterization in this paper. Other examples of successful AUV adaptive sampling include the detection of dissolved oxygen and benthic habitat mapping.

In using only one AUV to conduct the adaptive sampling, dominating methods can be grouped into either myopic (greedy) or non-myopic approaches. Myopic schemes guide the agent (AUV) towards the most informative location selected from a subset of candidate locations within the myopic (near-sighted) neighborhood radius. The greediness of such computationally effective algorithms can make them fail at revealing other interesting areas. Non-myopic strategies can alleviate such challenges by expanding their search horizon. The previous research has shown the effectiveness of such long-horizon algorithms in a small-scale case where the shapes of the unknown objects are revealed by a robot arm, using global kriging variance reduction as the main criterion. It provides an idea of using cost-aware RRT* to generate sampling paths using cross-entropy as the cost function.
However, the computational costs associated with non-myopic algorithms are usually very high, and it has shown difficulty to apply these methods to larger-scale onboard computation in the ocean.

In this paper, we suggest a cost valley approach for non-myopic adaptive sampling. We use this approach to guide the agent to a promising path for collecting valuable information from the salinity field to reveal the river plume front. The goal of the deployment is to map unknown ocean properties while considering the remaining distance budget and avoiding the potential risks of collision with known static obstacles. We propose a long-horizon path planner to solve this problem by constructing a cost valley built on multiple penalty and reward fields that are flexibly weighted. In an extensive simulation study, we compare the suggested approach to common pre-scripted planners and greedy strategies. Results from a field deployment in the Trondheim fjord show the merits of the adaptive sampling approach to efficiently refine an ocean model prediction of the river plume with in-situ AUV measurements.

The main contribution of this work is the proposal of the flexible cost valley for long-horizon path planning in an informative field. The simulation study has shown the effect of the weighting mechanism on the behavior of the AUVs. It has also shown that the equal weighting scheme is the most optimal one for our case. In the field experiment, we used RRT* as the path planner to determine the next waypoint and a budget ellipse for the time restriction consideration. We take advantage of the flexibility of the Gaussian random field to build our proxy model for the surface salinity field. The full-scale field experiment demonstrated the success of using the cost valley concept for multi-objective path planning. The balance between exploitation and exploration and the hard constraint on safety and punctuality are all considered and well shown in the final result.

To improve the system in the future, one can possibly add a dynamic obstacle avoidance system by leveraging the AIS system. We used rather standard auto-regressive modeling for the temporal variation, a more comprehensive temporal model can be incorporated to alleviate the drawback of trusting too much on the numerical data.


# EDA analysis reminders
There are three important parameters used to adjust SINMOD data and for EIBV exploration.
- $\beta_0 = 0.26095833$
- $\beta_1 = 0.99898364$
- $threshold = 26.81189868$

Here comes the parameters used in the actual test for GRF kernel.
- $\sigma = 1.5$
- $\tau = .4$
- `lateral range = 700m`
- $\phi = 4.5/700$



# HITL test:
Open 4 iterfaces either through tmux or `Ctrl+Alt+T`.
---
- `cd ~/catkin_ws/`
- `source devel/setup.bash`
---
- `cd ~/dune_all/build`
- `./dune -c lauv-simulator-1 -p Simulation`
---
- `cd ~/catkin_ws/`
- `source devel/setup.bash`
- `roslaunch src/imc_ros_interface/launch/bridge.launch `
---
- `cd Simulation_2DNidelva/HITL/`
- `python3 GOOGLELauncher.py`
