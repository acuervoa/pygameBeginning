class AntStateSeeking(State):

    def __init__(self, ant):

        State.__init__(self, "seeking")
        self.ant = ant
        self.leaf_id = None

    def check_conditions(self):

        # If the lead is gone, then go back to exploring
        leaf = self.ant.world.get(self.ant.leaf_id)
        if leaf is None:
            return "exploring"

        # If we are next ot the lear, pick it up and deliver it
        if self.ant.location.get_distance_to(leaf.location) < 5.0:

            self.ant.carry(leaf.image)
            self.ant.world.remove_entity(leaf)
            return "delivering"

        return None

    def entry_actions(self):

        # Set the destination to the location of the leaf
        leaf = self.ant.world.get(self.ant.leaf_id)
        if leaf is not None:
            self.ant.destination = leaf.location
            self.ant.speed = 160. + randint(-20, 20)
            
