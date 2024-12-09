#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/image.hpp"

#include <cv_bridge/cv_bridge.h>
#include <image_transport/image_transport.hpp>
#include <opencv2/opencv.hpp>

#include <chrono>
#include <iostream>

using std::placeholders::_1;

class ImageSubscriber : public rclcpp::Node {

    public:
    ImageSubscriber() : Node("camera_node") {
        subscription_ = this->create_subscription<sensor_msgs::msg::Image>
        ("camera/image_raw", 1000, std::bind(&ImageSubscriber::topic_callback, this, _1));    
    }
    
    private:
    void topic_callback(const sensor_msgs::msg::Image & msg) const {
        cv_bridge::CvImagePtr cv_ptr;
        cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);
        cv::imwrite("path_to_save_image.jpg", cv_ptr->image);
    }
    rclcpp::Subscription<sensor_msgs::msg::Image>::SharedPtr subscription_;
};

int main(int argc, char *argv[]) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<ImageSubscriber>());
    rclcpp::shutdown();
    return 0;
}