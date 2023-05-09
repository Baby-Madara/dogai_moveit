#! /usr/bin/env python3

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()

group_fr = moveit_commander.MoveGroupCommander("limb_fr")
group_fl = moveit_commander.MoveGroupCommander("limb_fl")
group_br = moveit_commander.MoveGroupCommander("limb_br")
group_bl = moveit_commander.MoveGroupCommander("limb_bl")

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory)

group_variable_values_fr = group_fr.get_current_joint_values()
group_variable_values_fl = group_fl.get_current_joint_values()
group_variable_values_br = group_br.get_current_joint_values()
group_variable_values_bl = group_bl.get_current_joint_values()

group_variable_values_fr[0] = 0.5
group_variable_values_fr[1] = -1.5
group_variable_values_fr[2] = -1.5

group_variable_values_fl[0] = 0.5
group_variable_values_fl[1] = 1.5
group_variable_values_fl[2] = -0.5

group_variable_values_br[0] = 0.5
group_variable_values_br[1] = -1.5
group_variable_values_br[2] = -1

group_variable_values_bl[0] = 0.5
group_variable_values_bl[1] = 1.5
group_variable_values_bl[2] = -1

group_fr.set_joint_value_target(group_variable_values_fr)
group_fl.set_joint_value_target(group_variable_values_fl)
group_br.set_joint_value_target(group_variable_values_br)
group_bl.set_joint_value_target(group_variable_values_bl)

plan_fr = group_fr.plan()
plan_fl = group_fl.plan()
plan_br = group_br.plan()
plan_bl = group_bl.plan()

group_fr.go(wait=True)
group_fl.go(wait=True)
group_br.go(wait=True)
group_bl.go(wait=True)
#move_group = moveit_commander.MoveGroupCommander("both_arms")
#move_group.execute(plan_fr, plan_fl)

pose_fr = group_fr.get_current_pose()
pose_fl = group_fl.get_current_pose()
pose_br = group_br.get_current_pose()
pose_bl = group_bl.get_current_pose()

print("End Effector Pose of dog_fr: ", pose_fr)
print("End Effector Pose of dog_fl: ", pose_fl)
print("End Effector Pose of dog_br: ", pose_br)
print("End Effector Pose of dog_bl: ", pose_bl)

moveit_commander.roscpp_shutdown()