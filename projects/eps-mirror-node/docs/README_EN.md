# EPS trajectory routing

During the Fall 2025 EPS at ENIT, our five-person Team BOB worked on a Ridgeback–Kinova mobile manipulator. I handled the Kinova-side environment, topic/message analysis, simulation integration, trajectory routing, and setup documentation.

[![Kinova hardware and the combined Gazebo model](../assets/kinova-overview.jpg)](../assets/kinova-demo-1x.mp4)

[16-second MP4 excerpt](../assets/kinova-demo-1x.mp4). I cropped the views from the original edited video. They do not share a time reference, so the video cannot show whether both systems ran at the same time.

A teammate suggested using MoveIt's display topic. I checked the interfaces and used AI for code drafts, then ran the code and changed the parts that did not work as expected. The router takes the first JointTrajectory and changes `joint_*` / `arm_0_joint_*` names while keeping the trajectory order.

I checked the combined Gazebo model and the physical Kinova arm on its own. We could not complete the full physical Ridgeback–Kinova setup because of the Ridgeback battery problem. I did not measure latency or synchronization error.

When preparing the portfolio in September 2026, I added packaging, input checks and tests. Sending commands to hardware now requires an explicit setting. These changes were made after the semester project. I have not run this revised version with ROS2 or the physical robot.

[Main README](../README.md) · [Running](running.md) · [Source and attribution](../SOURCES.md)
