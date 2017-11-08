class AntStateHunting(State):

    def __init__(self, ant):

        State.__init__(self, "hunting")
        self.ant = ant
        self.got_kill = False

    def do_actions(self):

        spider = self.ant.world.get(self.ant.spider_id)

        if spider is None:
            return

        self.ant.destination = spider.location

        if self.ant.location.get_distance_to(spider.location) < 15.:

            # Give the spider a fighting chance to avoid being killed!
            if randint(1, 5) == 1:
                spider.bitten()

                # If the spider is dead, move it back to the nest
                if spider.health <= 0:
                    self.ant.carry(spider.image)
                    self.ant.world.remove_entity(spider)
                    self.got_kill = True

    def check_conditions(self):

        if self.got_kill:
            return "delivering"

        spider = self.ant.world.get(self.ant.spider_id)

        # If the spider has been killed then return to exploring state
        if spider is None:
            return "exploring"

        # If the spider gets far enough way, return to exploring state
        if spider.location.get_distance_to(NEST_POSITION) > NEST_SIZE * 3:
            return "exploring"

        return None

    def entry_actions(self):

        self.speed = 160. + randint(0, 50)

    def exit_actions(self):

        self.got_kill = False
        
