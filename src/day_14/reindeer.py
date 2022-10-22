__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"


################################################################################

class Reindeer(object):
    """
    Reindeer class representation with all things needed for Reindeer Olympics.
    """

################################################################################

    def __init__(self,
                 name: str,
                 speed: int,
                 fly_time: int,
                 rest_time: int) -> None:
        """
        Reindeer has its name, speed, fly time and rest time. It can provide
        information about itself and functions are provided for starting the
        race, advancing the race for one second and awarding points.

        :param name: name of the reindeer
        :param speed: reindeer speed (km/s)
        :param fly_time: time for which reindeer can fly until it is exhausted
        (s)
        :param rest_time: time for which an exhausted reindeer has to rest (s)
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
    def name(self) -> str:
        """
        :return: reindeer name
        """

        return self._NAME

################################################################################

    @property
    def distance(self) -> int:
        """
        :return: reindeer distance at any point of the race
        """

        return self._distance

################################################################################

    @property
    def is_flying(self) -> bool:
        """
        :return: True if the reindeer is currently flying, False otherwise
        (resting)
        """

        return self._fly_remaining_time is not None

################################################################################

    @property
    def is_resting(self) -> bool:
        """
        :return: True if the reindeer is exhausted and resting, False otherwise
        (flying)
        """

        return self._rest_remaining_time is not None

################################################################################

    @property
    def points(self) -> int:
        """
        :return: points awarded to the reindeer in any point of the race
        """

        return self._points

################################################################################

    def start(self) -> None:
        """
        Initializes everything needed for the start of the race.

        :return: None
        """

        self._distance = 0
        self._fly_remaining_time = self._FLY_TIME
        self._points = 0

################################################################################

    def advance(self) -> None:
        """
        Advances the reindeer for one second in the race.
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

    def award_point(self) -> None:
        """
        Awards a point to the reindeer.
        """

        self._points += 1

################################################################################
