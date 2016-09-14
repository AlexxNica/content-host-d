import argparse
from subprocess import call


def docker_loop(image, t="latest", h=None, c=1, a=None, p=50000):
    if not image:
        return "An image must be specified."

    d_string = "docker run -d -v /dev/log:/dev/log{h}{p}{a}{i}"

    if ":" not in image:
        image = image + ":"

    if "{}" not in h:
        h = h + "{}"
    h = " -h " + h

    t = t.split(",")

    a = a = " -e " + " -e ".join(a.split(","))

    for i in range(c):
        call(d_string.format(
            h=h.format(i),
            p=" -p {}:22".format(p + i),
            a=a.replace("{}", t[i % len(t)] if len(t) > 1 else t[0]),
            i=image.format(t[i % len(t)] if len(t) > 1 else t[0])
        ), shell=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--image", type=str,
        help="The docker image to use (e.g 'jacobcallahan/content-host-d').")
    parser.add_argument(
        "-t", "--tag", type=str,
        help="The image tage to use (e.g 'latest', or '5,6,7').")
    parser.add_argument(
        "-n", "--hostname", type=str,
        help="The base hostname to use. (e.g 'Host{}', 'Test{}Docker', 'Docker').")
    parser.add_argument(
        "-c", "--count", type=int,
        help="How many containers to create.")
    parser.add_argument(
        "-a", "--args", type=str,
        help="The arguments to pass to the container (e.g 'SATHOST=my.host.domain.com,AK={}tools').")
    parser.add_argument(
        "-p", "--port", type=int,
        help="The port to start mapping ssh to (default 50000).")

    args = parser.parse_args()

    if not args.image:
        print ("An image must be specified. Use the -i or --image flag.")

    t = args.tag if args.tag else 'latest'
    h = args.hostname if args.hostname else None
    c = args.count if args.count else 1
    a = args.args if args.args else None
    p = args.port if args.port else 50000

    docker_loop(image=args.image, t=t, h=h, c=c, a=a, p=p)
