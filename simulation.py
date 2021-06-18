class Simulatable():
    def __init__(self):
        self.assets = []
        self.costs = []

    def add_asset(self, asset):
        self.assets.append(asset)

    def add_cost(self, cost):
        self.assets.append(cost)

    def tick_day(self):
        #costs first incase there is an overdraw
        for cost in self.costs:
            cost.tick_day()

        for asset in self.assets:
            # tick a day for all assets
            asset.tick_day()
