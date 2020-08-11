class Ingredient(object):
    """
    Ingredient class representation. It is just static data put together with no
    special functions.
    """

    CAPACITY_KEY = "capacity"
    DURABILITY_KEY = "durability"
    FLAVOR_KEY = "flavor"
    TEXTURE_KEY = "texture"
    CALORIES_KEY = "calories"
    COMMA_KEY = ","

################################################################################

    def __init__(self, line: str) -> None:
        """
        Creates an ingredient object from a line from the input.

        :param line: line from the input with all the ingredient data
        """

        self._NAME = line.split(":")[0]
        self._CAPACITY = int(line.split(self.CAPACITY_KEY)[1].split(self.COMMA_KEY)[0])
        self._DURABILITY = int(line.split(self.DURABILITY_KEY)[1].split(self.COMMA_KEY)[0])
        self._FLAVOR = int(line.split(self.FLAVOR_KEY)[1].split(self.COMMA_KEY)[0])
        self._TEXTURE = int(line.split(self.TEXTURE_KEY)[1].split(self.COMMA_KEY)[0])
        self._CALORIES = int(line.split(self.CALORIES_KEY)[1].split(self.COMMA_KEY)[0])

################################################################################

    @property
    def name(self) -> str:
        """
        :return: ingredient name
        """

        return self._NAME

################################################################################

    @property
    def capacity(self) -> int:
        """
        :return: ingredient capacity score
        """

        return self._CAPACITY

################################################################################

    @property
    def durability(self) -> int:
        """
        :return: ingredient durability score
        """

        return self._DURABILITY

################################################################################

    @property
    def flavor(self) -> int:
        """
        :return: ingredient flavor score
        """

        return self._FLAVOR

################################################################################

    @property
    def texture(self) -> int:
        """
        :return: ingredient texture score
        """

        return self._TEXTURE

################################################################################

    @property
    def calories(self) -> int:
        """
        :return: ingredient calories score
        """

        return self._CALORIES

################################################################################

    def __str__(self):
        """
        :return: string representation of the ingredient
        """

        return self._NAME \
               + ": capacity " + str(self._CAPACITY) \
               + ", durability " + str(self._DURABILITY) \
               + ", flavor " + str(self._FLAVOR) \
               + ", texture " + str(self._TEXTURE) \
               + ", calories " + str(self._CALORIES)

################################################################################
