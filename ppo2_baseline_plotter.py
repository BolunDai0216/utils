import argparse
import re
import matplotlib.pyplot as plt

"""
I have been finding it difficult to visualize the output of baselines,
so I wrote something that can plot the reward or other stats when running ppo2.

When using this code run the OpenAI baselines ppo2 code using the following
command:

    python python -m baselines.run --alg=ppo2 --env=PongNoFrameskip-v4
    --num_timesteps=2e7 --save_path=~/models/pong_20M_ppo2
    > /some/dir/filename.txt

And then when plotting the terminal output run the following command:

    python ppo2_baseline_plotter.py --filename filename --keyword keyword

And the plot should show up.
"""

# You can also specify the file and keyword here
FILENAME = "/home/bolun/ppo2_ang_vel_disc_1e9_400_0806.txt"
KEYWORD = "eprewmean"


def parse_args():
    parser = argparse.ArgumentParser("Plot the output of baselines/ppo2")
    parser.add_argument("--filename", type=str, default=FILENAME,
                        help="name of the output file")
    parser.add_argument("--keyword", type=str, default=KEYWORD,
                        help="extracted data name")
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

    name = args.filename.split('/')[-1].split('.')[0]
    plt.plot(time_list, match_list)
    plt.title('{} -- {}'.format(name, args.keyword))
    plt.show()


if __name__ == '__main__':
    arglist = parse_args()
    main(arglist)
