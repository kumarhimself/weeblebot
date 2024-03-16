; Auto-generated. Do not edit!


(cl:in-package mobrob_util-msg)


;//! \htmlinclude EncodersRaw.msg.html

(cl:defclass <EncodersRaw> (roslisp-msg-protocol:ros-message)
  ((e0
    :reader e0
    :initarg :e0
    :type cl:integer
    :initform 0)
   (e1
    :reader e1
    :initarg :e1
    :type cl:integer
    :initform 0)
   (t
    :reader t
    :initarg :t
    :type cl:real
    :initform 0))
)

(cl:defclass EncodersRaw (<EncodersRaw>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <EncodersRaw>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'EncodersRaw)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mobrob_util-msg:<EncodersRaw> is deprecated: use mobrob_util-msg:EncodersRaw instead.")))

(cl:ensure-generic-function 'e0-val :lambda-list '(m))
(cl:defmethod e0-val ((m <EncodersRaw>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mobrob_util-msg:e0-val is deprecated.  Use mobrob_util-msg:e0 instead.")
  (e0 m))

(cl:ensure-generic-function 'e1-val :lambda-list '(m))
(cl:defmethod e1-val ((m <EncodersRaw>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mobrob_util-msg:e1-val is deprecated.  Use mobrob_util-msg:e1 instead.")
  (e1 m))

(cl:ensure-generic-function 't-val :lambda-list '(m))
(cl:defmethod t-val ((m <EncodersRaw>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mobrob_util-msg:t-val is deprecated.  Use mobrob_util-msg:t instead.")
  (t m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <EncodersRaw>) ostream)
  "Serializes a message object of type '<EncodersRaw>"
  (cl:let* ((signed (cl:slot-value msg 'e0)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'e1)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let ((__sec (cl:floor (cl:slot-value msg 't)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 't) (cl:floor (cl:slot-value msg 't)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <EncodersRaw>) istream)
  "Deserializes a message object of type '<EncodersRaw>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'e0) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'e1) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 't) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<EncodersRaw>)))
  "Returns string type for a message object of type '<EncodersRaw>"
  "mobrob_util/EncodersRaw")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'EncodersRaw)))
  "Returns string type for a message object of type 'EncodersRaw"
  "mobrob_util/EncodersRaw")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<EncodersRaw>)))
  "Returns md5sum for a message object of type '<EncodersRaw>"
  "593ef6f85d37b23b49a86251ea1a5b8e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'EncodersRaw)))
  "Returns md5sum for a message object of type 'EncodersRaw"
  "593ef6f85d37b23b49a86251ea1a5b8e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<EncodersRaw>)))
  "Returns full string definition for message of type '<EncodersRaw>"
  (cl:format cl:nil "int64 e0~%int64 e1~%time t~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'EncodersRaw)))
  "Returns full string definition for message of type 'EncodersRaw"
  (cl:format cl:nil "int64 e0~%int64 e1~%time t~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <EncodersRaw>))
  (cl:+ 0
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <EncodersRaw>))
  "Converts a ROS message object to a list"
  (cl:list 'EncodersRaw
    (cl:cons ':e0 (e0 msg))
    (cl:cons ':e1 (e1 msg))
    (cl:cons ':t (t msg))
))
