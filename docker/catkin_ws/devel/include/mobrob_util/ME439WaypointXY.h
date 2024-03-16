// Generated by gencpp from file mobrob_util/ME439WaypointXY.msg
// DO NOT EDIT!


#ifndef MOBROB_UTIL_MESSAGE_ME439WAYPOINTXY_H
#define MOBROB_UTIL_MESSAGE_ME439WAYPOINTXY_H


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
struct ME439WaypointXY_
{
  typedef ME439WaypointXY_<ContainerAllocator> Type;

  ME439WaypointXY_()
    : x(0.0)
    , y(0.0)  {
    }
  ME439WaypointXY_(const ContainerAllocator& _alloc)
    : x(0.0)
    , y(0.0)  {
  (void)_alloc;
    }



   typedef float _x_type;
  _x_type x;

   typedef float _y_type;
  _y_type y;





  typedef boost::shared_ptr< ::mobrob_util::ME439WaypointXY_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mobrob_util::ME439WaypointXY_<ContainerAllocator> const> ConstPtr;

}; // struct ME439WaypointXY_

typedef ::mobrob_util::ME439WaypointXY_<std::allocator<void> > ME439WaypointXY;

typedef boost::shared_ptr< ::mobrob_util::ME439WaypointXY > ME439WaypointXYPtr;
typedef boost::shared_ptr< ::mobrob_util::ME439WaypointXY const> ME439WaypointXYConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mobrob_util::ME439WaypointXY_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mobrob_util::ME439WaypointXY_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::mobrob_util::ME439WaypointXY_<ContainerAllocator1> & lhs, const ::mobrob_util::ME439WaypointXY_<ContainerAllocator2> & rhs)
{
  return lhs.x == rhs.x &&
    lhs.y == rhs.y;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::mobrob_util::ME439WaypointXY_<ContainerAllocator1> & lhs, const ::mobrob_util::ME439WaypointXY_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace mobrob_util

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::mobrob_util::ME439WaypointXY_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mobrob_util::ME439WaypointXY_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mobrob_util::ME439WaypointXY_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mobrob_util::ME439WaypointXY_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mobrob_util::ME439WaypointXY_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mobrob_util::ME439WaypointXY_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mobrob_util::ME439WaypointXY_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ff8d7d66dd3e4b731ef14a45d38888b6";
  }

  static const char* value(const ::mobrob_util::ME439WaypointXY_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xff8d7d66dd3e4b73ULL;
  static const uint64_t static_value2 = 0x1ef14a45d38888b6ULL;
};

template<class ContainerAllocator>
struct DataType< ::mobrob_util::ME439WaypointXY_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mobrob_util/ME439WaypointXY";
  }

  static const char* value(const ::mobrob_util::ME439WaypointXY_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mobrob_util::ME439WaypointXY_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 x\n"
"float32 y\n"
;
  }

  static const char* value(const ::mobrob_util::ME439WaypointXY_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mobrob_util::ME439WaypointXY_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ME439WaypointXY_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mobrob_util::ME439WaypointXY_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mobrob_util::ME439WaypointXY_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<float>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<float>::stream(s, indent + "  ", v.y);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOBROB_UTIL_MESSAGE_ME439WAYPOINTXY_H
