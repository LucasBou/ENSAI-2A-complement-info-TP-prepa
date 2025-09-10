import os
import json
import requests

from typing import List, Optional
from business_object.attack.attack_factory import AttackFactory
from business_object.attack.abstract_attack import AbstractAttack
from utils.singleton import Singleton

END_POINT = "/attack"


class AttackClient(metaclass=Singleton):
    def __init__(self) -> None:
        # Using an environment variable defined in the .env file
        self.__HOST = os.environ["HOST_WEBSERVICE"]
        self.attack_factory = AttackFactory()

    def get_attack(self, id: int) -> Optional[AbstractAttack]:
        """
        Get a specific attack from the webservice by calling the GET endpoint
        with a specific resource identifier.Do not raise any
        exception if any attack is found, just return None.

        :param id: attack id wanted
        :type id: int
        :return: The attack object with all value if the attack is found.
                 else None
        :rtype: AbstractAttack
        """
        url = f"{self.__HOST}{END_POINT}/{id}"
        print("GET  " + url + "\n")
        req = requests.get(url)

        # Check if the request is ok
        if req.status_code == 200:
            raw_attack = req.json()

            print("Réponse JSON obtenue :\n" + json.dumps(raw_attack, indent=2) + "\n")

            # TODO
            #   create an attack using the data contained in the json
            #   see class AttackFactory to do this

            return self.attack_factory.instantiate_attack(
                type=raw_attack["attack_type"],
                id=id,
                power=raw_attack["power"],
                name=raw_attack["name"],
                description=raw_attack["description"],
                accuracy=raw_attack["accuracy"],
                element=raw_attack["element"],
            )

        print(f"Something went wrong with the call :\n {req=}")

    def get_all_attack(self) -> Optional[AbstractAttack]:
        url = f"{self.__HOST}{END_POINT}/"
        print("GET  " + url + "\n")
        req = requests.get(url)

        # Check if the request is ok
        if req.status_code == 200:
            raw_attack = req.json()

            print("Réponse JSON obtenue :\n" + json.dumps(raw_attack, indent=2) + "\n")

            # TODO
            #   create an attack using the data contained in the json
            #   see class AttackFactory to do this

            return [
                self.attack_factory.instantiate_attack(
                    type=a["attack_type"],
                    id=id,
                    power=0,
                    name=a["name"],
                    description="Unknown effect",
                    accuracy=0,
                    element="Unknown",
                )
                for a in raw_attack["results"]
            ]

        print(f"Something went wrong with the call :\n {req=}")


# Execute Code When the File Runs as a Script
if __name__ == "__main__":
    # To load environment variables contained in the .env file
    import dotenv

    dotenv.load_dotenv(override=True)

    attack_client = AttackClient()

    attack_id = 1
    attack_client.get_attack(attack_id)
