#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy  # ROS 라이브러리
from std_msgs.msg import String
import sys
import select

def main():
    # 퍼블리시 노드 초기화
    rospy.init_node('gps_walk_node', anonymous=False)

    # 퍼블리셔 변수
    pub = rospy.Publisher("/gps_walk", String, queue_size=1)

    # 입력값 변수 초기화
    user_input = None

    # 0.1초마다 반복(변수=rate)
    rate = rospy.Rate(10)  # 10Hz

    # 중단되거나 사용자가 강제종료(ctrl+C) 전까지 계속 실행
    while not rospy.is_shutdown():
        try:
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                # 사용자로부터 입력을 받음
                user_input = sys.stdin.readline().strip()
        except KeyboardInterrupt:
            rospy.loginfo("Shutting down gps_walk_node...")
            break  # 사용자가 ctrl+C로 종료하면 루프 종료


        pub.publish(user_input)

        rate.sleep()  # 주기적으로 루프 반복

if __name__ == '__main__':
    main()