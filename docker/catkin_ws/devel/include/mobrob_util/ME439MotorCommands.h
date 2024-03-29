// Generated by gencpp from file mobrob_util/ME439MotorCommands.msg
// DO NOT EDIT!


#ifndef MOBROB_UTIL_MESSAGE_ME439MOTORCOMMANDS_H
#define MOBROB_UTIL_MESSAGE_ME439MOTORCOMMANDS_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace mobrob_util
{
template <class ContainerAllocator>
struct ME439MotorCommands_
{
  typedef ME439MotorCommands_<ContainerAllocator> Type;

  ME439MotorCommands_()
    : cmd0(0)
    , cmd1(0)  {
    }
  ME439MotorCommands_(const ContainerAllocator& _alloc)
    : cmd0(0)
    , cmd1(0)  {
  (void)_alloc;
    }



   typedef int16_t _cmd0_type;
  _cmd0_type cmd0;

   typedef int16_t _cmd1_type;
  _cmd1_type cmd1;





  typedef boost::shared_ptr< ::mobrob_util::ME439MotorCommands_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mobrob_util::ME439MotorCommands_<ContainerAllocator> const> ConstPtr;

}; // struct ME439MotorCommands_

typedef ::mobrob_util::ME439MotorCommands_<std::allocator<void> > ME439MotorCommands;

typedef boost::shared_ptr< ::mobrob_util::ME439MotorCommands > ME439MotorCommandsPtr;
typedef boost::shared_ptr< ::mobrob_util::ME439MotorCommands const> ME439MotorCommandsConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mobrob_util::ME439MotorCommands_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mobrob_util::ME439MotorCommands_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::mobrob_util::ME439MotorCommands_<ContainerAllocator1> & lhs, const ::mobrob_util::ME439MotorCommands_<ContainerAllocator2> & rhs)
{
  return lhs.cmd0 == rhs.cmd0 &&
    lhs.cmd1 == rhs.cmd1;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::mobrob_util::ME439MotorCommands_<ContainerAllocator1> & lhs, const ::mobrob_util::ME439MotorCommands_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace mobrob_util

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::mobrob_util::ME439MotorCommands_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mobrob_util::ME439MotorCommands_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mobrob_util::ME439MotorCommands_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mobrob_util::ME439MotorCommands_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mobrob_util::ME439MotorCommands_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mobrob_util::ME439MotorCommands_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mobrob_util::ME439MotorCommands_<ContainerAllocator> >
{
  static const char* value()
  {
    return "853bb91b9c3f09306e8c71787dc35bdf";
  }

  static const char* value(const ::mobrob_util::ME439MotorCommands_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x853bb91b9c3f0930ULL;
  static const uint64_t static_value2 = 0x6e8c71787dc35bdfULL;
};

template<class ContainerAllocator>
struct DataType< ::mobrob_util::ME439MotorCommands_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mobrob_util/ME439MotorCommands";
  }

  static const char* value(const ::mobrob_util::ME439MotorCommands_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mobrob_util::ME439MotorCommands_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int16 cmd0\n"
"int16 cmd1\n"
;
  }

  static const char* value(const ::mobrob_util::ME439MotorCommands_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mobrob_util::ME439MotorCommands_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.cmd0);
      stream.next(m.cmd1);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ME439MotorCommands_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mobrob_util::ME439MotorCommands_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mobrob_util::ME439MotorCommands_<ContainerAllocator>& v)
  {
    s << indent << "cmd0: ";
    Printer<int16_t>::stream(s, indent + "  ", v.cmd0);
    s << indent << "cmd1: ";
    Printer<int16_t>::stream(s, indent + "  ", v.cmd1);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOBROB_UTIL_MESSAGE_ME439MOTORCOMMANDS_H
