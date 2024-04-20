class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        This function defines the options for the remote control.
        :param __status: This variable keeps track of the power status of the tv ON/OFF
        :param __muted: Keeps track of if the tv is muted or not.
        :param __volume: Volume variable set to the min value.
        :param __channel: Channel variable set to the min channel.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """

        :return:
        """
        self.__status = not self.__status

    def mute(self):
        """

        :return:
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """

        :return:
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """

        :return:
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        """

        :return:
        """
        if self.__status and not self.__muted:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            self.__muted = False


    def volume_down(self):
        if self.__status and not self.__muted:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            self.__muted = False

    def __str__(self):
        status = "On" if self.__status else "Off"
        return f"Power = [{status}], Channel = [{self.__channel}], Volume = [{self.__volume}]"
