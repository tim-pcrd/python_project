from classes.db import Db

class Chain:
    def __init__(self):
        self.chainID = None
        self.chain_name = None

    def select_setup_chains(self, sessionID):
        db = Db()
        query = "SELECT chains.chainID, chains.chainName, setup_chain.channel \
                 FROM chains \
                 JOIN setup_chain \
                 ON chains.chainID = setup_chain.chainID \
                 JOIN setups \
                 ON setups.setupID = setup_chain.setupID \
                 WHERE setups.setupID = %s"
        data = (sessionID,)
        db_results = db.db_select(query, data)

        chains: list[Chain] = []
        if db_results:
            for result in db_results:
                chain = Chain()
                chain.chainID = result[0]
                chain.chain_name = result[1]
                chain.channel = result[2]

                chains.append(chain)

        return chains
