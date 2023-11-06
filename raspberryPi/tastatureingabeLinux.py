import keyboard

keyboard.on_press(lambda event:
                  print(f"Taste gedrückt: {event.name}")
                  )

#keyboard.on_release(lambda event:
#                    print(f"Taste losgelassen: {event.name}")
#                    )

keyboard.wait('esc')  # Beenden Sie das Programm, wenn die Escape-Taste gedrückt wird