#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/elfnote-lto.h>
#include <linux/export-internal.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;
BUILD_LTO_INFO;

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
	{ 0xc1514a3b, "free_irq" },
	{ 0x6cc3ca21, "gpiod_get_raw_value" },
	{ 0xb060cb12, "gpiod_to_irq" },
	{ 0xe3878111, "gpiod_export" },
	{ 0xfe990052, "gpio_free" },
	{ 0x92997ed8, "_printk" },
	{ 0x6cbbfc54, "__arch_copy_to_user" },
	{ 0x6a89f3fc, "gpiod_unexport" },
	{ 0x92d5838e, "request_threaded_irq" },
	{ 0xdc13939f, "gpiod_direction_input" },
	{ 0xed1c07b8, "__register_chrdev" },
	{ 0xddd1dbcb, "gpio_to_desc" },
	{ 0x47229b5c, "gpio_request" },
	{ 0x6bc3fbc0, "__unregister_chrdev" },
	{ 0xc6308436, "module_layout" },
};

MODULE_INFO(depends, "");


MODULE_INFO(srcversion, "0337071245912C6C8818B39");
