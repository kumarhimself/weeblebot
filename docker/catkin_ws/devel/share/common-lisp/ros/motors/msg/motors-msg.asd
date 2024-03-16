
(cl:in-package :asdf)

(defsystem "motors-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "motors_speed_msg" :depends-on ("_package_motors_speed_msg"))
    (:file "_package_motors_speed_msg" :depends-on ("_package"))
  ))