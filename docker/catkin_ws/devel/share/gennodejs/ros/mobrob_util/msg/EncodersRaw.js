// Auto-generated. Do not edit!

// (in-package mobrob_util.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class EncodersRaw {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.e0 = null;
      this.e1 = null;
      this.t = null;
    }
    else {
      if (initObj.hasOwnProperty('e0')) {
        this.e0 = initObj.e0
      }
      else {
        this.e0 = 0;
      }
      if (initObj.hasOwnProperty('e1')) {
        this.e1 = initObj.e1
      }
      else {
        this.e1 = 0;
      }
      if (initObj.hasOwnProperty('t')) {
        this.t = initObj.t
      }
      else {
        this.t = {secs: 0, nsecs: 0};
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type EncodersRaw
    // Serialize message field [e0]
    bufferOffset = _serializer.int64(obj.e0, buffer, bufferOffset);
    // Serialize message field [e1]
    bufferOffset = _serializer.int64(obj.e1, buffer, bufferOffset);
    // Serialize message field [t]
    bufferOffset = _serializer.time(obj.t, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type EncodersRaw
    let len;
    let data = new EncodersRaw(null);
    // Deserialize message field [e0]
    data.e0 = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [e1]
    data.e1 = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [t]
    data.t = _deserializer.time(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'mobrob_util/EncodersRaw';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '593ef6f85d37b23b49a86251ea1a5b8e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 e0
    int64 e1
    time t
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new EncodersRaw(null);
    if (msg.e0 !== undefined) {
      resolved.e0 = msg.e0;
    }
    else {
      resolved.e0 = 0
    }

    if (msg.e1 !== undefined) {
      resolved.e1 = msg.e1;
    }
    else {
      resolved.e1 = 0
    }

    if (msg.t !== undefined) {
      resolved.t = msg.t;
    }
    else {
      resolved.t = {secs: 0, nsecs: 0}
    }

    return resolved;
    }
};

module.exports = EncodersRaw;
