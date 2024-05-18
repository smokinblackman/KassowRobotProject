#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image, Imu
from cv_bridge import CvBridge
import cv2

def color_callback(data):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    cv2.imshow("Color Image", cv_image)
    cv2.waitKey(1)

def depth_callback(data):
    bridge = CvBridge()
    depth_image = bridge.imgmsg_to_cv2(data, "16UC1")
    cv2.imshow("Depth Image", depth_image)
    cv2.waitKey(1)

def imu_callback(data):
    rospy.loginfo("IMU Data: %s", data)

def main():
    rospy.init_node('realsense_kassow_integration', anonymous=True)
    rospy.Subscriber("/camera/color/image_raw", Image, color_callback)
    rospy.Subscriber("/camera/depth/image_raw", Image, depth_callback)
    rospy.Subscriber("/camera/imu", Imu, imu_callback)
    rospy.spin()

if __name__ == "__main__":
    print("Hello, Kassow Robot!")
    main()
