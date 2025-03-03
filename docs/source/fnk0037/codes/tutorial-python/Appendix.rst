##############################################################################
Appendix
##############################################################################

Following are details of functions in "Freenove_Micro_Rover.py" file.

+------------------------------------+-----------------------------------------------------------------+
|              Function              |                           Description                           |
+====================================+=================================================================+
| constrain(Value,Low,High)          | Used to constrain a value within an interval.                   |
+------------------------------------+-----------------------------------------------------------------+
| all_led_show(Brightness,R,G,B)     | ight up all the LEDs on the body, and you can set the           |
|                                    |                                                                 |
|                                    | brightness and color.                                           |
+------------------------------------+-----------------------------------------------------------------+
| led_show(Index, Brightness ,R,G,B) | Light up the specified LED on the car, and you can set the      |
|                                    |                                                                 |
|                                    | brightness and color                                            |
+------------------------------------+-----------------------------------------------------------------+
| hsl_to_rgb(Degree)                 | Converts the color value of the corresponding hue to            |
|                                    |                                                                 |
|                                    | an RGB value.                                                   |
+------------------------------------+-----------------------------------------------------------------+
| motor(Left,Right)                  | Control the left and right motors. Positive integer makes motor |
|                                    |                                                                 |
|                                    | move forward, negative integer makes motor move back. The       |
|                                    |                                                                 |
|                                    | larger the absolute value of the number, the faster the speed.  |
+------------------------------------+-----------------------------------------------------------------+
| get_distance()                     | Obtain the distance measurement value of the ultrasonic module. |
+------------------------------------+-----------------------------------------------------------------+