;; Auto-generated. Do not edit!


(when (boundp 'motors::motors_speed_msg)
  (if (not (find-package "MOTORS"))
    (make-package "MOTORS"))
  (shadow 'motors_speed_msg (find-package "MOTORS")))
(unless (find-package "MOTORS::MOTORS_SPEED_MSG")
  (make-package "MOTORS::MOTORS_SPEED_MSG"))

(in-package "ROS")
;;//! \htmlinclude motors_speed_msg.msg.html


(defclass motors::motors_speed_msg
  :super ros::object
  :slots (_left_motor_speed _right_motor_speed ))

(defmethod motors::motors_speed_msg
  (:init
   (&key
    ((:left_motor_speed __left_motor_speed) 0.0)
    ((:right_motor_speed __right_motor_speed) 0.0)
    )
   (send-super :init)
   (setq _left_motor_speed (float __left_motor_speed))
   (setq _right_motor_speed (float __right_motor_speed))
   self)
  (:left_motor_speed
   (&optional __left_motor_speed)
   (if __left_motor_speed (setq _left_motor_speed __left_motor_speed)) _left_motor_speed)
  (:right_motor_speed
   (&optional __right_motor_speed)
   (if __right_motor_speed (setq _right_motor_speed __right_motor_speed)) _right_motor_speed)
  (:serialization-length
   ()
   (+
    ;; float32 _left_motor_speed
    4
    ;; float32 _right_motor_speed
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _left_motor_speed
       (sys::poke _left_motor_speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _right_motor_speed
       (sys::poke _right_motor_speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _left_motor_speed
     (setq _left_motor_speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _right_motor_speed
     (setq _right_motor_speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get motors::motors_speed_msg :md5sum-) "64774e203c8f0b9062c05b152b874c89")
(setf (get motors::motors_speed_msg :datatype-) "motors/motors_speed_msg")
(setf (get motors::motors_speed_msg :definition-)
      "float32 left_motor_speed
float32 right_motor_speed
")



(provide :motors/motors_speed_msg "64774e203c8f0b9062c05b152b874c89")


