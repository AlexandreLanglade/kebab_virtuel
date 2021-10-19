from ivy.ivy import IvyServer


class SimuVocal(IvyServer):
    def __init__(self):
        IvyServer.__init__(self, "SimuVocal")
        self.start('127.255.255.255:2010')


if __name__ == "__main__":
    sv = SimuVocal()
    while(True):
        simulation = input("[SRA5 SIMULATION]: ")
        simulation = "sra5 Parsed=action=" + simulation + \
            " Confidence=0.8000000 NP=0 Num_A=0"
        sv.send_msg(simulation)
