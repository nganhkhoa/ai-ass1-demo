import bloxorz.stages.stages as stages


def GenStage():
    maxlv = 1
    for i in range(maxlv):
        print("[+] Generating Stage {}".format(i + 1), end="\r")
        s = getattr(stages, "stage{}".format(i + 1, i + 1))
        s()

    print()
