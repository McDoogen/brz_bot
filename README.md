# brz-bot
brz-bot is an experimentation with ROS 2, localization, and teleoperation! Fun! :D

# Other Packages Used
1. https://github.com/ros-teleop/teleop_tools.git

# Tasks for Phase 2:
1. Improve Acceleration for starting/stopping movements
2. Add battery improvements to remove cables

# Parts needed for Future Phases:
1. Battery Pack for Logic (5V)
2. Battery Pack for Motor (5V)
3. Improved Motor Battery connections (find JST...)
4. Improved Mount for Pi to Robot Base
5. Dynamixel Motors
    -> This will affect voltage needs as well
    -> This will need more space potentially meaning modifications to the robot base
    -> Check compatibility with Raspberry PI.
6. Ultrasonic Range Sensor Integration

Batteries can be 9V for a smaller footprint and then stepped down. What is the Voltage range for the PI?

# Useful Commands to Stop Forgetting
rosdep install -i --from-path src --rosdistro galactic -y

# Questions needing answers
1. Is it possible to develop and build entirely on our PC, and then deploy to our PI? Can we just move the build folders over and not need to clone the src?