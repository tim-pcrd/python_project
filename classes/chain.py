from classes.db import Db
from classes.gearunit import Gearunit


class Chain:
    def __init__(self):
        self.chainID = None
        self.chain_name = None
        self.__gearunits: list[Gearunit] = []

    def select_setup_chains(self, sessionID):
        print("FUNCTIE AANGEROEPEN")
        print(sessionID)
        db = Db()
        query = "SELECT chains.chainID, chains.chainName, setup_chain.channel \
                 FROM sessions \
                 JOIN setups \
                 ON setups.setupID = sessions.setupID \
                 JOIN setup_chain \
                 ON setups.setupID = setup_chain.setupID \
                 JOIN chains \
                 ON chains.chainID = setup_chain.chainID \
                 WHERE sessions.sessionID = %s"
        data = (sessionID,)
        db_results = db.db_select(query, data)
        print(db_results)
        chains: list[Chain] = []
        if db_results:
            for result in db_results:
                chain = Chain()
                chain.chainID = result[0]
                chain.chain_name = result[1]
                chain.channel = result[2]
                chains.append(chain)

        return chains

    def select_chain_gearunits(self, chainID):
        db = Db()
        query = "SELECT gearunits.gearunitID, gearunits.gearunitName, gearunittypes.gearunittypeName, \
                 chain_gearunit.unitPosition \
                 FROM gearunits \
                 JOIN gearunittypes \
                 ON gearunittypes.gearunittypeID = gearunits.gearunitTypeID \
                 JOIN chain_gearunit \
                 ON gearunits.gearunitID = chain_gearunit.gearunitID \
                 JOIN chains \
                 ON chains.chainID = chain_gearunit.chainID \
                 WHERE chains.chainID = %s \
                 ORDER BY unitPosition"
        data = (chainID,)
        db_results = db.db_select(query, data)

        if db_results:
            for result in db_results:
                gearunit = Gearunit()
                gearunit.gearunitID = result[0]
                gearunit.gearunit_name = result[1]
                gearunit.gearunit_type_name = result[2]
                gearunit.unit_position = result[3]

                self.__gearunits.append(gearunit)

        return self.__gearunits

    def empty_gearunits_list(self):
        self.__gearunits.clear()

    def __str__(self) -> str:
        return f'{self.chainID}, {self.chain_name}'
