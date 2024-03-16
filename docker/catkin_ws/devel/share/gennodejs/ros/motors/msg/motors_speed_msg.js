// Auto-generated. Do not edit!

// (in-package motors.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class motors_speed_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.left_motor_speed = null;
      this.right_motor_speed = null;
    }
    else {
      if (initObj.hasOwnProperty('left_motor_speed')) {
        this.left_motor_speed = initObj.left_motor_speed
      }
      else {
        this.left_motor_speed = 0.0;
      }
      if (initObj.hasOwnProperty('right_motor_speed')) {
        this.right_motor_speed = initObj.right_motor_speed
      }
      else {
        this.right_motor_speed = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type motors_speed_msg
    // Serialize message field [left_motor_speed]
    bufferOffset = _serializer.float32(obj.left_motor_speed, buffer, bufferOffset);
    // Serialize message field [right_motor_speed]
    bufferOffset = _serializer.float32(obj.right_motor_speed, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type motors_speed_msg
    let len;
    let data = new motors_speed_msg(null);
    // Deserialize message field [left_motor_speed]
    data.left_motor_speed = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [right_motor_speed]
    data.right_motor_speed = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'motors/motors_speed_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '64774e203c8f0b9062c05b152b874c89';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 left_motor_speed
    float32 right_motor_speed
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new motors_speed_msg(null);
    if (msg.left_motor_speed !== undefined) {
      resolved.left_motor_speed = msg.left_motor_speed;
    }
    else {
      resolved.left_motor_speed = 0.0
    }

    if (msg.right_motor_speed !== undefined) {
      resolved.right_motor_speed = msg.right_motor_speed;
    }
    else {
      resolved.right_motor_speed = 0.0
    }

    return resolved;
    }
};

module.exports = motors_speed_msg;
