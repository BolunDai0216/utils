import argparse
import re
import matplotlib.pyplot as plt


def parse_args():
    parser = argparse.ArgumentParser("Plot the output of baselines/ppo2")
    parser.add_argument("--filename", type=str, default="/home/bolun/ppo2_ang_vel_disc_1e9_400_0806.txt",
                        help="name of the output file")
    parser.add_argument("--keyword", type=str, default="eprewmean", help="extracted data name")
    return parser.parse_args()


def main(args):
    with open(args.filename, 'r') as f:
        content = f.read()
        key_pattern = re.compile('^\n| '+args.keyword+'.+')
        time_pattern = re.compile('^\n| '+'misc/total_timesteps'+'.+')
        matches = key_pattern.findall(content)
        time_matches = time_pattern.findall(content)
        match_list = []
        time_list = []
        for match, time in zip(matches, time_matches):
            match_list.append(float(match.split('| ')[1].split(' ')[0]))
            time_list.append(float(time.split('| ')[1].split(' ')[0]))

    plt.plot(time_list, match_list)
    plt.title('ppo2 ' + args.keyword)
    plt.show()


if __name__ == '__main__':
    arglist = parse_args()
    main(arglist)
