class Reindeer(object):
    """

    """

################################################################################

    def __init__(self, name, speed, fly_time, rest_time) -> None:
        """

        :param speed:
        :param fly_time:
        :param rest_time:
        """

        self._NAME = name
        self._SPEED = speed
        self._FLY_TIME = fly_time
        self._REST_TIME = rest_time
        self._distance = None
        self._fly_remaining_time = None
        self._rest_remaining_time = None
        self._points = None

################################################################################

    @property
    def name(self):
        """

        :return:
        """

        return self._NAME

################################################################################

    @property
    def distance(self):
        """

        :return:
        """

        return self._distance

################################################################################

    @property
    def is_flying(self):
        """

        :return:
        """

        return self._fly_remaining_time is not None

################################################################################

    @property
    def is_resting(self):
        """

        :return:
        """

        return self._rest_remaining_time is not None

################################################################################

    @property
    def points(self):
        """

        :return:
        """

        return self._points

################################################################################

    def start(self):
        """

        :return:
        """

        self._distance = 0
        self._fly_remaining_time = self._FLY_TIME
        self._points = 0

################################################################################

    def advance(self):
        """

        :return:
        """

        if self.is_flying:
            self._distance += self._SPEED
            self._fly_remaining_time -= 1

            if self._fly_remaining_time == 0:
                self._fly_remaining_time = None
                self._rest_remaining_time = self._REST_TIME
        else:
            self._rest_remaining_time -= 1

            if self._rest_remaining_time == 0:
                self._rest_remaining_time = None
                self._fly_remaining_time = self._FLY_TIME


################################################################################

    def award_point(self):
        """

        :return:
        """

        self._points += 1

################################################################################
