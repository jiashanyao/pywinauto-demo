from pywinauto import Desktop, mouse
notifyWindow = Desktop(backend="uia").window(title_re='New notification')
notifyWindow.wait('visible', timeout=20)
print(notifyWindow.print_control_identifiers())
mailNotification = notifyWindow.child_window(title_re='New notification from Mail')
rect = mailNotification.rectangle()
mouse.click(coords=(rect.left // 2 + rect.right // 2, rect.top // 2 + rect.bottom // 2 - 50))
