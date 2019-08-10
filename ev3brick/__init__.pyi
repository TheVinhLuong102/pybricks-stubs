from pybricks.parameters import (Align, Button, Color)


class sound:
    @classmethod
    def beep(cls, frequency: int = 500, duration: int = 100, volume: int = 30):
        """
        Play a beep/tone.

        ----------
        frequency : int - Frequency of the beep in Hertz (Default: 500).

        duration : int - Duration of the beep in milliseconds (Default: 100).

        volume : int - Volume of the beep as a percentage (Default: 30).
        """
        ...

    @classmethod
    def beeps(cls, number: int):
        """
        Play a number of default beeps with a brief pause in between.

        ----------
        number : int – Number of beeps.
        """
        ...

    @classmethod
    def file(cls, file_name: str, volume: int = 100):
        """
        Play a sound file.

        ----------
        file_name : str – Path to the sound file, including extension.

        volume : int - Volume of the sound as a percent. (Default: 100).
        """
        ...


class display:
    @classmethod
    def clear(cls):
        """
        Clear everything on the display.
        """

    @classmethod
    def image(cls, file_name: str, alignment: Align = Align.CENTER, coordinate: tuple = None, clear: bool = True):
        """
        Show an image file. You can specify its placement either using alignmentor by specifying a coordinate, 
        but not both.

        ----------
        file_name : str – Path to the image file. Paths may be absolute or relative from theproject folder.

        alignment : Align – Where to place the image (Default: Align.CENTER).

        coordinate : tuple – (x, y) coordinate tuple. It is the top-left corner of the image (Default: None).

        clear : bool – Whether to clear the screen before showing the image (Default:True).
        """
        ...

    @classmethod
    def text(cls, text: str, coordinate: tuple = None):
        """
        Display text.

        ----------
        text : str – The text to display.

        coordinate : tuple – (x, y) coordinate tuple. It is the top-left corner of the first character. If no coordinate is specified, it is printed on the next line.
        """
        ...


class battery:
    @classmethod
    def current(cls) -> float:
        """
        Get the current supplied by the battery.

        ----------
        Returns - Battery current.
        Return type - current: mA
        """
        ...

    @classmethod
    def voltage(cls) -> float:
        """
        Get the voltage of the battery.

        ----------
        Returns - Battery voltage.
        Return type - voltage: mV
        """
        ...


def buttons(channel: int) -> List[Button]:
    """
    Check which buttons on the infrared remote are pressed.

    ----------
    channel : int – Channel number of the remote.

    ----------
    Returns - List of pressed buttons on the remote on the specified channel.
    Return type - List of Button
    """
    ...


def light(color: Color):
    """
    Set the color of the brick light.

    ----------
    color : Color – Color of the light.  Choose Color.BLACK or None to turn the light off.
    """
    ...
