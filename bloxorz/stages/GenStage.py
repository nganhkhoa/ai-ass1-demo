import bloxorz.stages.stages as stages


def GenStage():
    maxlv = 2
    for i in range(maxlv):
        print("[+] Generating Stage {} / {}".format(i + 1, maxlv), end="\r")
        s = getattr(stages, "stage{}".format(i + 1, i + 1))
        s()
