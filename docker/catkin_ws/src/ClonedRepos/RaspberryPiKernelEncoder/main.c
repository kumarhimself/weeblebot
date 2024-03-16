#include "device_file.h"
#include <linux/init.h>       /* module_init, module_exit */
#include <linux/module.h> /* version info, MODULE_LICENSE, MODULE_AUTHOR, printk() */

//kernel module setup file

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Joshua Tabor");
/*===============================================================================================*/
static int encoder_driver_init(void)
{
      int result = 0;
    printk( KERN_NOTICE "encoder init" );

      result = register_device();
    return result;
}
/*-----------------------------------------------------------------------------------------------*/
static void encoder_driver_exit(void)
{
   printk( KERN_NOTICE "encoder ending");
    unregister_device();
}
/*===============================================================================================*/

module_init(encoder_driver_init);
module_exit(encoder_driver_exit);
