#!/usr/bin/python

from argparse import ArgumentParser
import datetime

# BEEP MARKERS AARE CALCULATED BASED ON 15M BEEP TEST. 
# Variable, number of shuttles, level duration, shuttle duration 
# You can adjust this dictionary accordin to your beep test

def add_beep_markers(video, output, team, start_time):
    beep_test = [
                 (0, 0, 0, 0),
                 (1, 9, 57.2, 6.36),
                 (2, 10, 60, 6.00),
                 (3, 11, 62.5, 5.68),
                 (4, 11, 59.4, 5.40),
                 (5, 12, 61.7, 5.14),
                 (6, 12, 58.9, 4.91),
                 (7, 13, 61, 4.69),
                 (8, 13, 58.5, 4.50),
                 (9, 14, 60.5, 4.32),
                 (10, 14, 58.2, 4.16),
                 (11, 15, 60, 4.00),
                 (12, 16, 61.7, 3.86),
                 (13, 16, 59.6, 3.73),
                 (14, 17, 61.2, 3.60),
                 (15, 17, 59.2, 3.48),
                 (16, 18, 60.8, 3.38),
                 (17, 18, 58.9, 3.27),
                 (18, 19, 60.4, 3.18),
                 (19, 19, 58.6, 3.08),
                 (20, 20, 60, 3.00),
                 (21, 21, 61.3, 2.92)
                 ]

    print_header = f"""
    ffmpeg -y -i {video}  -vf "
     drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:
          text='%{{pts\:hms\:-{start_time}}}':
          enable='gte(t,{start_time})':
          x=(w-text_w)-10:
          y=10:
          fontsize=24:
          fontcolor=white:
          box=1:
          boxcolor=black@0.5,
     drawtext=text='00\\:00\\:00,000':fontcolor=white:box=1:boxcolor=black@0.5:fontsize=24:x=(w-text_w)-10:y=10:enable='between(t,0,{start_time})',
    drawtext=text='Level\: 1  Lap\: 0':fontcolor=white:box=1:boxcolor=black@0.5:fontsize=24:x=10:y=10:enable='between(t,0,{start_time})',
    """

    print(print_header)
    total_laps = 0
    start_time = start_time
    for x in beep_test[1:]:
      for lap in range(1, x[1]+1):
        total_laps += 1
        lap_duration=x[3]
        end_time=start_time+lap_duration
        start=str(datetime.timedelta(seconds=start_time).total_seconds())
        end=str(datetime.timedelta(seconds=end_time).total_seconds())
        print(f"drawtext=text='Level\\: {x[0]}  Lap\\: {lap}':fontcolor=white:box=1:boxcolor=black@0.5:fontsize=24:x=10:y=10:enable='between(t,{start},{end})',")
        start_time=start_time+lap_duration

    print_footer=f"""
    drawtext=text='{team}':fontcolor=white:box=1:boxcolor=black@0.5:fontsize=24:x=(w-text_w)/2:y=10
    " -c:a copy {output}
    """
    print(print_footer)




def get_args():
    parser = ArgumentParser()
    parser.add_argument("-s", "--start-time", help="time in the video when actual beep test starts, use if your video has 2-3 seconds of time prior to first beep",  default=0, dest='start_time', type=int)
    parser.add_argument("-t", "--team", help="PORT to bind on",  default='SK Šlapanice', dest='team', type=str)
    parser.add_argument("-v", "--video", help="input video, path to file",  default='input.mp4', dest='video', type=str)
    parser.add_argument("-o", "--output-video", help="output video",  default='output.mp4', dest='output', type=str)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    config = get_args()
    add_beep_markers(config.video, config.output, config.team, config.start_time)


