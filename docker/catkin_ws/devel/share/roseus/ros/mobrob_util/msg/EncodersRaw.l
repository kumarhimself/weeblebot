;; Auto-generated. Do not edit!


(when (boundp 'mobrob_util::EncodersRaw)
  (if (not (find-package "MOBROB_UTIL"))
    (make-package "MOBROB_UTIL"))
  (shadow 'EncodersRaw (find-package "MOBROB_UTIL")))
(unless (find-package "MOBROB_UTIL::ENCODERSRAW")
  (make-package "MOBROB_UTIL::ENCODERSRAW"))

(in-package "ROS")
;;//! \htmlinclude EncodersRaw.msg.html


(defclass mobrob_util::EncodersRaw
  :super ros::object
  :slots (_e0 _e1 _t ))

(defmethod mobrob_util::EncodersRaw
  (:init
   (&key
    ((:e0 __e0) 0)
    ((:e1 __e1) 0)
    ((:t __t) (instance ros::time :init))
    )
   (send-super :init)
   (setq _e0 (round __e0))
   (setq _e1 (round __e1))
   (setq _t __t)
   self)
  (:e0
   (&optional __e0)
   (if __e0 (setq _e0 __e0)) _e0)
  (:e1
   (&optional __e1)
   (if __e1 (setq _e1 __e1)) _e1)
  (:t
   (&optional __t)
   (if __t (setq _t __t)) _t)
  (:serialization-length
   ()
   (+
    ;; int64 _e0
    8
    ;; int64 _e1
    8
    ;; time _t
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _e0
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _e0 (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _e0) (= (length (_e0 . bv)) 2)) ;; bignum
              (write-long (ash (elt (_e0 . bv) 0) 0) s)
              (write-long (ash (elt (_e0 . bv) 1) -1) s))
             ((and (class _e0) (= (length (_e0 . bv)) 1)) ;; big1
              (write-long (elt (_e0 . bv) 0) s)
              (write-long (if (>= _e0 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _e0 s)(write-long (if (>= _e0 0) 0 #xffffffff) s)))
     ;; int64 _e1
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _e1 (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _e1) (= (length (_e1 . bv)) 2)) ;; bignum
              (write-long (ash (elt (_e1 . bv) 0) 0) s)
              (write-long (ash (elt (_e1 . bv) 1) -1) s))
             ((and (class _e1) (= (length (_e1 . bv)) 1)) ;; big1
              (write-long (elt (_e1 . bv) 0) s)
              (write-long (if (>= _e1 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _e1 s)(write-long (if (>= _e1 0) 0 #xffffffff) s)))
     ;; time _t
       (write-long (send _t :sec) s) (write-long (send _t :nsec) s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _e0
#+(or :alpha :irix6 :x86_64)
      (setf _e0 (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _e0 (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _e1
#+(or :alpha :irix6 :x86_64)
      (setf _e1 (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _e1 (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; time _t
     (send _t :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _t :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get mobrob_util::EncodersRaw :md5sum-) "593ef6f85d37b23b49a86251ea1a5b8e")
(setf (get mobrob_util::EncodersRaw :datatype-) "mobrob_util/EncodersRaw")
(setf (get mobrob_util::EncodersRaw :definition-)
      "int64 e0
int64 e1
time t

")



(provide :mobrob_util/EncodersRaw "593ef6f85d37b23b49a86251ea1a5b8e")


