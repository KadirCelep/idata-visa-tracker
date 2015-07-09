import objc

def notify(title, subtitle=None):
    global objc
    if not objc:
        objc = __import__('objc')
        swizzle(
            objc.lookUpClass('NSBundle'),
            'bundleIdentifier',
            swizzled_bundleIdentifier
        )

    NSUserNotification = objc.lookUpClass('NSUserNotification')
    NSUserNotificationCenter = objc.lookUpClass('NSUserNotificationCenter')
    if not NSUserNotification or not NSUserNotificationCenter:
        print('NSUserNotifcation is not supported by your version of Mac OS X')
        return

    notification = NSUserNotification.alloc().init()
    notification.setTitle_(str(title))
    if subtitle:
        notification.setSubtitle_(str(subtitle))

    notification_center = NSUserNotificationCenter.defaultUserNotificationCenter()
    notification_center.deliverNotification_(notification)