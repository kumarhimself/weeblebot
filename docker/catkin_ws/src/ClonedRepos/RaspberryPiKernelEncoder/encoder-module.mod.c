#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0x2e712c61, "module_layout" },
	{ 0x6bc3fbc0, "__unregister_chrdev" },
	{ 0x47229b5c, "gpio_request" },
	{ 0x45b62e8e, "gpio_to_desc" },
	{ 0x2b131b84, "__register_chrdev" },
	{ 0xb1ad28e0, "__gnu_mcount_nc" },
	{ 0x51a910c0, "arm_copy_to_user" },
	{ 0xc5850110, "printk" },
	{ 0x92cc807, "gpiod_direction_input" },
	{ 0x92d5838e, "request_threaded_irq" },
	{ 0x8be6d30, "gpiod_unexport" },
	{ 0xfe990052, "gpio_free" },
	{ 0xcc43850a, "gpiod_export" },
	{ 0x499d16db, "gpiod_to_irq" },
	{ 0xbf813084, "gpiod_get_raw_value" },
	{ 0xc1514a3b, "free_irq" },
};

MODULE_INFO(depends, "");


MODULE_INFO(srcversion, "78354328B79A842DB9B7EDC");
